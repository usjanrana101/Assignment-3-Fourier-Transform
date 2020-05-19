#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 23:23:57 2020

@author: jaga
"""

import numpy as np
import matplotlib.pyplot as plt

# extracting data from a text file
file_path = "/home/jaga/Desktop/com_phy_assgts/assgt3/noise.txt"
data = np.loadtxt(file_path , usecols = 0)
n = len(data)
sampl_rate = 1 # it is not given in the problem
plt.plot( data , label = "Data")
 
# DFT of the data 
dft_data = np.fft.fft(data , norm = 'ortho')
plt.plot( dft_data.real , label = "Real part of DFT of this data")
plt.plot( dft_data.imag , label = "Imaginary part of DFT of this data")

# power sprectrum calculation using periodogram
ft_data = sampl_rate * np.sqrt(n / (2 * np.pi)) * dft_data
power_spec = (abs(ft_data) ** 2 )/ n 
plt.plot( power_spec , label = "Power Sprecturm of this data")

# Binned power spectrum for 10 freq bin
bin_unit = (int)(n / 10)
binned_power_spec = np.zeros(10)
for i in range(10):
    
    # averaging between each bin width
    s = 0.0
    for j in range(i * bin_unit , (i+1) * bin_unit , 1):
        s = s + power_spec[(int)(j)]
    binned_power_spec[i] = s / bin_unit
freq = np.arange(0 , n - bin_unit, bin_unit)    
plt.plot(freq , binned_power_spec , label = " Binned Power Sprecturm of this data" , 
                       marker = '*' , color = 'black')
plt.legend()

