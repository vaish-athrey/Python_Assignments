# -*- coding: utf-8 -*-
"""Sign Language to Speech.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LLRCjMVGIr8iGGg6Zw1XeKXdZF8iQkoT
"""

import numpy as np
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense,Flatten,Conv2D,MaxPool2D,Dropout
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_df=pd.read_csv('/content/sign_mnist_train.csv')
test_df=pd.read_csv('/content/sign_mnist_test.csv')

train_df.head(6)

train_label=train_df['label']
train_label.head()
trainset=train_df.drop(['label'],axis=1)
trainset.head()

#convert to numpy array
X_train = trainset.values
X_train = trainset.values.reshape(-1,28,28,1)
print(X_train.shape)

test_label=test_df['label']
X_test=test_df.drop(['label'],axis=1)
print(X_test.shape)
X_test.head()

from sklearn.preprocessing import LabelBinarizer
lb=LabelBinarizer()
y_train=lb.fit_transform(train_label)
y_test=lb.fit_transform(test_label)
y_train

X_test=X_test.values.reshape(-1,28,28,1)

print(X_train.shape,y_train.shape,X_test.shape,y_test.shape)















