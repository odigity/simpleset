from objects.errorset import BaseError, ErrorSet


def test__errorset():
    FooError = ErrorSet( "FooError", "ERROR1", "ERROR2" )

    assert issubclass( FooError,        BaseError )
    assert issubclass( FooError.ERROR1, FooError  )
    assert FooError.errors[ "ERROR1" ] is FooError.ERROR1

    try:
        raise FooError.ERROR1( "oh no" )
    except FooError as e:
        ...
