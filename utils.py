OPERATIONS = {}
LOOP_CHARS = {}


def register_operation(char):
    """
    Define a decorator which registers brainfuck operation
    functions with function name and given char
    """
    def decorator(func):
        OPERATIONS[char] = func.__name__

        def f(*args, **kwargs):
            return func(*args, **kwargs)
        return f
    return decorator


def register_loop_symbol(symbol_type, symbol):
    """ Register loop symbols to let the interpreter know them """
    def decorator(func):
        LOOP_CHARS[symbol_type] = symbol

        def f(*args, **kwargs):
            return func(*args, **kwargs)
        return f
    return decorator


class UnbalancedLoopCharsError(Exception):
    pass
