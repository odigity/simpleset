# Customizing

`Constant` is just a plain old Python class, so if you want to add anything to it, just subclass it.

### Custom Base Class

For example, you may want to create a subclass for your whole project that adds general features:

```python
class CustomConstant( Constant ):
    def cname_in_mirror( self ):
        return self.cname[::-1]     # reverse string

Color = CustomConstant.define( "Color", "RED", "GREEN", "BLUE" )
Color.RED.cname_in_mirror()         # -> "DER"
```

### Custom One-Off Class

If you want to create a custom class for only one value set — such as to add convenience properties specific to planets — start by creating a subclass:

```python
class Planet( Constant ):
    @property
    def circumference( self ):
        return self.diameter * 3.14
```

Now, if you call `Planet.define_set`, it will construct and return a subclass of Planet, which is probably not what you want.  If you want to populate the `Planet` class itself with a set of instances, skip `define_set` and instead call `populate` directly — which is the same method that `define_set` uses.

```python
Planet.populate(
    Earth=dict( diameter=12742 ),
    Mars=dict(  diameter=6794  ),
)

Planet.Earth.circumference      # -> 40009.88
```

### Example: Strict

This package includes a class which subclasses `simpleset.Constant` and overrides the `populate` method in order to enforce strictness when defining sets.

```python
from simpleset.strict import Constant, StrictnessError
```

It will raise an exception if you mix forms:

```python
try:
    Color = Constant.define_set( "Color", "RED", "GREEN", BLUE="0000ff" )
except StrictnessError:
    ...
```

Or if you don't specify the same set of attributes for all instances:

```python
try:
    Foo = Constant.define_set( "Foo", A=dict( x=1 ), B=dict( y=2 ) )
except StrictnessError:
    ...
```

If you want to combine this feature with other mixins, import and use the mixin instead:

```python
from simpleset import Constant
from simpleset.strict import StrictMixin
class MyConstant( StrictMixin, Constant ):
    pass
```
