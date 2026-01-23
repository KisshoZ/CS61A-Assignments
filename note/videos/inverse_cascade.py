def inverse_cascade(n):
    """                                     
    >>> inverse_cascade(123)
    1
    12
    123
    12
    1
    """
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if(n):
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)
"""为了打印出
1
12
123
12
1
这种形式的东西
"""