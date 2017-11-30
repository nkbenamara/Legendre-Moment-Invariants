import cv2 as cv
import numpy as np
from math import factorial,pow

## Computing Pm(x) or Pn(y) ##
def PolyLMI(d,v):
    P=[]
    for k in range(0,d+1):
       if (d-k)%2==0:
        a=pow(-1,(d-k)/2)*(1/pow(2,d))*factorial(d+k)/(factorial((d-k)/2)*factorial((d+k)/2)*factorial(k))
        p = a * pow(v, k)
        P.append(p)
       else:
        a=0
    P=sum(P)
    return P

## Computing L_mn ##
def LegendreMomentInvariants(image,m,n):
    LMI_moment=[]
    M,N=np.shape(image)
    d=(M-1)*(N-1)
    for s in range(0,m+1):
        for t in range(0,n+1):
            norm = ((2 * s + 1) * (2 * t + 1)) /d
            L=0
            for i in range(0,M):
                for j in range(0,N):
                    xi = (2 * i - M - 1) / (M - 1)
                    yi = (2 * j - N - 1) / (N - 1)
                    T= image[i][j]*PolyLMI(s,xi)*PolyLMI(t,yi)
                    L=L+T
            L=norm*L
            LMI_moment.append(L)
    return LMI_moment


