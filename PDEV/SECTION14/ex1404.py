def extra(fun):
    
    def carpma(a,b):
        print(a,b)
    
    return carpma

@extra
def toplama(a,b):
    return a + b

print(toplama(5,9))