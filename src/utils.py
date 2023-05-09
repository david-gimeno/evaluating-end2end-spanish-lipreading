import torch
import torch.nn as nn
import torch.utils.data as data
from unidecode import unidecode
from collections import OrderedDict

from src.MyDataset import MyDataset

from espnet2.text.build_tokenizer import build_tokenizer
from espnet2.text.token_id_converter import TokenIDConverter

def data_processing(data, transforms, tokenizer, converter, ignore_id):
    x_speech = []
    x_ilens = []
    y_labels = []
    y_olens = []
    refs = []

    for sampleID, speech, transcription in data:
        speech = transforms(speech) if transforms else speech

        x_speech.append(speech)
        x_ilens.append(speech.shape[0])

        label = torch.Tensor(converter.tokens2ids(tokenizer.text2tokens(transcription)))
        y_labels.append(label)
        y_olens.append(label.shape[0])

        refs.append(transcription)

    # -- video: (#batch, time, width, height)
    x_speech = nn.utils.rnn.pad_sequence(x_speech, padding_value=ignore_id, batch_first=True).type(torch.float32)
    x_ilens = torch.Tensor(x_ilens).type(torch.int64) # -- (#batch,)
    # -- (#batch, time)
    y_labels = nn.utils.rnn.pad_sequence(y_labels, padding_value=ignore_id, batch_first=True).type(torch.int64)
    y_olens = torch.Tensor(y_olens).type(torch.int64) # -- (#batch,)

    return x_speech, x_ilens, y_labels, y_olens, refs

def get_tokenizer_converter(token_type, bpemodel, token_list):
    tokenizer = build_tokenizer(token_type=token_type) if token_type is not None else None
    converter = TokenIDConverter(token_list=token_list)

    return tokenizer, converter

def get_dataloader(args, config, dataset, transforms, tokenizer, converter):
    kwargs = {"num_workers": 8, "pin_memory": True} if torch.cuda.is_available() else {}

    database = MyDataset(
        args.database,
        "../data/" + args.database + "/ROIs/",
        "../data/" + args.database + "/transcriptions/",
        "../data/" + args.database + "/splits/" + args.scenario + "/" + dataset + args.database + ".csv",
    )

    # -- creating data loader
    dataloader = data.DataLoader(dataset=database,
                    batch_size=1,
                    shuffle=False,
                    collate_fn=lambda x: data_processing(x, transforms, tokenizer, converter, config.model_conf["ignore_id"]),
                    **kwargs)

    return dataloader
