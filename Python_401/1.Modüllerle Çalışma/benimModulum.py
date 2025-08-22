# -*- coding: utf-8 -*-

from math import pi

def topla(a,b):
    return a+b

def daireCevreHesapla(r):
    return 2 * pi * r

def daireAlanHesapla(r):
    """
    Parameters
    ----------
    r : dairenin yarı çapı
    
    Returns
    -------
    Dairenin alanının değerini döndürür.
    """
    return pi * r * r


#import hesap

if __name__ == '__main__':
    print(topla(75, 345))
print(__name__)