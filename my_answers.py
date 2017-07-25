import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras

import string

# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = []

    for i in range( 0, len(series)-window_size):
        X.append(series[i:i+window_size])
        y.append(series[i+window_size])
        
    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)
   
    
    return X,y
# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    pass

    my_model = Sequential()
    my_model.add(LSTM(input_shape=(window_size,1), units=5))
    my_model.add(Dense(units=1))

    return my_model

### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    punctuation = ['!', ',', '.', ':', ';', '?']
    
    allowed = punctuation + [l for l in string.ascii_lowercase] + [' ']
    summary = {}
    
    for c in text:
        if summary.get(c,None) is not None: 
            summary[c] +=1
        else:
            summary[c] = 1
    
    for c in summary:
        if not c in allowed:
            print(f"{c}: {summary[c]}")
            text = text.replace(c, '')
    #print(summary)


    return text

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = [ text[i:i+window_size] for i in range(0, len(text)-window_size, step_size)]
    outputs = [ text[i+window_size] for i in range(0, len(text)-window_size, step_size)]


    return inputs,outputs

# TODO build the required RNN model: 
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
    pass
