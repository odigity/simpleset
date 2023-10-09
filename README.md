\[ [Documentation](https://simpleset.readthedocs.io/en/latest/) | [Changelog](CHANGELOG.md) \]

### Disclaimer!

This package is very new and has only be used by me on a handful of projects.

When others start using it in different contexts, providing useful feedback on the quality of the API, and guiding its evolution to a mature 1.0 release, I will then offer API stability guarantees and adhere to SemVer.

In the meantime, I see no harm in using it in production given how simple it is.  However, _**please make sure to pin your package dependency to an exact version**_ so your code doesn't break if and when I decide to change something.

### Synopsis

I dislike Python enums.  They behave strangely and are difficult to build on top of or extend.  This package provides a Python class named `Object` which facilitates the creation and usage of enumerated values.  This plain old Python class is both simpler to understand and more powerful/flexible then native enums.

Even a Python beginner should be able to understand *most* of the source code.  The only notable exception is the `Object.define()` class method which uses `type()` to construct a subclass of itself.

### Preview

```
from objects import Object

# simplest form

Color = Object.define( "Color", "RED", "GREEN", "BLUE" )

assert Color.RED == "RED"
Color.RED.canonical_name    # "RED"
Color.all                   # [ Color.RED, Color.GREEN, Color.BLUE ]

# more complex

Color = Object.define(
    "Color",
    RED   = dict( hex="ff0000", like=True  ),
    GREEN = dict( hex="00ff00", like=True  ),
    BLUE  = dict( hex="0000ff", like=False ),
)

assert Color.max_length == 5        # useful for a VARCHAR db column
assert Color.select( like=True )    # [ Color.RED, Color.GREEN ]
assert Color.get( like=False )      # Color.BLUE
```

[Learn more.](https://simpleset.readthedocs.io/en/latest/)
