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
