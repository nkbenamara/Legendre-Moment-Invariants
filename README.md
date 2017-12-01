## Legendre-Moment-Invariants

python code for image processing

approximated LMI calculation using zeroth-order approximation (ZOA) 

### Install Dependecies

#### Python3

```
pip install numpy
pip install cv2
```
### Calculate LMI
import on your code the lmi function
```
from legendre_moment_invariants import LegendreMomentInvariants
```
input your image and (n,m) decomposition degrees
```
L=LegendreMomentInvariants(image,m,n)
```
