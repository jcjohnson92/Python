def lovefunc( flower1, flower2 ):
    # ...
    if ((flower1 % 2 == 0) and (flower2 % 2 == 1)) or ((flower1 % 2 == 1) and (flower2 % 2 == 0)):
        return True
    return False

print(lovefunc(1,4))
print(lovefunc(2,2))
print(lovefunc(0,1))
print(lovefunc(0,0))