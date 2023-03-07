def wrap_func(func):
    argnames = func.__code__.co_varnames[:func.__code__.co_argcount]
    fname = func.__name__
    defaults = func.__defaults__
    def inner_func(*args, **kwargs):
        print(dir(func))
        print(argnames)
        print(fname)
        print(args)
        print(kwargs)
        print(defaults)
    return inner_func

@wrap_func
def test_func(a, b=2, c=3, *args, **kwargs):
    pass

test_func(1,2,3,4,5)
