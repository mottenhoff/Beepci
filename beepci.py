import winsound

import numpy as np
import pylsl

STREAM_NAME = 'obci'

def connect_to_stream(name):
    inlet = pylsl.resolve_byprop('name', name, timeout=10)[0]
    return pylsl.StreamInlet(inlet)

def read_stream(stream):
    return stream.pull_chunk()[0]

def process_data(data):
    result = np.mean(data)

    print(result, end=' ')

    return result

def control_signal(result):

    if result > 0.5:
        winsound.Beep(frequency := 2000, duration := 1500)

def main():

    stream = connect_to_stream(STREAM_NAME)

    while True:

        data = read_stream(stream)
        
        if data:
            result = process_data(data)
            control_signal(result)


if __name__=='__main__':
    main()