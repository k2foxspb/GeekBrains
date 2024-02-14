from functools import wraps


def simple_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        nonlocal cache
        key = str(*args)
        if key not in cache:
            cache[key] = func(*args)
        return cache[key]

    return wrapper


def logger(func):
    def wrapper(*args):
        result = func(*args)
        print(f'\tcall {func.__name__}({", ".join(map(str, args))})')
        return result

    return wrapper


@logger
@simple_cache
def render_input(field):
    return f'<input id="id_{field}" type="text" name="{field}">'


username_f = render_input('username')


