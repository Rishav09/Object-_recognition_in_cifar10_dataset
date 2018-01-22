# Object-_recognition_in_cifar10_dataset
Object recognition is done on cifar-10 dataset using a simple convolutional neural network and a deeper convolutional network.



`Keras version=2.1.3`


`python=3.x`


`using tensorflow backend`.

The project contains 2 files-

## Simple CNN

### Architecture-


* Conv Input Layer-32\*3\*3,relu activation function.
* Dropout-20%.
* Convolution Layer-32\*3\*3.
* Max Pooling Layer-2\*2.
* Flatten Layer.
* FC layer with 512 units and a rectifier activation function.
* Dropout=50%.
* FC layer with 10 units and a softmax activation function.

## Larger CNN

### Architecture-
* Conv Input Layer-32\*3\*3,relu activation function.
* Dropout-20%.
* Convolution Layer-32\*3\*3.
* Convolution Layer-64\*3\*3
* Dropout-20%
* Convolution Layer-64\*3\*3
* Max Pool Layer-2\*2
* Convolution Layer-128\*3\*3
* Max Pool Layer-2\*2
* Flatten Layer
* Dropout Layer
* FC Layer-1024 units and a relu activation function
* Dropout Layer-20%
* FC Output Layer-10 units and a softmax activation function

Conv Nets were trained on Amazon EC2 instances using g2.2x large gpu.


Accuracy obtained was 70 and 75 % respectively.
