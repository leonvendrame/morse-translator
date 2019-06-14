#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from constants import FREQUENCY, SAMPLING_RATE, NUM_SAMPLES

def wave_samples():
    return [np.sin(2 * np.pi * FREQUENCY * x / SAMPLING_RATE) for x in range(NUM_SAMPLES)]
