#!/usr/bin/env python3
from src.tasks.asr import ASRTask
from src.bin.asr_inference import Speech2Text

import os
import sys
import yaml
import argparse
from tqdm import tqdm
from colorama import Fore
from pathlib import Path

import torch
import torch.nn as nn

from src.utils import *
from src.Tasas import computeTasas
from src.Transforms import *

def inference(args, speech2text, eval_loader, dataset):
    print(f"Decoding {dataset.upper()} dataset:")
    enc = "utf-8" if args.database not in ["VLRF"] else "ISO-8859-1"

    # -- obtaining hypothesis
    dst_dir = os.path.join(args.output_dir, "inference/")
    os.makedirs(dst_dir, exist_ok=True)
    dst_path = os.path.join(dst_dir, dataset+".inf")
    with open(dst_path, "w", encoding=enc) as f:
        with torch.no_grad():
            for xs_pad, ilens, ys_pad, olens, refs in tqdm(eval_loader, position=0, leave=True, file=sys.stdout, bar_format="{l_bar}%s{bar:10}%s{r_bar}" % (Fore.YELLOW, Fore.RESET)):
                result = speech2text(torch.squeeze(xs_pad, 0))
                # -- dumping results
                hyp = result[0][0]
                f.write(refs[0].strip() + "#" + hyp.strip() + "\n")

    # -- computing WER
    wer, cer, ci_wer, ci_cer = computeTasas(dst_path)
    report_wer = "%WER: " + str(wer) + " ± " + str(ci_wer); print(f"\n{report_wer}")
    report_cer = "%CER: " + str(cer) + " ± " + str(ci_cer); print(report_cer)
    with open(dst_path.replace(".inf", ".wer"), "w", encoding="utf-8") as f:
        f.write(report_wer + "\n")
        f.write(report_cer + "\n")

if __name__ == "__main__":
    # -- parsing command line arguments
    parser = argparse.ArgumentParser(description="Factors of Influence on End-to-End Continous Spanish Lipreading",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("--cuda", default=0, type=int, help="Cuda device.")
    parser.add_argument("--database", default="LIP-RTVE", type=str, help="Choose a database.")
    parser.add_argument("--scenario", default="speaker-independent", type=str, help="Choose a scenario.")

    parser.add_argument("--vsr-config-file", default="./configs/VSR/vsr_conv3dresnet18_conformer_ctc+transformer.yaml", type=str, help="Path to a config file that specifies the VSR model architecture.")
    parser.add_argument("--load-vsr", required=True, type=str, help="Path to load a pretrained VSR model.")
    parser.add_argument("--lm-config-file", default="./configs/LM/transformer-lm.yaml", type=str, help="Path to a config file that specifies the LM architecture.")
    parser.add_argument("--load-lm", default="", type=str, help="Path to load a pre-trained LM.")

    parser.add_argument("--output-dir", required=True, type=str, help="Path to save the inference hypothesis.")

    args = parser.parse_args()

    # -- configuration architecture details
    vsr_config_file = Path(args.vsr_config_file)
    with vsr_config_file.open("r", encoding="utf-8") as f:
        vsr_config = yaml.safe_load(f)
    vsr_config = argparse.Namespace(**vsr_config)

    # -- setting device
    device = torch.device("cuda:"+str(args.cuda))

    # -- building tokenizer and converter
    tokenizer, converter = get_tokenizer_converter(vsr_config.token_type, vsr_config.bpemodel, vsr_config.token_list)

    # -- preprocessing data
    if args.database == "LIP-RTVE":
        (mean, std) = (0.491, 0.166)
    elif args.database == "VLRF":
        (mean, std) = (0.392, 0.142)
    else:
        (mean, std) = (0.421, 0.165)
    fps = 50 if args.database in ["VLRF"] else 25

    test_visual_transforms = Compose([
        Normalise(0.0, 250.0),
        Normalise(mean, std),
        CenterCrop((88,88))
    ])

    # -- inference
    print("\nINFERENCE PHASE\n")
    if args.load_lm == "":
        print("No LM considered during inference!")

    # -- -- building speech-to-text recoginiser
    speech2text = Speech2Text(
        asr_train_config= args.vsr_config_file,
        asr_model_file=args.load_vsr,
        lm_train_config=args.lm_config_file if args.lm_config_file != "" else None,
        lm_file=args.load_lm if args.load_lm != "" else None,
        **vsr_config.inference_conf,
    )
    # -- -- creating development & test dataloaders
    test_loader = get_dataloader(args, vsr_config, dataset="test", transforms=test_visual_transforms, tokenizer=tokenizer, converter=converter)

    # -- -- visually infering speech
    inference(args, speech2text, test_loader, "test")
