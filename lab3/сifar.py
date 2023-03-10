import numpy as np
from tensorflow import keras
from keras import layers

import matplotlib.pyplot as plt

# Model / data parameters
num_classes = 10
input_shape = (32, 32, 3, 1)

# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()

# Scale images to the [0, 1] range
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
# Make sure images have shape (28, 28, 1)
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)
print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")


# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv3D(32, kernel_size=(3, 3, 3), padding='same', activation="relu"),
        layers.MaxPooling3D(pool_size=(2, 2, 2), padding='same'),
        layers.Conv3D(64, kernel_size=(3, 3, 3), padding='same', activation="relu"),
        layers.MaxPooling3D(pool_size=(2, 2, 2), padding='same'),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ]
)

model.summary()
keras.utils.plot_model(model, "CNN_cifar.png",show_shapes=True)

batch_size = 1024
epochs = 1

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

history=model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)
plt.plot(history.history ['accuracy'])
score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])
