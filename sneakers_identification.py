# -*- coding: utf-8 -*-
"""Copy of Copy of Copy of Sneakers Identification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/134QYLRmywuD-rsd7xk_Vl7RPz5wAP7NC
"""

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import cv2
import os

"""Mounting drive to import data"""

from google.colab import drive
drive.mount('/content/drive')

"""Loading image from drive"""

img = image.load_img("/content/drive/MyDrive/Dataset/Training /Original Sneakers/Authentic60.jpg")
plt.imshow(img)

"""Reading the shape of image"""

cv2.imread("/content/drive/MyDrive/Dataset/Training /Original Sneakers/Authentic10.jpg").shape

"""Rescaling the RGB values of images"""

train = ImageDataGenerator(rescale = 1/255)
validation = ImageDataGenerator(rescale = 1/255)

"""Providing datasets to nueral network with specifications for training"""

train_dataset = train.flow_from_directory('/content/drive/MyDrive/Dataset/Training ',
target_size = (200, 200),
batch_size = 3,
class_mode = 'binary')

validation_dataset = train.flow_from_directory('/content/drive/MyDrive/Dataset/Validation',
target_size = (200, 200),
batch_size = 3,
class_mode = 'binary')

"""Labels generated with functions"""

train_dataset.class_indices

"""Using CNN with max pooling and applying filters"""

model = tf.keras.models.Sequential([tf.keras.layers.Conv2D(16,(3,3), activation = 'relu', input_shape = (200, 200, 3)),
                                    tf.keras.layers.MaxPool2D(2,2),
                                    #
                                    tf.keras.layers.Conv2D(32,(3,3), activation = 'relu'),
                                    tf.keras.layers.MaxPool2D(2,2),
                                    #
                                    tf.keras.layers.Conv2D(64,(3,3), activation = 'relu'),
                                    tf.keras.layers.MaxPool2D(2,2),
                                    ##
                                    tf.keras.layers.Flatten(),
                                    ##
                                    tf.keras.layers.Dense(512,activation = 'relu'),
                                    ##
                                    tf.keras.layers.Dense(1,activation = 'sigmoid'),
                                    ])

"""Compiling the model"""

model.compile(loss = 'binary_crossentropy',
              optimizer = RMSprop(learning_rate=0.001),
              metrics = ['accuracy'])

"""Training the model"""

model_fit = model.fit(train_dataset,
                      steps_per_epoch = 3,
                      epochs = 15,
                      validation_data = validation_dataset)

"""Testing"""

dir_path = '/content/drive/MyDrive/Dataset/Testing '

for i in os.listdir(dir_path ):
  img = image.load_img(dir_path+'//'+ i, target_size=(200,200))
  plt.imshow(img)
  plt.axis('off')
  plt. show()

  X = image.img_to_array(img)
  X = np. expand_dims(X,axis =0)
  images = np.vstack([X])
  val = model.predict (images)
  if val == 0:
    print("Fake Sneakers")
  else:
    print ("Authentic Sneakers")