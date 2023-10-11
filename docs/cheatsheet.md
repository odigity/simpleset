# Cheatsheet

### Definition

`Constant.define_set` creates & returns a subclass for your constant set.

```python
# Form 1  (cname only)
Color = Constant.define_set( "Color", "RED", "GREEN", "BLUE" )

# Form 2  (cname + value)
Color = Constant.define_set( "Color", RED="ff0000", GREEN="00ff00", BLUE="0000ff" )

# Form 3  (cname + arbitrary attributes)
Color = Constant.define_set(
    "Color",
    RED   = dict( hex="ff0000", like=True  ),
    GREEN = dict( hex="00ff00", like=True  ),
    BLUE  = dict( hex="0000ff", like=False ),
)
```

### Instance API

```python
c = Color.RED

c.cname
c.cname_lower           # lowercased cname
c.cname_title           # titlecased cname (also replaces "_" with " ")
c.ordinal               # based on definition order (from 1 .. len)

c.value                 # if specified using form 2, or explicitly with form 3
c.<attribute>           # access any attributes specified during creation

c.__repr__(     )       # return cname
c.__str__(      )       # return cname
c.__len__(      )       # length of cname:  len( c )

c.__eq__( other )       # compare by cname (also __ne__)
c.__lt__( other )       # compare by cname (also __le__, __gt__, __ge__)

c.__hash__(     )       # hash of cname to support use as dict key
```

### Class API

```python
Color.RED       # constants are attached to subclass as attributes using cname
...

Color.populate( *args, **kwargs )   # create & register multiple constants
                                    # used by Constant.define_set; supports all three forms

Color.all                           # -> [ Color.RED, ... ]
Color.all_cname                     # -> [ "RED", ... ]
Color.max_length                    # returns length of longest cname

Color.filter(              func )   # returns list of constants for which func returns True
Color.select(          **kwargs )   # returns list of constants who's attributes match kwargs
Color.get(             **kwargs )   # returns single constant who's attributes match kwargs
                                    # raises ValueError if kwargs matches 0 or 2+ constants

Color.__contains__( item )          # Color.RED in Color  -or-  "RED" in Color
Color.__getitem(    item )          # Color[ Color.RED ]  -or-  Color[ "RED" ]
                                    # returns None if constant not found (by cname)
Color.__iter__(          )          # for color in Color
Color.__len__(           )          # len( Color ) -> count of constants
```
