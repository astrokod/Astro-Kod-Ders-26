import sympy as sp
import math


def value_checker(v):
    """
    Alınan değerin Value tipinde oması durumunda symbol değerini döndürür.
    Değilse girdi değerini olduğu gibi döndğürür.
    """
    if isinstance(v, Value):
        return v.symbol

    return v


class Value:
    """
    Value sınıfı.  Veri taşıyıcı olarak kullanılır.
    value, error (seçimli) ve sembol (seçimli) değerleri alır

    >>> Value(1, error=0.03, symbol="x")
    _x=1±0.03

    >>> Value(3.1415, error=0.0003, symbol="pi").round(3)
    _pi=3.142±0.0

    """
    def __init__(self, value, error=0, symbol="x"):
        """

        :param value: Değer
        :param error: Belirsizlik (default=0)
        :param symbol: Sembol (default="x")
        """
        self.value = value
        self.error = abs(error)
        self.symbol = sp.Dummy(symbol)
        self.builder = Builder()

    def __str__(self):
        return f"{self.symbol}={self.value}±{self.error}"

    def __repr__(self):
        return self.__str__()

    def __mul__(self, other):
        return self.builder.multiply(self, other)

    def __rmul__(self, other):
        return self.builder.multiply(other, self)

    def __truediv__(self, other):
        return self.builder.divide(self, other)

    def __rtruediv__(self, other):
        return self.builder.divide(other, self)

    def __add__(self, other):
        return self.builder.sum(self, other)

    def __sub__(self, other):
        return self.builder.subtract(self, other)

    def __pow__(self, power, modulo=None):
        return self.builder.pow(self, power)

    def __rpow__(self, other):
        return self.builder.pow(other, self)

    def __abs__(self):
        return Value(abs(self.value), error=self.error, symbol=self.symbol.name)

    def __neg__(self):
        return Value(-self.value, error=self.error, symbol=self.symbol.name)

    def round(self, n):
        return Value(round(self.value, n), round(self.error, n), symbol=self.symbol.name)


