#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 23:21:19 2020

@author: jaga
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    if x == 0:
        return 1
    else:
        return np.sin(x)/x
x_min = -100
x_max = 100
sampl_pts = 2048
sampl_rate = ( x_max - x_min )/(sampl_pts - 1)
space_sampl = np.arange(x_min , x_max + sampl_rate , sampl_rate , dtype = 'float')

# list for storing the function
sin = []
for i in range(sampl_pts):
    sin.append(f(space_sampl[i]))

# k values for ploting
freq_sampl = 2 * np.pi * np.fft.fftfreq( sampl_pts , d = sampl_rate )   
factor = sampl_rate * np.sqrt(0.5 * sampl_pts / np.pi) * np.exp(-1j * freq_sampl * x_min)

ft_sin = factor * np.fft.fft(np.array(sin) , norm = 'ortho')

plt.plot( freq_sampl , ft_sin.real ,label = 'Real Part (Using DFT)' , marker = '.')
plt.plot( freq_sampl , ft_sin.imag ,label = 'Imaginary Part (Using DFT)')

def anal_sol(k):
    if abs(k) <= 1:
        return np.sqrt(np.pi / 2)
    else:
        return 0
# Plotting the analytic solution
anal_soln = []
for i in range(sampl_pts):
    anal_soln.append(anal_sol(freq_sampl[i]))
plt.plot( freq_sampl , anal_soln , label = 'Analytic FT' , ls = ':', color = 'red' )

plt.title( 'Fourier Transform of sinc Function' , fontsize = 15 , color = 'red')
plt.xlabel('k', fontsize = 13 , color = 'red')
plt.ylabel('ft(k)', fontsize = 13 , color = 'red')
plt.ylim(0,2)
plt.xlim(-3,3)
plt.legend()

