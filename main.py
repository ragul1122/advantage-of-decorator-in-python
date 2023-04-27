def smart_divide(fn):
    def wrapper(*args, **kwargs):
        if args[1] == 0:
            print('I cannot divide with 0 !!!')
            return
        return fn(*args, **kwargs)
    return wrapper

@smart_divide
def divide(a, b):
    return a/b

print(divide(3, 5))   
print(divide(3, 0))   