<h1 align="center">Factors of Influence on <br/> End-to-End Continuous Spanish Lipreading</h1>

Thanks to the availability of large-scale audiovisual databases and the use of powerful attention-based mechanisms, unprecedented results have been achieved in Visual Speech Recognition. However, the use of these technologies in languages other than English is quite limited. In our paper, in addition to studying how the different components that form the architecture influence the quality of speech recognition, we presented a new Spanish Lipreading Benchmark. It covers diverse scenarios with different recording settings, speaker-dependent and speaker-independent experiments, as well as data-scarcity databases.

<details open>
  <summary><b>Spanish Lipreading Benchmark</b></summary>

<p> </p>
  
|            Models          |     %WER    |               Download               |  size (MB)  |
|:---------------------------|:-----------:|:------------------------------------:|:-----------:|
|  [**VLRF**](https://ieeexplore.ieee.org/abstract/document/7961743)                  |
|  **speaker-dependent**     |  24.8 ± 3.4 | [GoogleDrive](https://drive.google.com/file/d/18dQbL2Ul9g00AK7b0k1tK-AcNbd2-xs3/view?usp=share_link) |     201     |
|  Language Model            |      -      | [GoogleDrive](https://drive.google.com/file/d/1DuSO8FZWSSPZLRCg8puqk2710-NtDls3/view?usp=share_link) |     193     |
|  Landmarks                 |      -      | [GoogleDrive](https://drive.google.com/file/d/1oOoMmKYSNifEjbUU-5rtmgR-7vq4vtYL/view?usp=share_link) |     248     |
|  -                         |             |                                      |             |
|  [**LIP-RTVE**](https://aclanthology.org/2022.lrec-1.294/)              |            
|  **speaker-independent**   |  59.5 ± 1.2 | [GoogleDrive](https://drive.google.com/file/d/1HUipOpIOWtsAvBB2mIFAxHbSVB7S5bk8/view?usp=share_link) |     201     |
|  **speaker-dependent**     |  34.2 ± 1.2 | [GoogleDrive](https://drive.google.com/file/d/1Zq476xT2TVa-DDEDhLaLlYRsEFqRd8CK/view?usp=share_link) |     201     |
|  Language Model            |      -      | [GoogleDrive](https://drive.google.com/file/d/1Ze7zOII8MbgUQqZ4U3gYOAnobp3aDJnT/view?usp=share_link) |     193     |
|  Landmarks                 |      -      | [GoogleDrive](https://drive.google.com/file/d/1_gXDV3mC3GhSx9OSe2zjm0Xh-e2m7Fe3/view?usp=share_link) |     535     |
|  -                         |             |                                      |             |
  |  [**CMU-MOSEAS**](https://aclanthology.org/2020.emnlp-main.141/) <sup>**†**</sup>          |
|  **speaker-independent**   |  44.6 ± 0.6 | [GoogleDrive](https://drive.google.com/file/d/1f79zKcvaR9xRfRpSdLgCzLS7BTjC5tmf/view?usp=share_link) |     201     |
|  Language Model <sup>**†**</sup>            |      -      | [GoogleDrive](https://drive.google.com/file/d/15RLM1qYQXRIkrKVPYPeNWoP2G78-geL2/view?usp=share_link) |     193     |
|  Landmarks                 |      -      | [GoogleDrive](https://drive.google.com/file/d/1wBYCDYq8JCjBl4rFYJjW4eQiXsQkS3TK/view?usp=share_link) |     2970    |
|  -                         |             |                                      |             |
|  [**Multilingual-TEDx**](https://www.isca-speech.org/archive/interspeech_2021/salesky21_interspeech.html) <sup>**†**</sup>     |
|  **speaker-independent**   |  56.3 ± 0.3 | [GoogleDrive](https://drive.google.com/file/d/1f79zKcvaR9xRfRpSdLgCzLS7BTjC5tmf/view?usp=share_link) |     201     |
|  Language Model <sup>**†**</sup>            |      -      | [GoogleDrive](https://drive.google.com/file/d/15RLM1qYQXRIkrKVPYPeNWoP2G78-geL2/view?usp=share_link) |     193     |
|  Landmarks                 |      -      | [GoogleDrive](https://drive.google.com/file/d/1cYXYE0uIq-Cma4wE5-gjZO1AJ2WYlcv8/view?usp=share_link) |     2930    |

</details>
<sup>**†**</sup> These models were published by [Ma et al. (2022)](https://github.com/mpc001/Visual_Speech_Recognition_for_Multiple_Languages) However, the structere of the indicated checkpoints have been modified so that they can be loaded using the scripts provided in this repository.

Models publicly released by [Pingchuan Ma (2022)](https://github.com/mpc001/Visual_Speech_Recognition_for_Multiple_Languages) but modified thus the checkpoints can be loaded by the scripts provided in this repository.

## Authors

[David Gimeno-Gómez](https://scholar.google.es/citations?user=DVRSla8AAAAJ&hl=en) \& [Carlos-David Martínez-Hinarejos](http://personales.upv.es/carmarhi/)

## License

It is noted that the code can be used for research and/or benchmarking purposes. It is now allowed to use the code for commercial purposes. 

## Citation

## Acknowledgements

This work was partially supported by Grant CIACIF/2021/295 funded by Generalitat Valenciana and by Grant PID2021-124719OB-I00 under project LLEER (PID2021-124719OB-100) funded by MCIN/AEI/10.13039/501100011033/ and by ERDF, EU A way of making Europe.
