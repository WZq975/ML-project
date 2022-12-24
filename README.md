# ML-project

The dataset in this project is not publicly available and only used for this course：


Start to do feature classification:
```
$ python classification.py -h

usage: classification.py [-h] [--model MODEL] [--imp IMP] [--fd FD]

optional arguments:
  -h, --help     show this help message and exit
  --model MODEL  machine learning models: options are svm, rf (random forest),
                 and lr (logistic regression).
  --imp IMP      whether to plot feature importance in random forest, True or
                 False, require selecting random forest first if True.
  --fd FD        path of features
```
If you want to generate the features from scratch:
```
$ python stability.py
$ python saccade.py
$ python pursuit.py
$ python save_features.py
```
