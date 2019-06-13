#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import wave_samples
from file_handlers import write_outputs
from constants import MORSE_BASE

def txt_read(file_name, file_extension, input_read):
    morse_output = ''
    for i in range(len(input_read)):
        if (input_read[i] == ' ' or input_read[i] == '\n'):
            morse_output += "0000000"
        elif ((i == (len(input_read)-1)) or (input_read[i+1] == ' ')):
            morse_output += MORSE_BASE[input_read[i]]
        else:
            morse_output += MORSE_BASE[input_read[i]] + "000"
    
    sound_output = []
    for i in morse_output:
        if i == "1":
            sound_output += wave_samples()
        else:
            for i in range(0, 12000):
                sound_output.append(0)

    write_outputs(file_name, file_extension, [morse_output, sound_output])

def wav_read(file_name, file_extension, input_read):
    morse_read(file_name, file_extension, input_read)

def morse_read(file_name, file_extension, input_read):
    sound_output = []
    for i in morse_output:
        if i == "1":
            sound_output += wave_samples()
        else:
            for i in range(0, 12000):
                sound_output.append(0)
    
    output = ''
    input_read = input_read.split("0000000")
    for i in range(len(input_read)):
        input_read[i] = input_read[i].split("000") 
    # print(input_read)
    for i in range(len(input_read)):
        for j in range(len(input_read[i])):
            for k in MORSE_BASE.keys():
                if (input_read[i][j] == MORSE_BASE[k]):
                    output += k
        output += ' '
    # print(output)
    write_outputs(file_name, file_extension, output)

def morse_to_txt():
    None

def txt_to_morse():
    None

def morse_to_wave():
    None

def wave_to_morse():
    None