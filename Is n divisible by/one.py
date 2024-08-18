def is_divisible(n,*args):
    for i in args:
        if n % i != 0 or i == 0:
            return False
    return True


# arr = []
# print(help(arr))
