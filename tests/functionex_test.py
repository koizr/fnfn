import unittest
from operator import neg, sub

from fnfn import f_, flip, compose, identity, Function


class FunctionsTest(unittest.TestCase):
    def test_identity(self):
        self.assertEqual(identity(1), 1)

    def test_flip(self):
        actual = flip(sub)(10, 5)
        expected = sub(5, 10)
        self.assertEqual(actual, expected)

    def test_compose(self):
        actual = compose(neg, len)([1, 2, 3])
        expected = neg(len([1, 2, 3]))
        self.assertEqual(actual, expected)


class FunctionalExpressionTest(unittest.TestCase):
    def test_init(self):
        f = Function(lambda x: x + 1)
        self.assertEqual(f(42), 43)

    def test_exp(self):
        f = f_ // (lambda x: x + 1)
        self.assertEqual(f(42), 43)

    def test_apply(self):
        f = f_ // (lambda x: x + 1)
        self.assertEqual(f | 42, 43)

    def test_compose(self):
        f = f_ // (lambda x: x + "?") ^ (lambda x: x + "!")
        self.assertEqual(f | "Hello", "Hello!?")

    def test_function_as_callable(self):
        f = Function(lambda x: x + "?")
        g = Function(lambda x: x + "!")
        self.assertEqual(f ^ g | "Hello", "Hello!?")


if __name__ == "__main__":
    unittest.main()
