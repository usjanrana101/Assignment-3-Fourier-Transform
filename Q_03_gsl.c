#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include<gsl/gsl_fft_complex.h>
// Fourier transform using gsl lib.

float fun( float x) // defined the given function
{
	if (x == 0)
			return 1 ;
		else
			return sin(x)/x ;
}


int main()
{
	int sampl_pts = 2048, i ;
	double x , x_max = 100, x_min = -100 , sampl_rate = (x_max - x_min)/(sampl_pts - 1) ;

	// defining array to store the x_values  and frequencies
	double x_arr[sampl_pts] ,  k_arr[sampl_pts]; 
	double space_sampl[2 * sampl_pts] ;

	// constructing the array of space sample and also k values
	x = x_min ;
	i = 0 ;
	while (x <= x_max)
	{
		x_arr[i] = x ;
		// we need a array of 2n elements with real values at even position and 
		//imaginary values at odd position for calculating dft using gsl fuction 
		space_sampl[2 * i] = fun(x) ; 
		space_sampl[2 * i + 1] = 0 ;

		if (i<=sampl_pts/2)
			k_arr[i] = (2 * M_PI)*(i/(sampl_pts * sampl_rate)) ;
		else
			k_arr[i] = - (2 * M_PI)*(sampl_pts - i)/(sampl_pts * sampl_rate) ;
		
		i = i + 1 ;
		x = x + sampl_rate ;

	} 

	gsl_complex_packed_array data = space_sampl;
	gsl_fft_complex_radix2_forward (space_sampl, 1, sampl_pts);

	// printing frequency , real part of FT , complex part of FT column by column

	for (int i = 0; i < sampl_pts; i++)
	{
		printf("%lf %lf %lf \n", k_arr[i] 
			   ,sampl_rate * sqrt(1.0 / (2 * M_PI)) * (cos(k_arr[i] *x_min) * space_sampl[2 * i] + sin(k_arr[i] * x_min) * space_sampl[2 * i +1]),
			     sampl_rate * sqrt(1.0 / (2 * M_PI)) * (cos(k_arr[i] *x_min) * space_sampl[2 * i +1] - sin(k_arr[i] * x_min) * space_sampl[2 * i]) 
			     );                          

	}

	return 0;
}
