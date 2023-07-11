"""
SciComp - Python library for scientific computing.

This is a Python docstring, we can use reStructuredText syntax here!

.. code-block:: python

    # Import scicomp
    import scicomp

    # Call its only function
    get_random_ingredients(kind=["cheeses"])
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""

    pass


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise scicomp.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["A", "B", "C"]
