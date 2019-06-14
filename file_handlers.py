#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wave
import struct
import re
import numpy as np
from constants import SAMPLING_RATE, AMPLITUDE, NUM_SAMPLES

def read_file(app_arguments):   
    file_name = app_arguments[1].split(".")[0]
    file_extension = app_arguments[1].split(".")[1]
    
    if file_extension == "wav":
        return read_wav_file(file_name, file_extension)

    try: 
        file_object = open(app_arguments[1], "r")
    
    except:
        print("Erro ao abrir arquivo: Verifique se o arquivo existe e tente novamente.")
        exit()
    
    input_read = file_object.read()
    file_object.close()
    
    input_read = re.sub(r'[^a-zA-Z|0-9|\s|\n]', '', input_read)
    input_read = input_read.upper()
    
    return file_name, file_extension, input_read

def read_wav_file(file_name, file_extension):
    with wave.open(file_name + ".wav", "r") as wav_file:
        num_frames = wav_file.getnframes()
        input_read = wav_file.readframes(num_frames)
        input_read = struct.unpack('{n_f}h' .format(n_f = num_frames), input_read)
        input_read = np.array(input_read)

    return file_name, file_extension, input_read
    

def write_wav(sound_output, file_name):
    with wave.open(file_name + ".wav", 'w') as wave_file:
        wave_file.setparams((1, 2, SAMPLING_RATE, NUM_SAMPLES, "NONE", "not compressed"))

        for s in sound_output:
            wave_file.writeframes(struct.pack('h', int(s * AMPLITUDE)))

def write_morse(morse_output, file_name):
    file_object = open((file_name + ".morse"), "w")
    file_object.write(morse_output)
    file_object.close()

def write_txt(txt_output, file_name):
    file_object = open((file_name + ".txt"), "w")
    file_object.write(txt_output)
    file_object.close()    

def write_output(file_name, file_extension, write_content):
    if (file_extension == "txt"):
        write_morse(write_content[0], file_name)
        write_wav(write_content[1], file_name)

    elif (file_extension == "morse"):
        write_txt(write_content[0], file_name)
        write_wav(write_content[1], file_name)

    elif (file_extension == "wav"):
        write_txt(write_content[0], file_name)
        write_morse(write_content[1], file_name)
    
