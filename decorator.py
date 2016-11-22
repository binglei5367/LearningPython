import functools

def log(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call')
            a = func(*args, **kw)
            print('end call')
            return a
        return wrapper

def log2(text):
    if isinstance(text,(str, int, float)):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('begin call: %s()' % func.__name__)
                a = func(*args, **kw)
                print('%s %s():' % (text, func.__name__))
                print('end call: %s()' %func.__name__) 
                return a
            return wrapper
        return decorator
    else:
        func = text
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call: %s()' %func.__name__)
            a = func(*args, **kw)
            print('end call: %s()' %func.__name__)
            return a
        return wrapper


@log2
def puck():
    print('puck not fuck')

puck()
