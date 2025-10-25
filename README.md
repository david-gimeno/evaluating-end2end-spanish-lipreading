<h1 align="center">Factors of Influence on <br/> End-to-End Continuous Spanish Lipreading</h1>

<div align="center">
  <b><a href="https://scholar.google.es/citations?user=DVRSla8AAAAJ&hl=en">David Gimeno Gómez</a> & <a href="http://personales.upv.es/carmarhi/">Carlos-David Martínez-Hinarejos</a></b>
</div>

<br/>
Thanks to the availability of large-scale audiovisual databases and the use of powerful attention-based mechanisms, unprecedented results have been achieved in Visual Speech Recognition. However, the use of these technologies in languages other than English is quite limited. In our paper, in addition to studying how the different components that form the architecture influence the quality of speech recognition, we presented a new Spanish Lipreading Benchmark. It covers diverse scenarios with different recording settings, speaker-dependent and speaker-independent experiments, as well as data-scarcity databases.
<br/>


## Spanish Lipreading Benchmark

Pre-trained checkpoints for both VSR and LM models, as well as the extracted facial landmarks of all corpora except for MuAViC (check its original [repo](https://github.com/facebookresearch/muavic)), are available for downloading in [Zenodo](https://zenodo.org/records/17443293).
  
<p> </p>
  
|            Models          |     %WER    |
|:---------------------------|:-----------:|
|  [**VLRF**](https://ieeexplore.ieee.org/abstract/document/7961743/)                 |
|  **speaker-dependent**     |  24.8 ± 3.4 |
|  -                         |             |
|  [**LIP-RTVE**](https://aclanthology.org/2022.lrec-1.294/)              |            
|  **speaker-independent**   |  59.5 ± 1.2 |
|  **speaker-dependent**     |  34.2 ± 1.2 |
|  -                         |             |                                      |             |
  |  [**CMU-MOSEAS**](https://aclanthology.org/2020.emnlp-main.141/) <sup>**†**</sup>          |
|  **speaker-independent**   |  44.6 ± 0.6 |
|  -                         |             |                                      |             |
|  [**MuAViC**](https://www.isca-archive.org/interspeech_2023/anwar23_interspeech.html) <sup>**†**</sup>    |
|  **speaker-independent**   |  56.3 ± 0.3 |

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
