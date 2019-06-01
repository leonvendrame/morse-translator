#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

morse_base = {
    'A' : "101110", 'B' : "1110101010", 'C' : "111010111010",
    'D' : "11101010", 'E' : "10", 'F' : "1010111010",
    'G' : "1110111010", 'H' : "10101010", 'I' : "1010",
    'J' : "10111011101110", 'K' : "1110101110", 'L' : "1011101010",
    'M' : "11101110", 'N' : "111010", 'O' : "111011101110",
    'P' : "101110111010", 'Q' : "11101110101110", 'R' : "10111010",
    'S' : "101010", 'T' : "1110", 'U' : "10101110", 'V' : "1010101110",
    'W' : "1011101110", 'X' : "111010101110", 'Y' : "11101011101110",
    'Z' : "111011101010",
    '0' : "11101110111011101110", '1' : "101110111011101110",
    '2' : "1010111011101110", '3' : "10101011101110",
    '4' : "101010101110", '5' : "1010101010", '6' : "111010101010",
    '7' : "11101110101010", '8' : "1110111011101010",
    '9' : "111011101110111010"
}

def write_outputs(file_name, file_extension, write_content):
    if (file_extension == "txt"):
        file_object = open((file_name + ".morse"), "w")
        file_object.write(write_content)
        file_object.close()

        file_object = open((file_name + ".wav"), "w")
        file_object.write(write_content)
        file_object.close()

    elif (file_extension == "morse"):
        print("ALo")
    
    elif (file_extension == "wav"):
        print("ALo")
 
def txt_read(file_name, file_extension, input_read):
    output = ''
    for i in range(len(input_read)):
        if (input_read[i] == ' '):
            output += "0000000"
        elif (i == len(input_read)-1 or input_read[i+1] == ' '):
            output += morse_base[input_read[i]]
        else:
            output += morse_base[input_read[i]] + "000"
    write_outputs(file_name, file_extension, output)

def wav_read(file_name, file_extension, input_read):
    morse_read(file_name, file_extension, input_read)

def morse_read(file_name, file_extension, input_read):
    output = ''
    input_read = input_read.rsplit("0000000")
    for i in range(len(input_read)):
        input_read[i] = input_read[i].rsplit("000") 
    print(input_read)
    for i in range(len(input_read)):
        for j in range(len(input_read[i])):
            output = input_read[i][j].
def main():
    file_name = sys.argv[1].split(".")[0]
    file_extension = sys.argv[1].split(".")[1]
    file_object = open(sys.argv[1], "r")
    input_read = file_object.read()
    file_object.close()

    input_read = input_read.upper().replace('*', '').replace('?', '').replace('!', '') \
                .replace(',', '')

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