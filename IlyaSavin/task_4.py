#! /usr/bin/env python
# TODO: 1) Find a way to call `inner_function` without moving it
# from inside of `enclosed_function`.
# 2.1) Modify ONE LINE in `inner_function` to make it print variable 'a'
# from global scope.
# 2.2) Modify ONE LINE in `inner_function` to make it print variable 'a'
# form enclosing function.


"""
calling inner_function from modules.legb
2.1 and 2.2 in the comment in modules/legb.py
"""

from modules.legb import enclosing_funcion

inner_function = enclosing_funcion()
inner_function()
