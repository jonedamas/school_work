def skudd_aar(year):
    if year % 4 == 0:
        if year % 100:
            if year % 400:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

