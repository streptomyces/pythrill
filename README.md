# Conceptual code for Python 3

When you clone this repository a directory named `pythrill` will
be created. The instructions and commands below assume that your
working directory is the parent of `pythrill`. So, to run `modtest.py`
you will do

~~~ 
python3 pythrill/modtest.py
~~~

#### Compile only

`python3 -m py_compile script.py` can be used to compile a script.
A `.pyc` file is produced which can be ignored if you are just
interested in syntax checking.

#### Boolean

The `bool` class has only two possible instances `True` and `False`.
Note the capitalisation.

#### Constructors

There are constructors for the builtin types.

* `int()`
* `float()`
* `complex()`
* `list()`
* `dict()`
* `set()`

#### Literal syntax

* `int`s are instantiated by context.
* `float`s are instantiated by context.
* `complex`s are instantiated by context.
* `list`s are made using `[1, 2, 3, 4, "five", "six"]`
* `dict`s are made using `{k1:v1, k2:v2, k3:v3}`
* `tuple`s are made using `("one", "two", 3, 4)`
* `set`s are made using `{"one", "two", 3, 4}`

Note that empty braces `{}` are literal for an empty dictionary,
not an empty set. to get an empty set use `set()`.

