import data
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

# define model
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(9,)))
# model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
# model.add(Dropout(0.5))
model.add(Dense(1,  activation='sigmoid'))

# compile
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(optimizer=sgd,
              loss='binary_crossentropy',
              metrics=['accuracy'])

# data
(x_train, y_train), (x_test, y_test) = data.load_age_data()

model.fit(x_train, y_train, epochs=100, batch_size=64)

score = model.evaluate(x_test, y_test, batch_size=64)

print("\n", score)
