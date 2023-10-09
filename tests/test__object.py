from objects import Object


def test__object__define__form1():
    Color = Object.define( "Color", "RED", "GREEN", "BLUE" )
    assert issubclass( Color,     Object )
    assert isinstance( Color.RED, Color  )
    assert Color.RED.canonical_name == "RED"


def test__object__define__form2():
    Color = Object.define( "Color", RED="ff0000", GREEN="00ff00", BLUE="0000ff" )
    assert Color.RED.canonical_name == "RED"
    assert Color.RED.label          == "ff0000"


def test__object__define__form3():
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

    ##  Magic Methods

    # __eq__
    assert Color.RED == Color.RED
    assert Color.RED == "RED"

    # __len__
    assert len( Color.BLUE ) == 4

    # __lt__
    assert Color.BLUE  < Color.GREEN
    assert Color.GREEN > Color.BLUE     # provided by functools.total_ordering

    # __repr__
    assert repr( Color.RED ) == "RED"

    # __str__
    assert str( Color.RED ) == "RED"

    ##  Normal Methods

    assert Color.RED.cn           == "RED"
    assert Color.RED.cn_lower     == "red"
    assert Color.RED.cn_title     == "Red"
    assert Color.FOO_BAR.cn_title == "Foo Bar"
    assert Color.GREEN.ordinal    == 2


def test__object__class_methods():
    Color = Object.define(
        "Color",
        RED   = dict( foo=42, like=True  ),
        GREEN = dict( foo=43, like=True  ),
        BLUE  = dict( foo=43, like=False ),
    )

    ##  Magic Methods

    # __contains__
    assert Color.RED in Color
    assert "RED"     in Color

    # __getitem__
    assert Color[ "RED" ] == Color[ Color.RED ] == Color.RED

    # __iter__
    objs = [ obj for obj in Color ]
    assert len( objs ) == 3
    assert objs[ 0 ] == Color.RED

    # __len__
    assert len( Color ) == 3

    ##  Normal Methods

    # all
    assert Color.all[ 0 ] == Color.RED
    assert isinstance( Color.all[ 0 ], Color )

    # all_cn
    assert Color.all_cn[ 0 ] == Color.RED
    assert isinstance( Color.all_cn[ 0 ], str )

    # filter
    assert len( Color.filter( lambda o: o.like  ) ) == 2

    # get 1
    assert Color.get( foo=42 ) == Color.RED
    # get > 1
    try:
        Color.get( foo=43 )
        assert False
    except ValueError as e:
        ...
    # get < 1
    try:
        Color.get( foo=99 )
        assert False
    except ValueError as e:
        ...

    # max_length
    assert Color.max_length == 5

    # select
    assert len( Color.select(                    ) ) == 3
    assert len( Color.select( foo=42             ) ) == 1
    assert len( Color.select( foo=99             ) ) == 0
    assert len( Color.select(         like=True  ) ) == 2
    assert len( Color.select(         like=False ) ) == 1
    assert len( Color.select( foo=43, like=True  ) ) == 1
