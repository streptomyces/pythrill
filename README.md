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

I am having trouble explicitly passing `False` via `argparse`.
Any string is interpreted as `True`, even the strings _False_
and _0_ (zero).

#### Constructors

There are constructors for the builtin types.

* `int()`
* `float()`
* `complex()`
* `list()`
* `dict()`
* `set()`

The argument to `dict()` is a list of tuples.

~~~ {.py}
dict([(k1, v1), (k2,v2)])
~~~

Below also works. Think assignments to keys as arguments.

~~~ {.py}
dict(k1 = v1, k2 = v2, k3 = v3)
~~~

The argument to `set()` is a list.

~~~ {.py}
set([1,2,3])
~~~

#### Literal syntax

* `int` instantiated by context.
* `float` instantiated by context.
* `complex` instantiated by context.
* `list` made using `[1, 2, 3, 4, "five", "six"]`
* `dict` made using `{k1:v1, k2:v2, k3:v3}`
* `tuple` made using `("one", "two", 3, 4)`
* `set` made using `{"one", "two", 3, 4}`

Note that empty braces `{}` are literal for an empty dictionary,
not an empty set. To get an empty set use `set()`.

### A module of commonly used functions

In the directory _py3lib/_ there is file named _common.py_. This is
a collection of functions. They behave like some of those in
my _Sco::Common_ in Perl. Some may not be appropriate or needed in
Python, and most can be written better.



