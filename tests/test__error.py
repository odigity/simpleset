from simpleset import Error


PError  = Error.define_family( "PError", "CError1", "CError2" )
CError1 = PError.CError1

CError1.define_children( "GError1", "GError2" )     # grandchildren of PError
GError1 = CError1.GError1


def test__error__family():
    assert issubclass( PError, Error )
    assert PError.name == "PError"
    assert PError.parent is Error

    assert issubclass( CError1, PError )
    assert CError1.name == "CError1"
    assert CError1.parent is PError

    # test catching error
    try:
        raise CError1( "oh no" )
    except CError1 as e:
        ...

    # test catching parent via parent
    try:
        raise CError1( "oh no" )
    except PError as e:
        ...

    # test catching error via root class
    try:
        raise CError1( "oh no" )
    except Error as e:
        ...


def test__error__grandchildren():
    assert issubclass( GError1, CError1 )
    assert GError1.name == "GError1"
    assert GError1.parent is CError1
