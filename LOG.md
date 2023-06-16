## Insights

#### Repo is not ment for training
Implementing ccda required some content of the folder structure and preprocessing steps, the authors took. What I found is that, there is no mention of `pred_hands` directory in the entire repository.
I think while doing the training seqentially (authors) they were unable to create a felexible training callback pipeline, as there seems to be no structure regarding the training procress.
Check out, [segmentors file](https://github.com/owenzlz/EgoHOS/blob/726dffca6939a629957b030937713c9cf537aee8/mmsegmentation/mmseg/models/segmentors/encoder_decoder.py#L93). the term `pred` is clearly for output predictions,
it shouldn't be a part of the core architecture pipeline. It is just bad practice. Going through git history of [segmentors_file](https://github.com/owenzlz/EgoHOS/commits/726dffca6939a629957b030937713c9cf537aee8/mmsegmentation/mmseg/models/segmentors/encoder_decoder.py) gives more insight to this argument.
A complete re-implementation of the pipeline is required. (+2 weeks)

#### ccda is baked into the repo, not an independent feature.
The `preprocessing_scripts` folder, has no organisation regarding what steps to follow. Going through the paper I have arranged in seqential order.

#### mmcv 2.0+ changes are quite significant.
Implementd a semantic segmentation pipeline in HandSeg.ipynb.
