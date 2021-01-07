import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
import matplotlib.pyplot as plt
import numpy as np
import  pandas as pd

from CSVHandler import CSVHandler

"""Creating data
"""
def create_real_data():
    global  x_train, y_train, x_test, y_test
    csv = CSVHandler()
    x_train, y_train = csv.create_data_from_csv('train_selected_china.csv')
    x_test, y_test = csv.create_data_from_csv('test_selected_china.csv')
    x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
    input_shape = (28, 28, 1)
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255

"""Model
"""
create_real_data()
input_shape = (28, 28, 1)
model2 = tf.keras.Sequential()
model2.add(Conv2D(28, kernel_size=(3, 3), input_shape=input_shape))
model2.add(MaxPooling2D(pool_size=(2, 2)))
model2.add(Flatten())
model2.add(Dense(256, activation=tf.nn.relu))
model2.add(Dropout(0.2))
model2.add(Dense(100, activation=tf.nn.softmax))

model2.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model2.save("model.h5")

history = model2.fit(x=x_train, y=y_train, validation_split=0.1, epochs=15, batch_size=50)
predictions2 = model2.predict(x_test)
print(np.argmax(predictions2, axis=1))

"""prediction
"""
for i in range(1, 10):
    image = x_test[i]
    image = np.array(image, dtype='float')
    plt.imshow(image.reshape(28, 28), cmap='bone_r')
    plt.xlabel("predicted: " + str(np.argmax(predictions2, axis=1)[i]))
    plt.show()

"""accuracy
"""
plt.plot(history.history['acc'])
plt.ylabel('accuracy')
plt.xlabel('epochs')
plt.show()

"""evaluation
"""
model2.evaluate(x_test, y_test)