# Welcome to simpleset

This package contains the following:

- `simpleset.Constant` class — An alternative to Python's [Enum](https://docs.python.org/3/library/enum.html) for defining immutable data sets in code.  Supports a range of use cases, from simple list-of-strings to immutable named objects of arbitrary complexity.
- `simpleset.Error` class — A subclass of `Exception` that provides a pair of utility functions for defining sets or entire families of exception classes in a single line.  (A variation on the enum theme.)  See the [Error](error.md) page for the details.

## simpleset.Constant

### Definition

To define a set of immutable values or complex objects, use `Constant.define_set()`` to specify the name and values of the set:

```python
Color = Constant.define_set( "Color", "RED", "GREEN", "BLUE" )
```

This will:

- construct a subclass of `Constant` named `Color`
- create an instance of `Color` for each value (the value is known as the canonical name or cname)
- attach those instances to the Color class using their cnames

```python
assert issubclass( Color, Constant )
assert isinstance( Color.RED, Color )
Color.RED.cname     # -> "RED"
```

This is the simplest form of definition, referred to as "form 1".

##### Form 2

Instead of just a cname, you can specify both a cname and a value:

```python
Color = Constant.define_set( "Color", RED="ff0000", GREEN="00ff00", BLUE="0000ff" )
Color.RED.value     # -> "ff0000"
```

##### Form 3

If you have more than than one value to specify, use form 3, which supports the setting of arbitrary attributes:

```python
Color = Constant.define_set(
    "Color",
    RED   = dict( hex="ff0000", like=True  ),
    GREEN = dict( hex="00ff00", like=True  ),
    BLUE  = dict( hex="0000ff", like=False ),
)
Color.RED.hex       # -> "ff0000"
Color.RED.like      # -> True
Color.RED.value     # "AttributeError: 'Color' object has no attribute 'value'"
```

### Instance API


### Class API



