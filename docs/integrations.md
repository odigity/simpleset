# Integrations

## Django

One example of how to use Constants with [Django](https://pypi.org/projects/Django/):

```python
Color = Constant.define_set( "Color", "RED", "GREEN", "BLUE" )

# declare an enumerated DB field in a model class
color = models.CharField(
    choices    = Color.choices(),
    max_length = Color.max_length,
    default    = Color.RED,
)
```

If you prefer a different pair of values to populate the `choices` attribute, use `as_tuple`.

## Graphene

Unfortunately, working with [Graphene](https://pypi.org/projects/graphene/) is much more complicated due to its horrificly awful design and implementation.  Fortunately, I've already lived through that pain, and can provide a solution.

**Import Warning**

You will need to import one of the two classes in `simpleset.graphene`.  That module will need to import the `graphene` package — which is not a dependency of this package! — so make sure it's already installed before you do this.  (In practice, this shouldn't be a problem, as anyone who needs to generate Graphene enums surely has `graphene` listed in their project dependencies.)

##### Classes

You can either import `GrapheneMixin` and use it to generate your own base class:

```python
from simpleset import Constant
from simpleset.graphene import GrapheneMixin
class MyConstant( GrapheneMixin, Constant ):
    ...
```

Or you can import `simpleset.graphene.Constant`, which has already combined `simpleset.Constant` and `GrapheneMixin` for you:

```python
from simpleset.graphene import Constant
```

##### Usage

The simplest case:

```python
Color = Constant.define_set( "Color", "RED", "GREEN", "BLUE" )
ColorEnum = Color.graphene()
```

The `graphene` class method will construct and return a `graphene.Enum` class populated with the data from your class.  Specifically, the enum class name will be the same as your class name, the item names and values will both be set to `cname` (configurable), the item descriptions will be set to `cname_pretty` (configurable), and the class description will be based on your class docstring — if it exists.

*Note: The `graphene` method caches results for each combination of inputs, so if you call it twice with the same inputs, you will only generate one Graphene Enum.  Without this, Graphene would end up raising an exception when generating the schema.*

The above example is the equivalent of doing this:

```python
from graphene import Enum

class Color( Enum ):
    RED   = "RED"
    GREEN = "GREEN"
    BLUE  = "BLUE"

    @property
    def description( self ):
        match self:
            case Color.RED:
                return "Red"
            case Color.GREEN:
                return "Green"
            case Color.BLUE:
                return "Blue"
            case _:
                return Color.__doc__
```

To set the class name to something else, pass a `name` param:

```python
ColorEnum = Color.graphene( name="ColorEnum" )
```

To filter out some of the instances, pass a `filter` param:

```python
ColorEnum = Color.graphene( filter=lambda o: o != "BLUE" )
```

To use attributes other than `cname` and `cname_pretty`, call `graphene_config` on the class before calling `graphene`:

```python
Color.graphene_config( name="attr1", value="attr2", desc="attr3" )
ColorEnum = Color.graphene()
```

All kwargs are optional, so you only need to include the ones you want to override.  It will also return itself in case you want to use chaining:

```python
Color = Constant.define_set(
    "Color",
    RED   = dict( hex="ff0000", description="a lovely shade of red"   ),
    GREEN = dict( hex="00ff00", description="a lovely shade of green" ),
    BLUE  = dict( hex="0000ff", description="a lovely shade of blue"  ),
).graphene_config( desc="description" )

ColorEnum = Color.graphene()
```
