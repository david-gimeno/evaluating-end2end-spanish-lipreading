#! /usr/bin/env python
# -*- coding: utf-8 -*-

import torch
import random
import numpy as np
import torchaudio
import torch.nn as nn
from typing import List, Optional, Tuple, Union

class Compose(object):
    """Compose several preprocess together.
    """

    def __init__(self, preprocess):
        """__init__.
        Args:
            preprocess (list of ``Preprocess`` objects): list of preprocess to compose.
        """
        self.preprocess = preprocess

    def __call__(self, video_data: torch.Tensor
    ) -> torch.Tensor:
        """
        Args:
            video_data (torch.Tensor): input video sequence.
        Returns:
            torch.Tensor: the preprocessed video sequence.
        """
        for p in self.preprocess:
            if p is not None:
                video_data = p(video_data)
        return video_data

class Normalise(object):
    """Normalise a Tensor image sequence with mean and standard deviation.
    """

    def __init__(self, mean, std):
        self.mean = mean
        self.std = std

    def __call__(self, video_data: torch.Tensor
    ) -> torch.Tensor:
        """
        Args:
            video_data (torch.Tensor): input video sequence to be normalised.
        Returns:
            torch.Tensor: Normalised video sequence.
        """
        return (video_data - self.mean) / self.std

    def __repr__(self):
        return self.__class__.__name__+'(mean={0}, std={1})'.format(self.mean, self.std)

class CenterCrop(object):
    """Crop each image of the video sequence at the center.
    """

    def __init__(self, crop_size):
        self.crop_size = crop_size

    def __call__(self, video_data):
        """
        Args:
            video_data (torch.Tensor): Video sequence to be cropped.
        Returns:
            torch.Tensor: Cropped video sequence.
        """
        frames, h, w = video_data.shape
        th, tw = self.crop_size
        delta_w = int(round((w - tw))/2.)
        delta_h = int(round((h - th))/2.)
        return video_data[:, delta_h:delta_h+th, delta_w:delta_w+tw]

    def __repr__(self):
        return self.__class__.__name__ + '(size={0})'.format(self.crop_size)
