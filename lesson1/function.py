def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    result = one + delimiter + two
    return result.upper()

print(get_summ('Learn', 'python'))