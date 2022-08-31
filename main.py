def func_sqrt(number):
    num = number ** 0.5
    num_string = str(num)
    if f"{int(num)}.0" in num_string:
        return int(num)
    return None
