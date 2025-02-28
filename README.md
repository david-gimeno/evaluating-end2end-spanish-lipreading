<h1 align="center">Factors of Influence on <br/> End-to-End Continuous Spanish Lipreading</h1>

<div align="center">
  <b><a href="https://scholar.google.es/citations?user=DVRSla8AAAAJ&hl=en">David Gimeno Gómez</a> & <a href="http://personales.upv.es/carmarhi/">Carlos-David Martínez-Hinarejos</a></b>
</div>

<br/>
Thanks to the availability of large-scale audiovisual databases and the use of powerful attention-based mechanisms, unprecedented results have been achieved in Visual Speech Recognition. However, the use of these technologies in languages other than English is quite limited. In our paper, in addition to studying how the different components that form the architecture influence the quality of speech recognition, we presented a new Spanish Lipreading Benchmark. It covers diverse scenarios with different recording settings, speaker-dependent and speaker-independent experiments, as well as data-scarcity databases.
<br/>


## Spanish Lipreading Benchmark
  
<p> </p>
  
|            Models          |     %WER    |               Download               |  size (MB)  |
|:---------------------------|:-----------:|:------------------------------------:|:-----------:|
|  [**VLRF**](https://ieeexplore.ieee.org/abstract/document/7961743)                  |
|  **speaker-dependent**     |  24.8 ± 3.4 | [vsr-vlrf.pth](https://drive.google.com/file/d/18dQbL2Ul9g00AK7b0k1tK-AcNbd2-xs3/view?usp=share_link) |     201     |
|  Language Model            |      -      | [lm-vlrf.pth](https://drive.google.com/file/d/1DuSO8FZWSSPZLRCg8puqk2710-NtDls3/view?usp=share_link) |     193     |
|  Landmarks                 |      -      | [landmarks-vlrf.zip](https://drive.google.com/file/d/1oOoMmKYSNifEjbUU-5rtmgR-7vq4vtYL/view?usp=share_link) |     248     |
|  -                         |             |                                      |             |
|  [**LIP-RTVE**](https://aclanthology.org/2022.lrec-1.294/)              |            
|  **speaker-independent**   |  59.5 ± 1.2 | [vsr-liprtve-si.pth](https://drive.google.com/file/d/1HUipOpIOWtsAvBB2mIFAxHbSVB7S5bk8/view?usp=share_link) |     201     |
|  **speaker-dependent**     |  34.2 ± 1.2 | [vsr-liprtve-sd.pth](https://drive.google.com/file/d/1Zq476xT2TVa-DDEDhLaLlYRsEFqRd8CK/view?usp=share_link) |     201     |
|  Language Model            |      -      | [lm-liprtve.pth](https://drive.google.com/file/d/1Ze7zOII8MbgUQqZ4U3gYOAnobp3aDJnT/view?usp=share_link) |     193     |
|  Landmarks                 |      -      | [landmarks-liprtve.zip](https://drive.google.com/file/d/1_gXDV3mC3GhSx9OSe2zjm0Xh-e2m7Fe3/view?usp=share_link) |     535     |
|  -                         |             |                                      |             |
  |  [**CMU-MOSEAS**](https://aclanthology.org/2020.emnlp-main.141/) <sup>**†**</sup>          |
|  **speaker-independent**   |  44.6 ± 0.6 | [vsr-ma2022-spanish.pth](https://drive.google.com/file/d/1f79zKcvaR9xRfRpSdLgCzLS7BTjC5tmf/view?usp=share_link) |     201     |
|  Language Model <sup>**†**</sup>            |      -      | [lm-ma2022-spanish.pth](https://drive.google.com/file/d/15RLM1qYQXRIkrKVPYPeNWoP2G78-geL2/view?usp=share_link) |     193     |
|  Landmarks                 |      -      | [landmarks-cmumoseas-spanish.zip](https://drive.google.com/file/d/1wBYCDYq8JCjBl4rFYJjW4eQiXsQkS3TK/view?usp=share_link) |     2970    |
|  -                         |             |                                      |             |
|  [**MuAViC**](https://www.isca-archive.org/interspeech_2023/anwar23_interspeech.html) <sup>**†**</sup>    |
|  **speaker-independent**   |  56.3 ± 0.3 | [vsr-ma2022-spanish.pth](https://drive.google.com/file/d/1f79zKcvaR9xRfRpSdLgCzLS7BTjC5tmf/view?usp=share_link) |     201     |
|  Language Model <sup>**†**</sup>            |      -      | [lm-ma2022-spanish.pth](https://drive.google.com/file/d/15RLM1qYQXRIkrKVPYPeNWoP2G78-geL2/view?usp=share_link) |     193     |
|  Landmarks                 |      -      | [Can be found in the original GitHub repository](https://github.com/facebookresearch/muavic) |     -    |

<b><sup>†</sup></b> These models were published by <a href="https://github.com/mpc001/Visual_Speech_Recognition_for_Multiple_Languages">Ma et al. (2022)</a>. However, the structure of the indicated checkpoints has been modified so that they can be loaded using the scripts provided in this repository.

## Preparation
1. Clone the Github repository and enter it locally:

```
git clone https://github.com/david-gimeno/Factors_of_Influence_on_End-to-End_Continuous_Spanish_Lipreading.git
cd Factors_of_Influence_on_End-to-End_Continuous_Spanish_Lipreading/
```

2. Create a Conda environment:

```
conda create -y -n vsr-factors python=3.8
conda activate vsr-factors
```

3. Install required pip packages:

```
./prepare_env.sh
```

4. Download the database you are interested on.

5. Considering the [src/MyDataset.py]() script as an example, implement your own Dataset object according to the way you structured your database of interest. It will also be useful to inspect the [src/utils.py]() script.

## Benchmark Evaluation

An usage example for the speaker-dependent partition of the LIP-RTVE database (using the LM fine-tuned to the task) would be to execute the following command:

```
python vsr_main.py --database LIP-RTVE \
                   --scenario speaker-dependent \
                   --load-vsr ./models/VSR/liprtve-sd.pth \
                   --load-lm ./models/LM/lm-liprtve.pth \
                   --output-dir ./spanish-benchmark/liprtve-sd/lm-finetuned/
```
If you do not want to use any LM, just discard the ```--load-lm``` argument.

## License

It is noted that the code can be used for research and/or benchmarking purposes. It is not allowed to use the code for commercial purposes. 

## Citation

If you find our work interesting or you use our VSR models, please cite our paper:

```
@article{gimeno2025evaluation,
  author={Gimeno-G{\'o}mez, D. and Mart{\'\i}nez-Hinarejos, C.-D.},
  title={{Evaluation of End-to-End Continuous Spanish Lipreading in Different Data Conditions}},
  journal={Language Resources and Evaluation},
  year={2025},
  doi={10.1007/s10579-025-09809-4},
  issn={1574-0218},
}
```

## Acknowledgements

This work was partially supported by Grant CIACIF/2021/295 funded by Generalitat Valenciana and by Grant PID2021-124719OB-I00 under project LLEER (PID2021-124719OB-100) funded by MCIN/AEI/10.13039/501100011033/ and by ERDF, EU A way of making Europe.
