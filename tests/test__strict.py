from simpleset.strict import Constant, StrictnessError


def test__strict_forms():
    try:
        Color = Constant.define_set( "Color", "RED", "GREEN", BLUE="0000ff" )
    except StrictnessError.MixedFormsError as e:
        assert "mix args" in str( e )

    try:
        Color = Constant.define_set(
            "Color",
            RED   = "ff0000",
            GREEN = "00ff00",
            BLUE  = dict( hex="0000ff" ),
        )
        assert False
    except StrictnessError.MixedFormsError as e:
        assert "Forms 2 and 3" in str( e )


def test__strict_attributes():
    try:
        Foo = Constant.define_set( "Foo", A=dict( x=1 ), B=dict( y=2 ) )
        assert False
    except StrictnessError.SparseAttributesError as e:
        assert "same set of attributes" in str( e )
