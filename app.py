#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
from converters import *
from file_handlers import read_file
from constants import FREQUENCY, SAMPLING_RATE, NUM_SAMPLES

def wave_samples():
    return [np.sin(2 * np.pi * FREQUENCY * x / SAMPLING_RATE) for x in range(NUM_SAMPLES)]

def main():
    file_name, file_extension, input_read = read_file(sys.argv)

    if (file_extension == "txt"):
        txt_read(file_name, file_extension, input_read)
    elif (file_extension == "morse"):
        morse_read(file_name, file_extension, input_read)
    elif (file_extension == "wav"):
        wav_read(file_name, file_extension, input_read)
    else:
        print("Erro ao abrir o arquivo: Tipo de arquivo não reconhecido, tente novamente.")
        exit()
    

if __name__ == "__main__":
    main()