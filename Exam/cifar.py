import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Завантаження датасету CIFAR100
(x_train, y_train), (x_test, y_test) = keras.datasets.cifar100.load_data()

# Нормалізація даних
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

model = keras.Sequential(
    [
        layers.Conv2D(32, (3, 3), activation="relu", input_shape=(32, 32, 3)),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, (3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(128, (3, 3), activation="relu"),
        layers.Flatten(),
        layers.Dense(256, activation="relu"),
        layers.Dense(100),
    ]
)

# Компіляція та навчання моделі
model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001),
              loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=[keras.metrics.SparseCategoricalAccuracy()])
model.fit(x_train, y_train, epochs=448, batch_size=144, validation_data=(x_test, y_test))