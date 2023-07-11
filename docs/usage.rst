Usage
=====

.. _installation:

Installation
------------

To use SciComp, first install it using pip:

.. code-block:: console

   (.venv) $ pip install scicomp

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``scicomp.get_random_ingredients()`` function:

.. autofunction:: scicomp.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`scicomp.get_random_ingredients`
will raise an exception.

.. autoexception:: scicomp.InvalidKindError

For example:

>>> import scicomp
>>> scicomp.get_random_ingredients()
['A', 'B', 'C']

