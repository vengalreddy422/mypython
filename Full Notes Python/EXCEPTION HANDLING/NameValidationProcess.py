#NameValidationProcess.py<--File Name and Mdule Name
from NameValidationExcept import SpaceError, ZeroLengthError, InvalidNameError
def validate(name):
    if(name.isspace()):
        raise SpaceError
    else:
        words=name.split()
        if(len(words)==0):
            raise ZeroLengthError
        else:
            res=True
            for word in words:
                if(not word.isalpha()):
                    res=False
                    break
            if(res):
                return name
            else:
                raise InvalidNameError
