# imp imports

    import glob
    import numpy as np
    from PIL import Image
    import matplotlib.pyplot as plt
    from sklearn.utils import shuffle
    from keras.models import Sequential
    from keras.layers import Dense, Dropout, Conv2D, MaxPool2D, Flatten


# divides data into x and y-axis

    train_x = arrimage[:size,:width-1,:height-1,np.newaxis]
    test_x = arrimage[size:,:width-1,:height-1,np.newaxis]
    train_y = labels[:size]
    test_y = labels[size:]train_x = arrimage[:size,:width-1,:height-1,np.newaxis]
    test_x = arrimage[size:,:width-1,:height-1,np.newaxis]
    train_y = labels[:size]
    test_y = labels[size:]


# model to create the layers(Convolution layers)

    def model():
        model = Sequential()
        model.add(Conv2D(50, kernel_size=(3,3), padding='same', activation='relu', input_shape=(126, 126,1)))
        model.add(Conv2D(75, kernel_size=(3,3), padding='same', activation='relu'))
        model.add(MaxPool2D(pool_size=(2,2)))
        model.add(Dropout(0.25))
        model.add(Conv2D(125, kernel_size=(3,3), padding='same', activation='relu'))
        model.add(MaxPool2D(pool_size=(2,2)))
        model.add(Dropout(0.25))
        model.add(Flatten())
        model.add(Dense(500, activation='relu'))
        model.add(Dropout(0.4))
        model.add(Dense(250, activation='relu'))
        model.add(Dropout(0.3))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', metrics=['accuracy'], optimizer='adam')
        return model
        

