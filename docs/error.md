# Error

A variation on the enum theme for Python exceptions.

### Defining Families

Declare a family of Exception classes in one line:

```
from simpleset import Error

APIError = Error.define_family( "APIError", "VersionError", "AuthenticationError" )

raise APIError( "..." )
raise APIError.VersionError( "..." )
```

Catch the most specific errors:

```python
try:
    ...
except APIError.VersionError as e:
    ...
```

Or the whole family, since VersionError is a subclass of APIError:

```python
try:
    ...
except APIError as e:
    ...
```

Or all errors defined with this module, since APIError is a subclass of Error:

```python
try:
    ...
except Error as e:
    ...
```

_Notice the difference &mdash; Constants are classes with instances attached, whereas Errors are classes with subclasses attached._

### Extending the Family

I assume `define_family` is enough for the vast majority of cases, but if for some reason you want to create a custom family tree with three or more levels, you can call `define_children` on any class to create another level of child error classes.

```python
APIError.VersionError.define_children( "VersionOmittedError", "VersionUnspportedError" )
```

### Cheatsheet

```python
cls.define_family( parent_name, *child_names )      # -> parent_class
cls.define_children( *child_names )                 # -> [ child_class1, ... ]

cls.<child_name>    # -> child_class

cls.name            # shortcut for cls.__name__
cls.parent          # -> parent_class
```