class Builder:
    """
    SymPy formülleri oluşturmak için sınıf

    >>> x = Value(1, error=0.1, symbol="x")
    >>> y = Value(1, error=0.1, symbol="y")

    >>> Builder().cos(x)
    cos(_x)

    >>> Builder().acos(x)
    acos(_x)

    >>> Builder().cosh(x)
    cosh(_x)

    >>> Builder().acosh(x)
    acosh(_x)

    >>> Builder().sin(x)
    sin(_x)

    >>> Builder().tan(x)
    tan(_x)

    >>> Builder().atan2(x, y)
    atan2(_x, _y)

    >>> Builder().sec(x)
    sec(_x)

    >>> Builder().csc(x)
    csc(_x)

    >>> Builder().exp(x)
    exp(_x)


    >>> Builder().pow(x, y)
    _x**_y

    >>> Builder().sqrt(x)
    sqrt(_x)

    >>> Builder().log(x)
    log(_x, E)
    >>> Builder().log(x, base=10)
    log(_x, 10)


    >>> Builder().multiply(x, y)
    _x*_y

    >>> Builder().divide(x, y)
    _x/_y


    >>> Builder().sum(x, y)
    _x + _y
    >>> Builder().subtract(x, y)
    _x - _y
    """
    def __init__(self):
        pass

    def cos(self, value):
        """
        Verilen değeri kullanarak, sumpy.cos döndürür
        :param value: değer
        :return: sympy.cos
        """
        return sp.cos(value_checker(value))

    def acos(self, value):
        """
        Verilen değeri kullanarak, sumpy.acos döndürür
        :param value: değer
        :return: sumpy.acos
        """
        return sp.acos(value_checker(value))

    def cosh(self, value):
        """
        Verilen değeri kullanarak, sumpy.cosh döndürür
        :param value: değer
        :return: sympy.cosh
        """
        return sp.cosh(value_checker(value))

    def acosh(self, value):
        """
        Verilen değeri kullanarak, sumpy.acosh döndürür
        :param value: değer
        :return: sympy.acosh
        """
        return sp.acosh(value_checker(value))

    def sin(self, value):
        """
        Verilen değeri kullanarak, sumpy.sin döndürür
        :param value: değer
        :return: sympy.sin
        """
        return sp.sin(value_checker(value))

    def asin(self, value):
        """
        Verilen değeri kullanarak, sumpy.asin döndürür
        :param value: değer
        :return: sympy.asin
        """
        return sp.asin(value_checker(value))

    def sinh(self, value):
        """
        Verilen değeri kullanarak, sumpy.sinh döndürür
        :param value: değer
        :return: sympy.sinh
        """
        return sp.sinh(value_checker(value))

    def asinh(self, value):
        """
        Verilen değeri kullanarak, sumpy.asinh döndürür
        :param value: değer
        :return: sympy.asinh
        """
        return sp.asinh(value_checker(value))

    def tan(self, value):
        """
        Verilen değeri kullanarak, sumpy.tan döndürür
        :param value: değer
        :return: sympy.tan
        """
        return sp.tan(value_checker(value))

    def atan(self, value):
        """
        Verilen değeri kullanarak, sumpy.atan döndürür
        :param value: değer
        :return: sympy.atan
        """
        return sp.atan(value_checker(value))

    def atan2(self, x, y):
        """
        Verilen değeri kullanarak, sumpy.atan2 döndürür
        :param x: x değeri
        :param y: y değeri
        :return: sumpy.atan2
        """
        return sp.atan2(value_checker(x), value_checker(y))

    def tanh(self, value):
        """
        Verilen değeri kullanarak, sumpy.tanh döndürür
        :param value: değer
        :return: sympy.tanh
        """
        return sp.tanh(value_checker(value))

    def atanh(self, value):
        """
        Verilen değeri kullanarak, sumpy.atanh döndürür
        :param value: değer
        :return: sympy.atanh
        """
        return sp.atanh(value_checker(value))

    def sec(self, value):
        """
        Verilen değeri kullanarak, sumpy.sec döndürür
        :param value: değer
        :return: sympy.sec
        """
        return sp.sec(value_checker(value))

    def sech(self, value):
        """
        Verilen değeri kullanarak, sumpy.sech döndürür
        :param value: değer
        :return: sympy.sech
        """
        return sp.sech(value_checker(value))

    def asec(self, value):
        """
        Verilen değeri kullanarak, sumpy.asec döndürür
        :param value: değer
        :return: sympy.asec
        """
        return sp.asec(value_checker(value))

    def asech(self, value):
        """
        Verilen değeri kullanarak, sumpy.asech döndürür
        :param value: değer
        :return: sympy.asech
        """
        return sp.asech(value_checker(value))

    def csc(self, value):
        """
        Verilen değeri kullanarak, sumpy.csc döndürür
        :param value: değer
        :return: sympy.csc
        """
        return sp.csc(value_checker(value))

    def acsc(self, value):
        """
        Verilen değeri kullanarak, sumpy.acsc döndürür
        :param value: değer
        :return: sympy.acsc
        """
        return sp.acsc(value_checker(value))

    def csch(self, value):
        """
        Verilen değeri kullanarak, sumpy.csch döndürür
        :param value: değer
        :return: sympy.csch
        """
        return sp.csch(value_checker(value))

    def acsch(self, value):
        """
        Verilen değeri kullanarak, sumpy.acsch döndürür
        :param value: değer
        :return: sympy.acsch
        """
        return sp.acsch(value_checker(value))

    def exp(self, value):
        """
        Verilen değeri kullanarak, sumpy.exp döndürür
        :param value: değer
        :return: sympy.exp
        """
        return sp.exp(value_checker(value))

    def pow(self, value, p):
        """
        Verilen değeri kullanarak, sympy.pow değeri döndürür
        :param value: değer
        :return: sympy.pow
        """
        return value_checker(value) ** value_checker(p)

    def sqrt(self, value):
        """
        Verilen değeri kullanarak, sympy.sqrt değeri döndürür
        :param value: değer
        :return: sympy.pow
        """
        return sp.sqrt(value_checker(value))

    def log(self, value, base=None):
        """
        Verilen değeri kullanarak, sumpy.log döndürür
        :param value: değer
        :return: sympy.log
        """
        base = base or sp.exp(1)
        return sp.log(value_checker(value), base, evaluate=False)

    def multiply(self, value1, value2):
        """
        Verilen değeri kullanarak, sympy.Mul değeri döndürür
        :param value1: 1. değer
        :param value2: 2. değer
        :return: sympy.Mul
        """
        return value_checker(value1) * value_checker(value2)

    def divide(self, value1, value2):
        """
        Verilen değeri kullanarak, sympy.Mul değeri döndürür
        :param value1: 1. değer
        :param value2: 2. değer
        :return: sympy.Mul
        """
        return value_checker(value1) / value_checker(value2)

    def sum(self, value1, value2):
        """
        Verilen değeri kullanarak, sympy.Add değeri döndürür
        :param value1: 1. değer
        :param value2: 2. değer
        :return: sympy.Add
        """
        return value_checker(value1) + value_checker(value2)

    def subtract(self, value1, value2):
        """
        Verilen değeri kullanarak, sympy.Add değeri döndürür
        :param value1: 1. değer
        :param value2: 2. değer
        :return: sympy.Add
        """
        return value_checker(value1) - value_checker(value2)


class Error:
    """
    >>> x = Value(3.1415, error=0.002, symbol="x")
    >>> f = x ** x
    >>> Error().propagate(f, (x, ), symbol="res")
    _res=36.4549147287201±0.15636973988079056
    """
    def __init__(self):
        pass

    def values2dict(self, values):
        """
        Gelen values listesinden sumbs'ın kabul edebileceği, dict tipinde, bir veri oluşturur

        :param values: değerler
        :return: subs için dict objesi
        """
        return {value.symbol: value.value for value in values}

    def propagate(self, f, values, symbol="x"):
        """
        Belirsizlik yayılması hesabı yapar.

        :param f: sympy fonksiyon
        :param values: fonksiyonda hatları hsaba katılacak değerler
        :param symbol: çıktı değer için sembol
        :return: belirsizliği hesaplanmış işlem
        """
        ditc2use = self.values2dict(values)
        sums = 0
        for value in values:
            sums += math.pow(sp.diff(f, value.symbol).evalf(subs=ditc2use), 2) * math.pow(value.error, 2)

        return Value(sp.N(f.evalf(subs=ditc2use)), error=math.sqrt(sums), symbol=symbol)
