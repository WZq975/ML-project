# ML-project

The dataset in this project is not publicly available and only used for this course：

Google Drive: https://drive.google.com/file/d/1fay7AFjkgrEO_31Q5zbvrD0z20QqW6pI/view?usp=share_link

The "dataset" should be placed in the "scripts" fold as .../scripts/dataset/...

Then start to do feature classification:
```
$ python classification.py -h

usage: classification.py [-h] [--model MODEL] [--imp IMP]

optional arguments:
  -h, --help     show this help message and exit
  --model MODEL  machine learning models: options are svm, rf (random forest),
                 and lr (logistic regression).
  --imp IMP      whether to plot feature importance in random forest, True or
                 False, require selecting random forest first if True.
                 
```
If you want to generate the features from scratch:
```
$ python stability.py
$ python saccade.py
$ python pursuit.py
$ python save_features.py
```
