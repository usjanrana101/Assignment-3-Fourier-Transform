#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <fftw3.h>
// Fourier transform using fftw3 lib

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
	
	fftw_complex space_sampl[sampl_pts] , freq_sampl[sampl_pts] ;
	fftw_plan plan ;

	// constructing the array of space sample and also k values
	x = x_min ;
	i = 0 ;
	while (x <= x_max)
	{
		x_arr[i] = x ;
		// real and imaginary part of the fftw_complex structure
		space_sampl[i][0] = fun(x) ; 
		space_sampl[i][1] = 0 ;
		if (i<=sampl_pts/2)
			k_arr[i] = (2 * M_PI)*(i/(sampl_pts * sampl_rate)) ;
		else
			k_arr[i] = - (2 * M_PI)*(sampl_pts - i)/(sampl_pts * sampl_rate) ;
		
		i = i + 1 ;
		x = x + sampl_rate ;

	} 
	//  defining and executing the plan for calculating dft 
	plan = fftw_plan_dft_1d(sampl_pts, space_sampl, freq_sampl ,FFTW_FORWARD, FFTW_ESTIMATE);
	fftw_execute(plan); // store the DFT of space_sampl array to freq_sampl array

// printing frequency , real part of FT , complex part of FT column by column

	for (int i = 0; i < sampl_pts; i++)
	{
		printf("%lf %lf %lf \n", k_arr[i] 
			   ,sampl_rate * sqrt(1.0 / (2 * M_PI)) * (cos(k_arr[i] *x_min) * freq_sampl[i][0] + sin(k_arr[i] * x_min) * freq_sampl[i][1]),
			     sampl_rate * sqrt(1.0 / (2 * M_PI)) * (cos(k_arr[i] *x_min) * freq_sampl[i][1] - sin(k_arr[i] * x_min) * freq_sampl[i][0]) 
			     );                          

	}
	
	fftw_destroy_plan(plan) ;
	return 0;
}
