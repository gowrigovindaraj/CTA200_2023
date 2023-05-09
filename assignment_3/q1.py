def iter_method(c):
    z = 0
    for i in range(100):
        z = z*z + c
        if abs(z) > 2:
            return i
    return 100
