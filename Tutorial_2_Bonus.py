# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 02:39:48 2018

@author: Tankiso
"""

from numpy import concatenate,exp,pi,arange,complex

def myfft(vec):
    n=vec.size
    if n==1:
        return vec
    Even=vec[0::2]
    Odd=vec[1::2]

    t=n/2;
    i=complex(0,1)    
    twid=exp(-2*pi*i*arange(0,t)/n) #phase factors
    Evenft=myfft(Even)
    Oddft=myfft(Odd)

    Answer=concatenate((Evenft+twid*Oddft,Evenft-twid*Oddft))#partials combined with phase factors
    return Answer

def myfft3(vec):
    n=vec.size
    if n==1:
        return vec
    mya=vec[0::3]
    myb=vec[1::3]
    myc=vec[2::3]
    i=complex(0,1)
    t=n/3
    twid1=exp(-2*pi*i*arange(0,t)/n)
    twid2=exp(-4*pi*i*arange(0,t)/n)

    f1=exp(-2*pi*i/3) 
    f2=exp(-4*pi*i/3)
    f1b=f2;          
    f2b=f1; 

    aft=myfft3(mya)
    bft=myfft3(myb)*twid1
    cft=myfft3(myc)*twid2
    
    ft1=aft+bft+cft
    ft2=aft+bft*f1+cft*f2
    ft3=aft+bft*f1b+cft*f2b
    
    ft=concatenate((ft1,ft2,ft3))

    return ft