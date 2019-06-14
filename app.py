#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from converters import txt_converter, morse_converter, wav_converter
from file_handlers import read_file

def main():
    file_name, file_extension, input_read = read_file(sys.argv)

    if (file_extension == "txt"):
        txt_converter(file_name, file_extension, input_read)
    
    elif (file_extension == "morse"):
        morse_converter(file_name, file_extension, input_read)
    
    elif (file_extension == "wav"):
        wav_converter(file_name, file_extension, input_read)
    
    else:
        print("Erro ao abrir o arquivo: Tipo de arquivo não reconhecido, tente novamente.")
        exit()
    

if __name__ == "__main__":
    main()