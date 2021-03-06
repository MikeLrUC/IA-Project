# Based on https://github.com/EckoTan0804/flying-guide-dog/blob/main/models/traffic_light_classification/simple_cnn.py

import loader
from tensorflow import random
from tensorflow.keras import models, layers, losses, optimizers
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier

input_size = (224, 224, 3)

def flying_dogs_cnn():
    def flying_dogs_model():
        model = models.Sequential()
        
        model.add(layers.Conv2D(6, (3, 3), activation='relu', input_shape=input_size))
        model.add(layers.Conv2D(16, (3, 3), activation='relu'))
        model.add(layers.AveragePooling2D())
        model.add(layers.Conv2D(16, (3, 3), activation='relu'))
        model.add(layers.AveragePooling2D())
        model.add(layers.Conv2D(16, (3, 3), activation='relu'))
        model.add(layers.AveragePooling2D())
        model.add(layers.Conv2D(16, (3, 3), activation='relu'))
        model.add(layers.AveragePooling2D())
        
        model.add(layers.Flatten())
        model.add(layers.Dense(1024, activation='relu'))
        model.add(layers.Dropout(0.25))
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dropout(0.25))
        model.add(layers.Dense(5, activation='relu'))
        model.add(layers.Dropout(0.25))

        model.compile(loss=losses.mean_squared_error, optimizer=optimizers.Adam(), metrics=['accuracy'])
        return model

    return KerasClassifier(flying_dogs_model)

def main(epochs):
    '''Flying Dogs'''
    # Loading Data
    X_train, y_train, X_val, y_val = loader.main()

    # Classify
    cnn = flying_dogs_cnn()
    cnn.fit(X_train, y_train, epochs=epochs)
    return cnn.score(X_train, y_train), cnn.score(X_val, y_val)

if __name__ == "__main__":
    random.set_seed(42)
    main(25)


