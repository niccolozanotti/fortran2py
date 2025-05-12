"""Example from https://numpy.org/doc/stable/f2py/f2py-examples.html#creating-source-for-a-basic-extension-module.
Binds Fortran-77 subroutine zadd to a python function
"""

from add import zadd
from add_dir import zadd as zadd_dir


if __name__ == "__main__":
    print("zadd with directives in .pyf")
    print(zadd.__doc__)
    c = zadd([1, 2, 3], [4, 5, 6])
    print("zadd([1,2,3],[4,5,6]) = ", c)
    print("\n-----------------------\n")

    print("zadd with directives in .f")
    print(zadd_dir.__doc__)
    c = zadd_dir([1, 2, 3], [4, 5, 6])
    print("zadd([1,2,3],[4,5,6]) = ", c)
