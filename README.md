# Hand Segmentation

## Setup
create conda env using env.yml
cd mmsegmentation
pip install e .

## Inference on Videos

- Let's first download inference video. Update its path on pred_twohands_video.sh

- Predict hands and (1st order) interacting objects.
```bash
cd mmsegmentation
bash pred_twohands_video.sh
```
- Download the model weights form the drive and place it ./mmsegmentation/work_dirs
https://drive.google.com/drive/folders/1uza0YM6GGH6oyHKN2rg69KnxToilm3ky?usp=sharing
  
References:
**Fine-Grained Egocentric Hand-Object Segmentation: Dataset, Model, and Applications**\
*European Conference on Computer Vision (ECCV), 2022*\
[Lingzhi Zhang*](https://owenzlz.github.io/), [Shenghao Zhou*](https://scholar.google.com/citations?user=kWdwbUYAAAAJ&hl=en), [Simon Stent](https://scholar.google.com/citations?user=f3aij5UAAAAJ&hl=en), [Jianbo Shi](https://www.cis.upenn.edu/~jshi/) (* indicates equal contribution)
