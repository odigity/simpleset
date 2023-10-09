# ErrorSet

A variation on the enum theme for Python exceptions.  Declare a family of Exception classes in one line:

    from objects import ErrorSet

    APIError = ErrorSet( "APIError", "CERTIFICATE_ERROR", "CONNECTION_ERROR", "VERSION_ERROR" )

    raise APIError( "..." )
    raise APIError.VERSION_ERROR( "..." )

Catch the most specific errors:

    try:
        ...
    except APIError.VERSION_ERROR as e:
        ...

Or the whole family:

    try:
        ...
    except APIError as e:
        ...

_Notice the difference &mdash; Objects are classes with instances attached, whereas ErrorSets are classes with subclasses attached._
