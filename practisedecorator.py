
def upper_decor(hi):
    def wrapping():
        res=hi()
        return res.upper()
    return wrapping

@upper_decor
def hello():
    return 'mohammed shamil rafeequr'
print(hello())