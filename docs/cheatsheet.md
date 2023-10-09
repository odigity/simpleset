# Cheatsheet

### Definition

`Object.define` creates & returns a subclass for your object set.

```python
# Form 1  (canonical_name only)
Color = Object.define( "Color", "RED", "GREEN", "BLUE" )

# Form 2  (canonical_name + label)
Color = Object.define( "Color", RED="ff0000", GREEN="00ff00", BLUE="0000ff" )

# Form 3  (canonical_name + arbitrary attributes)
Color = Object.define(
    "Color",
    RED=dict(   hex="ff0000", like=True  ),
    GREEN=dict( hex="00ff00", like=True  ),
    BLUE=dict(  hex="0000ff", like=False ),
)
```

### Subclass API

```python
Color.RED       # objects are attached to subclass as attributes using canonical_name
...

Color.populate( *args, **kwargs )   # create & register multiple objects
                                    # used by Object.define; supports all three forms

Color.all                           # -> [ Color.RED, ... ]
Color.all_cn                        # -> [ "RED", ... ]
Color.max_length                    # returns length of longest canonical_name

Color.filter(              func )   # returns list of objects for which func returns True
Color.select(          **kwargs )   # returns list of objects who's attributes match kwargs
Color.get(             **kwargs )   # returns single object who's attributes match kwargs
                                    # raises ValueError if kwargs matches 0 or 2+ objects

Color.__contains__( item )          # Color.RED in Color  -or-  "RED" in Color
Color.__getitem(    item )          # Color[ Color.RED ]  -or-  Color[ "RED" ]
                                    # returns None if object not found (by canonical_name)
Color.__iter__(          )          # for color in Color
Color.__len__(           )          # len( Color ) -> count of objects
```

### Instance API

```python
obj.cn                  # shortcut for obj.canonical_name
obj.cn_lower            # lowercased canonical_name
obj.cn_title            # titlecased canonical_name (also replaces "_" with " ")
obj.ordinal             # based on definition order (from 1 .. len)

obj.__repr__(     )     # return canonical_name
obj.__str__(      )     # return canonical_name
obj.__len__(      )     # length of canonical_name:  len( obj )

obj.__eq__( other )     # compare by canonical_name (also __ne__)
obj.__lt__( other )     # compare by canonical_name (also __le__, __gt__, __ge__)

obj.__hash__(     )     # hash of canonical_name to support use as dict key
```
