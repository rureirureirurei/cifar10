# cifar10 😔
Solving CIFAR10 without using conventional CNN approach. Based by this [paper](https://www-cs.stanford.edu/~acoates/papers/coatesng_nntot2012.pdf).

We use K-means features extraction and XGBoost model to achieve the accuracy of 0.6252.

Main notebook is `overview.ipynb`. Feel free to experiment and play with the model. 

### Results across different approaches. For more details please check the notebook.

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
