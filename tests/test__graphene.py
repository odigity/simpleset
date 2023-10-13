from graphene.types.enum import EnumMeta

from simpleset.graphene  import Constant


def test__graphene_enum():
    Color = Constant.define_set( "Color", "RED", "GREEN", "BLUE" )
    ColorEnum = Color.graphene()
    assert isinstance( ColorEnum, EnumMeta )
