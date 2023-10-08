from objects import Object


def test__object__form1():
    Color = Object.define( "Color", "RED", "GREEN", "BLUE" )
    assert issubclass( Color,     Object )
    assert isinstance( Color.RED, Color  )
    assert Color.RED.canonical_name == "RED"


def test__object__form2():
    Color = Object.define( "Color", RED="ff0000", GREEN="00ff00", BLUE="0000ff" )
    assert Color.RED.canonical_name == "RED"
    assert Color.RED.label          == "ff0000"


def test__object__form3():
    Color = Object.define(
        "Color",
        RED   = dict( foo=42, like=True  ),
        GREEN = dict( foo=43, like=True  ),
        BLUE  = dict( foo=43, like=False ),
    )
    assert Color.RED.canonical_name == "RED"
    assert Color.RED.foo            == 42


def test__object__instance_methods():
    Color = Object.define( "Color", "RED", "GREEN", "BLUE", "FOO_BAR" )

    # __eq__
    assert Color.RED == Color.RED
    assert Color.RED == "RED"

    # __len__
    assert len( Color.BLUE ) == 4

    # __repr__
    assert repr( Color.RED ) == "RED"

    # __str__
    assert str( Color.RED ) == "RED"

    # cn_lower
    assert Color.RED.cn_lower == "red"

    # cn_title
    assert Color.RED.cn_title     == "Red"
    assert Color.FOO_BAR.cn_title == "Foo Bar"

    # ordinal
    assert Color.BLUE.ordinal == 3
