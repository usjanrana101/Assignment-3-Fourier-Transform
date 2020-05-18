#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 23:23:16 2020

@author: jaga
"""

import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection="3d")

def f(x , y):
    return np.exp(- (x*x + y*y))

x_min = -5
x_max = 5
y_min = -5
y_max = 5
sampl_pts = 256
sampl_rate_x = ( x_max - x_min )/(sampl_pts - 1)
sampl_rate_y = ( y_max - y_min )/(sampl_pts - 1)
space_sampl_x = np.arange(x_min , x_max + sampl_rate_x , sampl_rate_x , dtype = 'float')
space_sampl_y = np.arange(x_min , x_max + sampl_rate_y , sampl_rate_y , dtype = 'float')

# forming the real space data points using np.meshgrid()
x_arr , y_arr = np.meshgrid(space_sampl_x ,space_sampl_y)

freq_sampl_x = 2 * np.pi * np.fft.fftfreq( sampl_pts , d = sampl_rate_x ) 
freq_sampl_y = 2 * np.pi * np.fft.fftfreq( sampl_pts , d = sampl_rate_y ) 

# forming the freqency space data points using np.meshgrid()
kx_arr , ky_arr = np.meshgrid(freq_sampl_x ,freq_sampl_y)
  
factor_x = sampl_rate_x * np.sqrt(0.5 * sampl_pts / np.pi) * np.exp(-1j * freq_sampl_x * x_min)
factor_y = sampl_rate_y * np.sqrt(0.5 * sampl_pts / np.pi) * np.exp(-1j * freq_sampl_y * y_min)

#  fourier trans  = factor * 2D DFT
FT = factor_x * factor_y * np.fft.fft2( f(x_arr , y_arr) , norm = 'ortho')

def anal_sol(x , y):
    return 0.5 * np.exp(- (x*x + y*y)/4.0) 
# Plotting the analytic solution
ax.plot_wireframe(kx_arr , ky_arr , FT , color='red',label="Numerical solution")
ax.plot_wireframe(kx_arr , ky_arr , anal_sol( kx_arr , ky_arr ) , color='green',label="Analytic solution")
ax.set_xlabel('kx',fontsize=15)
ax.set_ylabel('ky',fontsize=15)
ax.set_zlabel('ƒ(kx,ky)',fontsize=15)
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
plt.title('Fourier Transform of 2D Gaussian',fontsize=15)
plt.legend()
plt.show()
