def upper_decor(fun):
    def hai():
        res=fun()
        return res.upper()
    return hai
@upper_decor
def hello():
    return 'hai'
print(hello())