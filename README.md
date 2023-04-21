# cifar10 😔
Solving CIFAR10 without using CNN.

Based on [this paper](https://www-cs.stanford.edu/~acoates/papers/coatesng_nntot2012.pdf)
and [this notebook](https://github.com/marekpiotradamczyk/ml_uwr_22/blob/main/kmeans_deep_features.ipynb)

Main notebook is nn.ipynb.

Right now it's a real mess, I might tidy things up later.

# Results

| Model | Accuracy |
|------|----------|
| default | 0.4535 |
| (1) Logistic regression | 0.5168|
| (2) Logistic regression| 0.4856|
| (3) Neural network | 0.4856|
| (4) Neural network | 0.5625|
| (5) Random forest | 0.4789|
| (6) XGBoost | 0.5464|
| (7) XGBoost NO FEATURES | 0.5381|
| (8) XGBoost 220 | 0.6252|

Best accuracy: 0.6252


Some insights I got when experimenting:
1) Optimal PATCH_NUM is approximately 30000. (Tested with k = 64)
2) The optimal value of K is approximately 72. (Increasing K did not result in a decrease in accuracy, but significantly increased the training time required)
3) STRIDE 2 is the best
4) Increasing XGBoost depth can improve accuracy although training takes ungodly amounts of time


Explanations for the results table:
* More features logreg (1)
```
PATCH_SIZE = 4
PATCH_NUM  = 1000000
STRIDE     = 2
K          = 256
```

* Slightly more features logreg (2)
```
PATCH_SIZE = 6
PATCH_NUM  = 100000
STRIDE     = 8
K          = 64
```
* Simple neural network (3)
```
PATCH_SIZE = 4
PATCH_NUM  = 1000000
STRIDE     = 2
K          = 64

Neural network achitecture:

dense 1024 -> dense 512 -> dense 10

activation : relu
loss       : categorical_crossentropy
optimizer  : adam
```
* A bit tuned neural network (4)
```
PATCH_SIZE = 12
PATCH_NUM  = 1000000
STRIDE     = 6
K          = 256

Neural network achitecture:

dense 1024 -> dense 1024 -> dense 1024 -> dense 10

dropout    : 0.2
activation : relu
loss       : categorical_crossentropy
optimizer  : adam
```
* Random Forest (5)
```
PATCH_SIZE = 7
PATCH_NUM  = 2000000
STRIDE     = 5
K          = 256

default
```
* XGBoost (6)
```
PATCH_SIZE = 8
PATCH_NUM  = 1000000
STRIDE     = 6
K          = 32

max depth  : 15
estimators : 60
```
* XGBoost (7)
```
max depth  : 6
estimators : 100
```
* XGBoost (8)
```
PATCH_SIZE = 10
PATCH_NUM  = 4000000
STRIDE     = 5
K          = 128

max depth  : 10
estimators : 220
```
