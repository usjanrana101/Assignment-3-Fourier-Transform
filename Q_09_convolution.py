#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 23:23:45 2020

@author: jaga
"""

import numpy as np
import matplotlib.pyplot as plt
def f(x):
    if abs(x) <= 1:
        return 1
    else:
        return 0
    
def anal_convo(x): # analytic convolution 
    if abs(x) <= 2:
        return -abs(x) + 2
    else:
        return 0
x_min = -50
x_max = 50
sampl_pts = 2048
sampl_rate = ( x_max - x_min )/(sampl_pts - 1)
space_sampl = np.arange(x_min , x_max + sampl_rate , sampl_rate , dtype = 'float')

# ploting the function and analytic convolution
fn_sampl = []
anal_convo_sampl = []
for i in range(sampl_pts):
    fn_sampl.append(f(space_sampl[i]))
    anal_convo_sampl.append(anal_convo(space_sampl[i]))
plt.plot( space_sampl , fn_sampl ,label = 'f (x)' )
plt.plot( space_sampl , anal_convo_sampl ,label = ' Analytic f o f (x)'  ,color = 'red')

# zero padding is done by doubling the sampling points i.e n = 2 * sampl_pts
dft_f = np.fft.fft(np.array(fn_sampl) , n = 2 * sampl_pts , norm = 'ortho')
freq_sampl = 2 * np.pi * np.fft.fftfreq( 2 * sampl_pts , d = sampl_rate )
factor = np.exp(-1j * freq_sampl * x_min)
mul_dft = (factor * dft_f) * (factor* dft_f) 

# calculating the inverse dft for convolution
dk =freq_sampl[3] -freq_sampl[2]
f_o_f = sampl_rate * np.sqrt(2 * sampl_pts) * np.fft.ifft( mul_dft , norm = 'ortho')

# x_arr is the inverse sample of the of the freq_sampl i.e real space sample
x_arr = 2 * np.pi * np.fft.fftfreq( 2 * sampl_pts , d = dk )


# ploting the numerical convolution
plt.plot( x_arr , f_o_f ,label = 'f o f (x)' , marker = '.' ,color = 'black')
plt.title( 'Convolution of Box Function with itself' , fontsize = 15 , color = 'red')
plt.xlabel('x', fontsize = 13 , color = 'red')
plt.xlim(-3,3)
plt.ylim(0,3)
plt.legend()

