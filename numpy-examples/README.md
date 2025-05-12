Examples from numpy official docs: https://numpy.org/doc/stable/f2py/f2py-examples.html#f2py-examples

# Fortran 77 example

```shell
python -m numpy.f2py -h add.pyf -m add add.f
```
- generates the extension module `add` 
- generates the iterface file `add.pyf`

Modify the interface file if needed. Then, to compile the fortran 
source file and the interface file run
```shell
python -m numpy.f2py -c add.pyf add.f
```
For the version including directives run
```shell
python -m numpy.f2py -h add_dir.pyf -m add_dir add_directives.f
python -m numpy.f2py -c add_dir.pyf add_directives.f
```
To verify the module extensions work properly you can now run `python add.py`.


## Fortran 90 example


```shell
python -m numpy.f2py -h myroutine.pyf -m myroutine myroutine.f90
```
After removing `depend(m,n)` statement from the signature file (see [here](https://numpy.org/doc/stable/f2py/f2py-examples.html#depends-keyword-example)) compile the files with
```shell
python -m numpy.f2py -c myroutine.pyf myroutine.f90
```
Test the module can be correctly imported via `python myrout.py`.
