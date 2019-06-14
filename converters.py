#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from wave_generator import wave_samples
from file_handlers import write_output
from constants import MORSE_BASE, NUM_SAMPLES

def txt_converter(file_name, file_extension, input_read):
    morse_output = txt_to_morse(input_read)
    wave_output = morse_to_wave(morse_output)
    write_output(file_name, file_extension, [morse_output, wave_output])

def wav_converter(file_name, file_extension, input_read):
    morse_output = wave_to_morse(input_read)
    txt_output = morse_to_txt(morse_output)
    write_output(file_name, file_extension, [txt_output, morse_output])

def morse_converter(file_name, file_extension, input_read):
    txt_output = morse_to_txt(input_read)
    wave_output = morse_to_wave(input_read)
    write_output(file_name, file_extension, [txt_output, wave_output])

def txt_to_morse(input_read):
    morse_output = ''

    for i in range(len(input_read)):
        if (input_read[i] == ' ' or input_read[i] == '\n'):
            morse_output += "0000000"

        elif ((i == (len(input_read)-1)) or (input_read[i+1] == ' ')):
            morse_output += MORSE_BASE[input_read[i]]

        else:
            morse_output += MORSE_BASE[input_read[i]] + "000"
    
    return morse_output

def morse_to_txt(input_read):
    txt_output = ''
    input_read = input_read.split("0000000")

    for i in range(len(input_read)):
        input_read[i] = input_read[i].split("000") 

    for i in range(len(input_read)):
        for j in range(len(input_read[i])):
            for k in MORSE_BASE.keys():
                if (input_read[i][j] == MORSE_BASE[k]):
                    txt_output += k
        if i != (len(input_read)-1):
            txt_output += ' '

    return txt_output

def morse_to_wave(input_read):
    wave_output = []

    for i in input_read:
        if i == "1":
            wave_output += int(i) * wave_samples()

        else:
            for i in range(NUM_SAMPLES):
                wave_output.append(0)
    
    return wave_output

def wave_to_morse(input_read):
    morse_string_len = len(input_read) / NUM_SAMPLES
    input_read = np.array_split(input_read, morse_string_len)
    morse_output = ''

    for i in input_read:
        if i.max() == 0:
            morse_output += '0'
        
        else:
            morse_output += '1'

    return morse_output