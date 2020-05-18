#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 23:21:57 2020

@author: jaga
"""

import numpy as np
import matplotlib.pyplot as plt
import timeit

''' Empty lists to store the time taken for calculating DFT
                           using FFT and not using it'''
time_without_FFT = []
time_with_FFT =[]

n_min = 4
n_max = 200
n_diff = 5

for n in range(n_min, n_max + n_diff, n_diff):
    #  computing DFT without using FFT
    points = np.arange(n) ** 2
    dx = 1
    p = np.arange(n)
    x_p = p * dx  # Space Samples
    k_q = 2 * np.pi * p / (n * dx)  # Freq Samples
    
    starttime = timeit.default_timer()
    
    dft = []
    for i in range(n):
        sum = 0
        for j in range(n):
            sum = sum + points[j] * np.exp(-1j * k_q[i] * x_p[j])
        dft.append(sum)
   
    time_without_FFT.append( timeit.default_timer() - starttime)
   
    #  computing DFT by numpy.fft.fft i.e using FFT
    starttime = timeit.default_timer()
    
    dft = np.fft.fft(points , norm = 'ortho')
    time_with_FFT.append( timeit.default_timer() - starttime)

n = np.arange(n_min , n_max + n_diff , n_diff)
plt.plot(n , time_without_FFT , label = 'DFT without using FFT')
plt.plot(n , time_with_FFT , LABEL = 'DFT using numpy.fft' )

plt.xlabel('No of Sample Points (n)')
plt.ylabel('Time Complexity')
plt.title('Time Complexity for DFT  Vs No. of Sample Points')
plt.legend()

 