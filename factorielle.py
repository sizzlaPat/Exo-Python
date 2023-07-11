def recursivite(a):
    if(a >1):
        return a * recursivite(a-1)
    else:
        return a

if __name__=='__main__':
    print(recursivite(5))
    