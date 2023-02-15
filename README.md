# cifar10 🤪
Solving cifar10! 

Here's a table with some results I got!

| Model | Accuracy |
|------|----------|
| default | 0.4535 |
| (1) | 0.5168|
| (2) | 0.4856|
| (3) | 0.4856|
| (4) | 0.5443|




* More features (1)
```
PATCH_SIZE = 4
PATCH_NUM  = 1000000
STRIDE     = 2
K          = 256
```

* Slightly more features (2)
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

activation: relu
loss:       categorical_crossentropy
optimizer:  adam
```
* Simple neural network (4)
```
PATCH_SIZE = 12
PATCH_NUM  = 1000000
STRIDE     = 6
K          = 256

Neural network achitecture:

dense 1024 -> dense 1024 -> dense 1024 -> dense 10

dropout:    0.2
activation: relu
loss:       categorical_crossentropy
optimizer:  adam
```
