#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('.')
import unittest
from converters import txt_to_morse, morse_to_txt

class TestConverters(unittest.TestCase):
    
    def test_morse_to_txt(self):
        TEST_STRING = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        EXPECTED_RETURN = ("1011100011101010100011101011101000111010100010001010111"
            "0100011101110100010101010001010001011101110111000111010111000101110101000"
            "1110111000111010001110111011100010111011101000111011101011100010111010001"
            "0101000111000101011100010101011100010111011100011101010111000111010111011"
            "1000111011101010001110111011101110111000101110111011101110001010111011101"
            "1100010101011101110001010101011100010101010100011101010101000111011101010"
            "100011101110111010100011101110111011101")

        self.assertEqual(txt_to_morse(TEST_STRING), EXPECTED_RETURN, "Passed")

    def test_txt_to_morse(self):
        TEST_STRING = ("1011100011101010100011101011101000111010100010001010111"
            "0100011101110100010101010001010001011101110111000111010111000101110101000"
            "1110111000111010001110111011100010111011101000111011101011100010111010001"
            "0101000111000101011100010101011100010111011100011101010111000111010111011"
            "1000111011101010001110111011101110111000101110111011101110001010111011101"
            "1100010101011101110001010101011100010101010100011101010101000111011101010"
            "100011101110111010100011101110111011101")
        EXPECTED_RETURN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        self.assertEqual(morse_to_txt(TEST_STRING), EXPECTED_RETURN, "Passed")

if __name__ == "__main__":
    unittest.main()