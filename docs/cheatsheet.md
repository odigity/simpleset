# Cheatsheet

### Definition

`Constant.define_set` creates & returns a subclass for your constant set.

```python
# Form 1  (canonical_name only)
Color = Constant.define_set( "Color", "RED", "GREEN", "BLUE" )

# Form 2  (canonical_name + label)
Color = Constant.define_set( "Color", RED="ff0000", GREEN="00ff00", BLUE="0000ff" )

# Form 3  (canonical_name + arbitrary attributes)
Color = Constant.define_set(
    "Color",
    RED   = dict( hex="ff0000", like=True  ),
    GREEN = dict( hex="00ff00", like=True  ),
    BLUE  = dict( hex="0000ff", like=False ),
)
```

### Set API

```python
Color.RED       # constants are attached to subclass as attributes using canonical_name
...

Color.populate( *args, **kwargs )   # create & register multiple constants
                                    # used by Constant.define_set; supports all three forms

Color.all                           # -> [ Color.RED, ... ]
Color.all_cn                        # -> [ "RED", ... ]
Color.max_length                    # returns length of longest canonical_name

Color.filter(              func )   # returns list of constants for which func returns True
Color.select(          **kwargs )   # returns list of constants who's attributes match kwargs
Color.get(             **kwargs )   # returns single constant who's attributes match kwargs
                                    # raises ValueError if kwargs matches 0 or 2+ constants

Color.__contains__( item )          # Color.RED in Color  -or-  "RED" in Color
Color.__getitem(    item )          # Color[ Color.RED ]  -or-  Color[ "RED" ]
                                    # returns None if constant not found (by canonical_name)
Color.__iter__(          )          # for color in Color
Color.__len__(           )          # len( Color ) -> count of constants
```

### Constant API

```python
c = Color.RED

c.cn                    # shortcut for c.canonical_name
c.cn_lower              # lowercased canonical_name
c.cn_title              # titlecased canonical_name (also replaces "_" with " ")
c.ordinal               # based on definition order (from 1 .. len)

c.__repr__(     )       # return canonical_name
c.__str__(      )       # return canonical_name
c.__len__(      )       # length of canonical_name:  len( c )

c.__eq__( other )       # compare by canonical_name (also __ne__)
c.__lt__( other )       # compare by canonical_name (also __le__, __gt__, __ge__)

c.__hash__(     )       # hash of canonical_name to support use as dict key
```
