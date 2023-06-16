# Hand Segmentation

## Setup
create conda env using env.yml
(install mmcv with cuda, if conda env doesn't.)    
cd mmsegmentation  
pip install e .  

## Inference on Videos

- First download inference video or any video. Update its path on `pred_twohands_video.sh`.
- Download the checkpoints, using `download_checkpoints`.
- Predict hands segments in the video.
```bash
cd mmsegmentation
bash pred_twohands_video.sh
```

References:
**Fine-Grained Egocentric Hand-Object Segmentation: Dataset, Model, and Applications**\
*European Conference on Computer Vision (ECCV), 2022*\
[Lingzhi Zhang*](https://owenzlz.github.io/), [Shenghao Zhou*](https://scholar.google.com/citations?user=kWdwbUYAAAAJ&hl=en), [Simon Stent](https://scholar.google.com/citations?user=f3aij5UAAAAJ&hl=en), [Jianbo Shi](https://www.cis.upenn.edu/~jshi/) (* indicates equal contribution)
