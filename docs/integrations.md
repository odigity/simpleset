# Integrations

TODO

# OLD CONTENT

## Bonus: Help for Django Users

Stop using Django.

.

If you must use Django, I suggest adding the following to your personal Object base class:

    def django_pair( self ):
        django_value = self.canonical_name
        django_label = self.label if hasattr( self, "label" ) else self.canonical_name
        return ( django_value, django_label )

    @classmethod
    def choices( cls, filter=None ):
        objects = cls.objects.filter( filter ) if filter else cls.objects.all
        return [ obj.django_pair() for obj in objects ]

Then you can use Objects instead of Enums in model fields:

    color = models.CharField(
        choices    = Color.choices(),                                   # use all values
            -or-
        choices    = Color.choices( filter=lambda o: o != "BLUE" ),     # filter out some
        max_length = Color.objects.max_length,
        default    = Color.RED,
    )

## Bonus: Help for Graphene Users

Stop using Graphene.

.

Seriously, it's really really bad.

.

If you must use Graphene, I suggest adding the following to you personal Object base class:

    from functools import cache
    from graphene import Enum

    def graphene_pair( self ):
        graphene_name  = self.canonical_name
        graphene_value = self.canonical_name
        return ( graphene_name, graphene_value )

    def graphene_description( self ):
        if hasattr( self, "description" ):
            return self.description
        if hasattr( self, "label" ):
            return self.label
        return None

    @classmethod
    @cache
    def graphene( cls, name=None, filter=None ):
        name         = name or cls.__name__
        objects      = cls.objects.filter( filter ) if filter else cls.objects.all
        enum_items   = [ obj.graphene_pair() for obj in objects ]
        descriptions = { obj.graphene_pair()[ 0 ]: obj.graphene_description() for obj in objects }

        def description( enum_obj ):
            return descriptions[ enum_obj.name ] if enum_obj else cls.__doc__

        return graphene.Enum( name, enum_items, description=description )

Then you can use Objects instead of Enums and still generate Graphene enums from them:

    ColorEnum = Color.graphene()

    class Foo( graphene.ObjectType ):
        color = ColorEnum( required=True )
        ...
