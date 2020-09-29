"""
Wynik działania interpretera

In [9]: "Hello"
Out[9]: 'Hello'

In [10]: 'Hello'
Out[10]: 'Hello'

In [11]: 2
Out[11]: 2

In [12]: Hello
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-12-1d229271928d> in <module>
----> 1 Hello

NameError: name 'Hello' is not defined

"""

add1 = 100
add2 = 100.0
sum_value = add1 + add2

print(f"""
add1 typu {type(add1)} i wartości {add1}
add2 typu {type(add2)} i wartości {add2}
sum_value typu {(type(sum_value))} i wartości {sum_value}""")

