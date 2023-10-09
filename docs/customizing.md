# Customizing

TODO

# OLD CONTENT

If you want to add your own features to Object, just subclass it:

    class MyObject( Object ):
        def my_new_method( self ):
            ...

    Color = MyObject.define( "Color", "RED", "GREEN", "BLUE" )
    Color.RED.my_new_method()

That works well for defining a project-wide base class, but what if you just want a one-off class to add a feature to a specific object type in your collection?  Easy &mdash; just skip past `define`, which is just a helper method around `createmany`, and use `createmany` directly:

    class Planet( MyObject ):
        @property
        def circumference( self ):
            return self.diameter * 3.14

    Planet.createmany(
        EARTH=dict( diameter=12742 ),
        MARS=dict(  diameter=6794  ),
    )

    Planet.EARTH.circumference
