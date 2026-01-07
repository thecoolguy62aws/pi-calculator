def isNum(s):
    try:
        s = int(s)
        if s >= 2 and s <= 1500: return True
        else: return False
    except ValueError:
        return False