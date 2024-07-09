import re
import torch
import numpy as np
import pandas as pd
from unidecode import unidecode
from torch.utils.data import Dataset

class MyDataset(Dataset):

    def __init__(self, database, rois_dir, text_dir, samples_csv):
        self.database = database
        self.rois_dir = rois_dir
        self.text_dir = text_dir
        samples = pd.read_csv(samples_csv, delimiter=",")

        if self.database in ["LIP-RTVE", "Multilingual-TEDx-Spanish", "CMU-MOSEAS-Spanish"]:
            self.delimiter = 5
            self.text_enc = "utf-8"

        elif self.database in ["VLRF"]:
            self.delimiter = 6
            self.text_enc = "utf-8"
            if "train" in samples_csv:
                samples.drop(samples[samples["sampleID"] == "speaker17003_22_01"])

        self.samples = samples["sampleID"].tolist()

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):
        sampleID = self.samples[index]

        lips = self.__get_visual_sample__(sampleID)
        transcription = self.__get_transcription_sample__(sampleID)

        return sampleID, lips, transcription

    def __get_visual_sample__(self, sampleID):
        spkrID = sampleID[:-self.delimiter]

        lips_path = self.rois_dir + spkrID + "/" + sampleID + ".npz"
        data = np.load(lips_path)
        lips = data[data.files[0]]

        return torch.from_numpy(lips) # (T,96,96)

    def __get_transcription_sample__(self, sampleID):
        spkrID = sampleID[:-self.delimiter]

        transcription_path = self.text_dir + spkrID + "/" + sampleID + ".txt"
        transcription = open(transcription_path, "r", encoding=self.text_enc).readlines()[0].strip()

        if self.database in ["LIP-RTVE", "VLRF"]:
            transcription = transcription.lower()
            transcription = re.sub(r"[^\w\s]","",transcription)
            transcription = unidecode(transcription.replace("ñ", "N")).replace("N", "ñ")
        else:
            transcription = transcription.replace("{", "").replace("}", "")

        return transcription
