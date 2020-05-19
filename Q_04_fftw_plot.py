#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 23:29:30 2020

@author: jaga
"""

import numpy as np
import matplotlib.pyplot as plt

''' actually this is importing the file, where the data of FT of this function
        is stored by running the c code using fftw3 library .
         Now we can plot this to check with the numpy.fft.fft'''
file =  "/home/jaga/Desktop/com_phy_assgts/assgt3/Q_04_import_data.txt" 
freq , FT_real , FT_imag = np.loadtxt(file, usecols = (0,1,2) ,unpack = "true")
plt.plot( freq , FT_real ,label = 'Real Part (Using fftw3)' , marker = '*', color = 'black')
plt.plot( freq , FT_imag ,label = 'Imaginary Part (Using fftw3)')

# FT using numpy
def f(x):
    return np.exp(-x*x)
x_min = -15
x_max = 15
sampl_pts = 256
sampl_rate = ( x_max - x_min )/(sampl_pts - 1)
space_sampl = np.arange(x_min , x_max + sampl_rate , sampl_rate , dtype = 'float')

sin = []
for i in range(sampl_pts):
    sin.append(f(space_sampl[i]))

freq_sampl = 2 * np.pi * np.fft.fftfreq( sampl_pts , d = sampl_rate )   
factor = sampl_rate * np.sqrt(0.5 * sampl_pts / np.pi) * np.exp(-1j * freq_sampl * x_min)
ft_sin = factor * np.fft.fft(np.array(sin) , norm = 'ortho')

plt.plot( freq_sampl , ft_sin.real ,label = 'Real Part (Using DFT)' )
plt.plot( freq_sampl , ft_sin.imag ,label = 'Imaginary Part (Using DFT)')

def anal_sol(x):
    return np.exp(-x*x/4)/np.sqrt(2) 
# Plotting the analytic solution
anal_soln = []
for i in range(sampl_pts):
    anal_soln.append(anal_sol(freq_sampl[i]))
plt.plot( freq_sampl , anal_soln , label = 'Analytic FT' , ls = ':', color = 'red' )

plt.title( 'Fourier Transform of Gaussian' , fontsize = 15 , color = 'red')
plt.xlabel('k', fontsize = 13 , color = 'red')
plt.ylabel('ft(k)', fontsize = 13 , color = 'red')
plt.xlim(-10,10)
plt.ylim(0,1.25)
plt.legend()

