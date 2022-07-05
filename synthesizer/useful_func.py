def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        pass