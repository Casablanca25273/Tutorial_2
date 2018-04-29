# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 01:27:02 2018

@author: Tankiso
"""
from numpy.fft import fft,ifft
import numpy as np
import pylab

#1&2
def Shifted(x,n=0):  
    vec=0*x         #make a vector of zeros the same length as the input vector
    vec[n]=1
    vecft=fft(vec)
    xft=fft(x)
    return np.real(ifft(xft*vecft))
    
def Gaussian(x):
    sigma=2
    y=np.exp(-0.5*x**2/sigma**2)     
    return y
    
if __name__=='__main__':

    x=np.arange(-30,30,0.1)
    y=Gaussian(x)

    yshift=Shifted(y,100)
    pylab.plot(x,y)
    pylab.plot(x,yshift)
    pylab.show()
    
#3
def Correlate(x,y):         
    assert(x.size==y.size) # the vectors of the same size
    fta = fft(x)
    ftb = fft(y)
    ftbconj=np.conj(ftb)
    return np.real(ifft(fta*ftbconj))

def Gaussian(x):
    sigma=2
    y=np.exp(-0.5*x**2/sigma**2)
    return y
    
if __name__=='__main__':

    x=np.arange(-30,30,0.1)
    y=Gaussian(x)

    ycorr=Correlate(y,y)
    pylab.plot(x,ycorr,'k')
    pylab.show()
  
    ycorr=Correlate(y,y)
    yshift=Shifted(y,y.size/4)
    yshiftcorr=Correlate(yshift,yshift)
    MeanError=np.mean(np.abs(ycorr-yshiftcorr))
    print 'Mean difference between two correlation functions = ' + repr(MeanError)
    pylab.plot(x,ycorr)
    pylab.plot(x,yshiftcorr,'b')        
    pylab.show()  
    
#4    
def Convolve(x,y):          
    assert(x.size==y.size) 
    xx=np.zeros(2*x.size)
    xx[0:x.size]=x

    yy=np.zeros(2*y.size)
    yy[0:y.size]=y
    xxft=fft(xx)
    yyft=fft(yy)
    vec=np.real(ifft(xxft*yyft))
    return vec[0:x.size]

y=y/y.sum()
yconv=Convolve(y,y)
pylab.plot(x,y)
pylab.plot(x,yconv)
pylab.show()



    
       
  

   
    