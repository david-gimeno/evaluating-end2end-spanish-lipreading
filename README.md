<h1 align="center">Factors of Influence on <br/> End-to-End Continuous Spanish Lipreading</h1>

Thanks to the availability of large-scale audiovisual databases and the use of powerful attention-based mechanisms, unprecedented results have been achieved in Visual Speech Recognition. However, the use of these technologies in languages other than English is quite limited. In our paper, in addition to studying how the different components that form the architecture influence the quality of speech recognition, we presented a new Spanish Lipreading Benchmark. It covers diverse scenarios with different recording settings, speaker-dependent and speaker-independent experiments, as well as data-scarcity databases.

<details open>
  <summary><b>Spanish Lipreading Benchmark</b></summary>

<p> </p>
  
|            Models          |     %WER    |               Download               |  size (MB)  |
|:---------------------------|:-----------:|:------------------------------------:|:-----------:|
|  [**VLRF**](https://ieeexplore.ieee.org/abstract/document/7961743)                  |
|  **speaker-dependent**     |  24.8 ± 3.4 | [GoogleDrive](https://drive.google.com/file/d/18dQbL2Ul9g00AK7b0k1tK-AcNbd2-xs3/view?usp=share_link) |     201     |
|  Language Model<sup>**+**</sup>            |      -      | [GoogleDrive](https://drive.google.com/file/d/1DuSO8FZWSSPZLRCg8puqk2710-NtDls3/view?usp=share_link) |     193     |
|  Landmarks                 |      -      | [GoogleDrive](http://bit.ly/40EAtyX) |     260     |
|  -                         |             |                                      |             |
|  [**LIP-RTVE**](https://aclanthology.org/2022.lrec-1.294/)              |            
|  **speaker-independent**   |  59.5 ± 1.2 | [GoogleDrive](https://drive.google.com/file/d/1HUipOpIOWtsAvBB2mIFAxHbSVB7S5bk8/view?usp=share_link) |     201     |
|  **speaker-dependent**     |  34.2 ± 1.2 | [GoogleDrive](https://drive.google.com/file/d/1Zq476xT2TVa-DDEDhLaLlYRsEFqRd8CK/view?usp=share_link) |     201     |
|  Language Model            |      -      | [GoogleDrive](https://drive.google.com/file/d/1Ze7zOII8MbgUQqZ4U3gYOAnobp3aDJnT/view?usp=share_link) |     193     |
|  Landmarks                 |      -      | [GoogleDrive](http://bit.ly/40EAtyX) |     562     |
|  -                         |             |                                      |             |
  |  [**CMU-MOSEAS**](https://aclanthology.org/2020.emnlp-main.141/)<sup>**†**</sup>          |
|  **speaker-independent**   |  44.6 ± 0.6 | [GoogleDrive](https://drive.google.com/file/d/1f79zKcvaR9xRfRpSdLgCzLS7BTjC5tmf/view?usp=share_link) |     201     |
|  Language Model<sup>**†**</sup>            |      -      | [GoogleDrive](https://drive.google.com/file/d/15RLM1qYQXRIkrKVPYPeNWoP2G78-geL2/view?usp=share_link) |     193     |
|  Landmarks                 |      -      | [GoogleDrive](http://bit.ly/40EAtyX) |     3187    |
|  -                         |             |                                      |             |
|  [**Multilingual-TEDx**](https://www.isca-speech.org/archive/interspeech_2021/salesky21_interspeech.html)<sup>**†**</sup>     |
|  **speaker-independent**   |  56.3 ± 0.3 | [GoogleDrive](https://drive.google.com/file/d/1f79zKcvaR9xRfRpSdLgCzLS7BTjC5tmf/view?usp=share_link) |     201     |
|  Language Model<sup>**†**</sup>            |      -      | [GoogleDrive](https://drive.google.com/file/d/15RLM1qYQXRIkrKVPYPeNWoP2G78-geL2/view?usp=share_link) |     193     |
|  Landmarks                 |      -      | [GoogleDrive](http://bit.ly/40EAtyX) |     3143    |

</details>

<sup>**†**</sup> These models were published by [Ma et al. (2022)](https://github.com/mpc001/Visual_Speech_Recognition_for_Multiple_Languages) However, the structere of the indicated checkpoints have been modified so that they can be loaded using the scripts provided in this repository.

Models publicly released by [Pingchuan Ma (2022)](https://github.com/mpc001/Visual_Speech_Recognition_for_Multiple_Languages) but modified thus the checkpoints can be loaded by the scripts provided in this repository.

## Authors

[David Gimeno-Gómez](https://scholar.google.es/citations?user=DVRSla8AAAAJ&hl=en) \& [Carlos-David Martínez-Hinarejos](http://personales.upv.es/carmarhi/)

## License

It is noted that the code can only be used for comparative or benchmarking purposes. Users can only use code supplied for non-commercial purposes.

## Citation
