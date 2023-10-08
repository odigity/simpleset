from objects import Object


def test__object_manager():
    Color = Object.define(
        "Color",
        RED   = dict( foo=42, like=True  ),
        GREEN = dict( foo=43, like=True  ),
        BLUE  = dict( foo=43, like=False ),
    )

    # __contains__
    assert Color.RED in Color.objects
    assert "RED"     in Color.objects

    # __getitem__
    assert Color.objects[ "RED" ] == Color.objects[ Color.RED ] == Color.RED

    # __len__
    assert len( Color.objects ) == 3

    # all
    assert Color.objects.all[ 0 ] == Color.RED

    # first
    assert Color.objects.first() == Color.RED

    # last
    assert Color.objects.last() == Color.BLUE

    # max_length
    assert Color.objects.max_length == 5

    # random
    assert Color.objects.random() in Color.objects

    # select
    assert len( Color.objects.select(                   ) ) == 3
    assert len( Color.objects.select( foo=42            ) ) == 1
    assert len( Color.objects.select( foo=99            ) ) == 0
    assert len( Color.objects.select( like=True         ) ) == 2
    assert len( Color.objects.select( like=False        ) ) == 1
    assert len( Color.objects.select( like=True, foo=43 ) ) == 1

    # filter
    assert len( Color.objects.filter( lambda o: o.like  ) ) == 2

    # get
    assert Color.objects.get( foo=42 ) == Color.RED
    try:
        Color.objects.get( foo=99 )
        assert False
    except ValueError as e:
        ...
