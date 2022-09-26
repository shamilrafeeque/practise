from unittest import result


def upper_decor(fun):
    def wrapper():
        result=fun()
        # return result.upper()
        
        return result+'jai'
    return wrapper 

@upper_decor
def display():
    return 'hai'
print(display())
