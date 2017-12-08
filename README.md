## Legendre-Moment-Invariants

python code for image processing

approximated LMI calculation using zeroth-order approximation (ZOA) 

### Install Dependecies

#### Python3

```
pip install numpy
```
### Calculate LMI
import on your code the lmi function
```
from legendre_moment_invariants import LegendreMomentInvariants
import numpy as np
```
input your image and (n,m) decomposition degrees
```
L=LegendreMomentInvariants(image,m,n)
```
