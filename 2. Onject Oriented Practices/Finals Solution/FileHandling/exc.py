a = int(input('degf'))
try:
    var = 1 / a
    print(var)
except ZeroDivisionError:
    raise ZeroDivisionError('Numvber will aporicag infinity')