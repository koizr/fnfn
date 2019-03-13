from typing import Callable, TypeVar, Optional

A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')


def flip(f: Callable[[A, B], C]) -> Callable[[B, A], C]:
    """flip arguments"""
    return lambda y, x: f(x, y)


def identity(x: A) -> A:
    return x


def compose(f: Callable[[B], C], g: Callable[[A], B]) -> Callable[[A], C]:
    """compose functions"""
    return lambda *args, **kwargs: f(g(*args, **kwargs))


class Function(Callable):
    def __init__(self, f: Optional[Callable] = None):
        self.f = identity if f is None else f

    def __xor__(self, g: Callable):
        """compose"""
        return self.__class__(compose(self.f, g))

    def __or__(self, value):
        """apply value to self"""
        return self(value)

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)

    def __floordiv__(self, f: Callable):
        """init"""
        return self.__class__(f)


"""start of functional expression"""
f_ = Function()
