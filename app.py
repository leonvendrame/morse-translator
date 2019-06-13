#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import wave
import numpy as np
import re
import struct

NUM_SAMPLES = 12000
SAMPLING_RATE = 48000
FREQUENCY = 440

morse_base = {
    'A' : "10111", 'B' : "111010101", 'C' : "11101011101",
    'D' : "1110101", 'E' : "1", 'F' : "101011101",
    'G' : "111011101", 'H' : "1010101", 'I' : "101",
    'J' : "1011101110111", 'K' : "111010111", 'L' : "101110101",
    'M' : "1110111", 'N' : "11101", 'O' : "11101110111",
    'P' : "10111011101", 'Q' : "1110111010111", 'R' : "1011101",
    'S' : "10101", 'T' : "111", 'U' : "1010111", 'V' : "101010111",
    'W' : "101110111", 'X' : "11101010111", 'Y' : "1110101110111",
    'Z' : "11101110101",
    '0' : "1110111011101110111", '1' : "10111011101110111",
    '2' : "101011101110111", '3' : "1010101110111",
    '4' : "10101010111", '5' : "101010101", '6' : "11101010101",
    '7' : "1110111010101", '8' : "111011101110101",
    '9' : "11101110111011101"
}

def write_outputs(file_name, file_extension, write_content):
    if (file_extension == "txt"):
        file_object = open((file_name + ".morse"), "w")
        file_object.write(write_content[0])
        file_object.close()

        wav_writer(write_content[1], file_name)

    elif (file_extension == "morse"):
        file_object = open((file_name + ".txt"), "w")
        file_object.write(write_content)
        file_object.close()

        file_object = open((file_name + ".wav"), "w")
        file_object.write(write_content)
        file_object.close()
    
    elif (file_extension == "wav"):
        print("ALo")
 
def txt_read(file_name, file_extension, input_read):
    morse_output = ''
    for i in range(len(input_read)):
        if (input_read[i] == ' ' or input_read[i] == '\n'):
            morse_output += "0000000"
        elif (i == len(input_read)-1 or input_read[i+1] == ' '):
            morse_output += morse_base[input_read[i]]
        else:
            morse_output += morse_base[input_read[i]] + "000"
    
    sound_output = []
    for i in morse_output:
        if i == "1":
            sound_output += wave_samples()
        else:
            for i in range(0, 12000):
                sound_output.append(0)

    write_outputs(file_name, file_extension, [morse_output, sound_output])

def wav_writer(sound_output, file_name):
    with wave.open(file_name + ".wav", 'w') as wave_file:
        wave_file.setparams((1, 2, SAMPLING_RATE, NUM_SAMPLES, "NONE", "not compressed"))

        for s in sound_output:
            wave_file.writeframes(struct.pack('h', int(s * 16000)))

def wav_read(file_name, file_extension, input_read):
    morse_read(file_name, file_extension, input_read)

def morse_read(file_name, file_extension, input_read):
    output = ''
    input_read = input_read.split("0000000")
    for i in range(len(input_read)):
        input_read[i] = input_read[i].split("000") 
    # print(input_read)
    for i in range(len(input_read)):
        for j in range(len(input_read[i])):
            for k in morse_base.keys():
                if (input_read[i][j] == morse_base[k]):
                    output += k
        output += ' '
    # print(output)
    write_outputs(file_name, file_extension, output)

def wave_samples(frequency = 440, sampling_rate = 48000, num_samples = 12000):
    return [np.sin(2 * np.pi * frequency * x / sampling_rate) for x in range(num_samples)]

def file_reader(app_arguments):   
    file_name = app_arguments[1].split(".")[0]
    file_extension = app_arguments[1].split(".")[1]
    try: 
        file_object = open(app_arguments[1], "r")
    except:
        print("Erro ao abrir arquivo, verifique se o arquivo existe e tente novamente.")
        exit()
    input_read = file_object.read()
    file_object.close()
    
    input_read = re.sub(r'[^a-zA-Z|0-9|\s|\n]', '', input_read)
    input_read = input_read.upper()
    
    return file_name, file_extension, input_read

def main():
    file_name, file_extension, input_read = file_reader(sys.argv)

    if (file_extension == "txt"):
        txt_read(file_name, file_extension, input_read)
    elif (file_extension == "morse"):
        morse_read(file_name, file_extension, input_read)
    elif (file_extension == "wav"):
        wav_read(file_name, file_extension, input_read)
    else:
        print("Tipo de arquivo não reconhecido, tente novamente.")
    

if __name__ == "__main__":
    main()