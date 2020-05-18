#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 23:22:11 2020

@author: jaga
"""

import numpy as np
import matplotlib.pyplot as plt

''' Here the constant function is f(x)= 1 , -5 <= x <= 5
                                      = 0 , elsewhere '''
constant = 1
def f(x):
    if abs(x) <= 5:
        return constant
    else:
        return 0
x_min = -100
x_max = 100
sampl_pts = 256
sampl_rate = ( x_max - x_min )/(sampl_pts - 1)
space_sampl = np.arange(x_min , x_max + sampl_rate , sampl_rate , dtype = 'float')

# list for storind the functional values
const = []
for i in range(sampl_pts):
    const.append(f(space_sampl[i]))

freq_sampl = 2 * np.pi * np.fft.fftfreq( sampl_pts , d = sampl_rate )   
factor = sampl_rate * np.sqrt(0.5 * sampl_pts / np.pi) * np.exp(-1j * freq_sampl * x_min)
ft_sin = factor * np.fft.fft(np.array(const) , norm = 'ortho')

plt.plot( freq_sampl , ft_sin.real ,label = 'Real' , marker = '.')
plt.plot( freq_sampl , ft_sin.imag ,label = 'Imaginary')
plt.title( 'Fourier Transform of Constant Function' , fontsize = 15 , color = 'red')
plt.xlabel('k', fontsize = 13 , color = 'red')
plt.ylabel('ft(k)', fontsize = 13 , color = 'red')
plt.legend()