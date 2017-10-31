import data

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM

model = Sequential()
model.add(Embedding(None, 2, input_length=1))
model.add(LSTM(128))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# model.fit(x_train, y_train, batch_size=16, epochs=10)
# score = model.evaluate(x_test, y_test, batch_size=16)

# # define model
# model = Sequential()
# model.add(Dense(128, activation='relu', input_shape=(9,)))
# # model.add(Dropout(0.5))
# model.add(Dense(64, activation='relu'))
# # model.add(Dropout(0.5))
# model.add(Dense(1,  activation='sigmoid'))
#
# # compile
# sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
# model.compile(optimizer=sgd,
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])

# data
(x_train, y_train), (x_test, y_test) = data.load_data()

model.fit(x_train, y_train, epochs=1000, batch_size=10)

score = model.evaluate(x_test, y_test, batch_size=10)

print("\n", score)
