# Welcome to simpleset

## Manifest

This package contains the following:

- `simpleset.Constant` — An alternative to Python's [Enum](https://docs.python.org/3/library/enum.html) for defining immutable data sets in code.  Supports a range of use cases, from simple list-of-strings to immutable named objects of arbitrary complexity.
- `simpleset.Error` — A subclass of `Exception` that provides a pair of utility functions for defining sets or entire families of exception classes in a single line.  (A variation on the enum theme.)  See the [Error](error) page for the details.
- `simpleset.strict` — Contains a class mixin (`StrictMixin`) which adds strictness to set definitions, preventing the mixing of forms or inconsistent attribute sets, and an alternate `Constant` class which includes the mixin.  See the [Customizing](customizing) page for the details.
- `simpleset.graphene` — Contains a class mixin (`GrapheneMixin`) which adds helper methods for generating Graphene enums, and an alternate `Constant` class which includes the mixin.  See the [Integrations](integrations) page for the details.

## Constant

### Definition

To define a set of immutable named objects of arbitrary complexity, use `Constant.define_set()`` to specify the set name + object names:

```python
Color = Constant.define_set( "Color", "RED", "GREEN", "BLUE" )
```

This will:

- construct a subclass of `Constant` named `Color`
- create an instance of `Color` for each name, which is known as the canonical name or cname
- attach those instances to the Color class using their cnames

```python
issubclass( Color, Constant )   # -> True
isinstance( Color.RED, Color )  # -> True
Color.RED.cname                 # -> "RED"
```

This is the simplest form of definition, referred to as "Form 1".

##### Form 2

Instead of just a cname, you can specify both a cname and a value:

```python
Color = Constant.define_set( "Color", RED="ff0000", GREEN="00ff00", BLUE="0000ff" )
Color.RED.value     # -> "ff0000"
```

##### Form 3

If you'd like to associate more more than than one value with each instance, use Form 3, which supports the setting of arbitrary attributes:

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

We've already covered basic attribute access:

```python
obj.cname
obj.value
obj.<arbitrary_attribute>
```

##### Convenience Properties

There are also two convenience properties:

```python
obj.cname_pretty    # "FOO_BAR" -> "Foo Bar"
obj.ordinal         # definition order (from 1 to N, where N is the size of the set)
```

Notice that the `ordinal` property gives you the equivalent of auto-numbered enums for free:

```python
Color.RED.ordinal   # -> 1
Color.BLUE.ordinal  # -> 3
```

##### Magic Methods

Lastly, instances support a number of magic methods, implementing various Python protocols:

```python
str(  Color.RED )       # -> "RED"
repr( Color.RED )       # -> "RED"

len(  Color.RED )       # -> 3, because "RED" is three characters long

# comparisons
Color.RED == "RED"      # -> True  (compared by cname)
Color.RED < Color.BLUE  # -> True  (compared by ordinal)

# using as dict key
mydict[ Color.RED ] = "my favorite"
```

### Class API

The `Constant` class also provides a number of properties and methods for working with the entire set of instances.

##### All Instances

The `all` and `all_cname` properties will return a list of instances or cnames, respectively.

```python
Color.all           # -> [ Color.RED, Color.GREEN, Color.BLUE ]
Color.all_cname     # -> [ "RED", "GREEN", "BLUE" ]
```

You can also iterate the class:

```python
for color in Color:
    print( Color.cname )
```

Or get the count of instances:

```python
len( Color )        # -> 3
```

Or get the length of the longest cname, which is useful for setting the size of a VARCHAR column in databases:

```python
Color.max_length    # -> 5  (because of GREEN)
```

##### A Subset of Instances

To get a subset of instances, you can use the `select` method to specify attribute names and values to match against each instance (simple equality only), or the `filter` method to provide a function that will receive each instance and must return True or False to indicate matching.

```python
Char.define_set( A=dict( ascii=65 ), B=dict( ascii=66 ), C=dict( ascii=67 ) )
Char.select( ascii=66 )                 # -> [ Char.B ]
Char.filter( lambda i: i.ascii < 67 )   # -> [ Char.A, Char.B ]
```

Note: If you pass multiple kwargs to `select`, they will be "AND"-ed, meaning only objects that match all kwargs will be returned.

##### A Single Instance

The `get` method takes kwargs like the `select` method, but returns a single object instead of a list.  Note: If your specified kwargs produces zero results or more than one result, `ValueError` is raised.

```python
Char.get( ascii=66 )    # -> Char.B
```

You can also check for inclusion using either an instance or a bare cname:

```python
Color.RED in Color      # -> True
"RED"     in Color      # -> True
```

If you're writing a function that takes an arg which might be either an instance or a cname, and want to normalize the arg into a proper instance, use member access notation:

```python
# accepts both Color.RED and "RED"
def get_ordinal( color ):
    color = Color[ color ]
    return color.ordinal
```
