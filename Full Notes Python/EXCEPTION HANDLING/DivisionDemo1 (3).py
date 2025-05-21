#Division.py<-----File Name and Module Name
from DivExcept import ZeroError
def divop(a,b):
    if(b==0):
        raise ZeroError # raise used to Hit the exception as part of Function Body
    else:
        return(a/b)

#Phase-2: Hitting the Exceptions