from simpleset import Constant


def test__form1():
    Color = Constant.define_set( "Color", "RED", "GREEN", "BLUE" )
    assert issubclass( Color,     Constant )
    assert isinstance( Color.RED, Color    )
    assert Color.RED.cname == "RED"


def test__form2():
    Color = Constant.define_set( "Color", RED="ff0000", GREEN="00ff00", BLUE="0000ff" )
    assert Color.RED.cname == "RED"
    assert Color.RED.value == "ff0000"


def test__form3():
    Color = Constant.define_set(
        "Color",
        RED   = dict( foo=42, like=True  ),
        GREEN = dict( foo=43, like=True  ),
        BLUE  = dict( foo=43, like=False ),
    )
    assert Color.RED.cname == "RED"
    assert Color.RED.foo   == 42


def test__instance_methods():
    Color = Constant.define_set( "Color", "RED", "GREEN", "BLUE", "FOO_BAR" )

    ##  Magic Methods

    # __eq__
    assert Color.RED == Color.RED
    assert Color.RED == "RED"

    # __len__
    assert len( Color.BLUE ) == 4

    # __lt__
    assert Color.GREEN < Color.BLUE
    assert Color.BLUE  > Color.GREEN    # provided by functools.total_ordering

    # __repr__
    assert repr( Color.RED ) == "RED"

    # __str__
    assert str( Color.RED ) == "RED"

    ##  Normal Methods

    assert Color.RED.cname            == "RED"
    assert Color.RED.cname_pretty     == "Red"
    assert Color.FOO_BAR.cname_pretty == "Foo Bar"
    assert Color.GREEN.ordinal        == 2


def test__exports():
    Color = Constant.define_set( "Color", "RED", "GREEN", "BLUE" )
    Fruit = Constant.define_set(
        "Fruit",
        Apple  = dict( price=1, qty=10 ),
        Orange = dict( price=2, qty=20 ),
    )

    # as_cnames
    assert Color.as_cnames()[ 0 ] == "RED"
    assert Color.as_cnames( filter=lambda o: o != "RED" )[ 0 ] == "GREEN"

    # pick
    assert Fruit.pick( "qty" )[ 0 ] == 10
    assert Fruit.pick( "qty", filter=lambda o: o.qty > 10 )[ 0 ] == 20

    # as_dict / as_dicts
    assert Fruit.Apple.as_dict() == dict( cname="Apple", price=1, qty=10 )
    assert Fruit.Apple.as_dict(  "price", "qty" ) ==   dict( price=1, qty=10 )
    assert Fruit.as_dicts(
        "price", "qty", filter=lambda o: o != "Orange"
    ) == [ dict( price=1, qty=10 ) ]

    # as_tuple / as_tuples
    assert Fruit.Apple.as_tuple() == ( "Apple", 1, 10 )
    assert Fruit.Apple.as_tuple(  "qty", "cname" ) ==   ( 10, "Apple" )
    assert Fruit.as_tuples(
        "qty", "cname", filter=lambda o: o != "Orange"
    ) == [ ( 10, "Apple" ) ]
    assert Color.BLUE.as_tuple() == ( "BLUE", 3 )   # with ordinal value

    # choices
    assert Color.choices()[ 0 ] == ( "RED", "Red" )


def test__class_methods():
    Color = Constant.define_set(
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


def test__immutability():
    Fruit = Constant.define_set( "Fruit", apple=dict( qty=10 ) )
    assert Fruit.apple.qty == 10

    # try setting attribute to different value
    try:
        Fruit.apple.qty = 11
        assert False
    except AttributeError as e:
        assert "immutable" in str( e )

    # try deleting attribute
    try:
        del Fruit.apple.qty
        assert False
    except AttributeError as e:
        assert "immutable" in str( e )

    # try setting instance to different value
    try:
        Fruit.apple = "I ate it"
        assert False
    except AttributeError as e:
        assert "immutable" in str( e )

    # try deleting instance
    try:
        del Fruit.apple
        assert False
    except AttributeError as e:
        assert "immutable" in str( e )


def test__attribute_collision():
    Color = Constant.define_set( "Color", "RED", "GREEN", "BLUE" )
    assert Color.GREEN.ordinal == 2
    Funky = Constant.define_set( "Funky", Foo=dict( ordinal=99 ) )
    assert Funky.Foo.ordinal == 99
