"""
Use the triangle class to represent triangles.
"""

from math import sqrt

class Triangle(object):
    """
    A :class:`~trianglelib.shape.Triangle` object is a three-sided polygon.

    You instantiate a :class:`~trianglelib.shape.Triangle` by providing exactly three lengths ``a``, ``b``, and ``c``.

    They can either be intergers or floating-point numbers, and should be listed clockwise around the triangle.

    If the three lengths *cannot* make a valid triangle, then ``ValueError`` will be raised instead.

    >>> from trianglelib.shape import Triangle
    >>> t = Triangle(3, 4, 5)
    >>> print(t.is_equilateral())
    False
    >>> print(t.area())
    6.0

    Triangles support the following attributes, operators, and methods.

    .. attribute:: a
                   b
                   c



        Returns true if the two triangles have sides of the same lengths,
        in the same order.
        Note that it is okay if the two triangles
        happen to start their list of sides at a different corner;
        ``3,4,5`` is the same triangle as ``4,5,3``
        but neither of these are the same triangle
        as their mirror image ``5,4,3``.
    """

    def __init__(self, a, b, c):
        """
        Create a :class:`~trianglelib.shape.Triangle` object with sides of lengths `a`, `b`, and `c`.

        Raises `ValueError` if the three length values provided cannot
        actually form a triangle.

        :param a: side length one
        :type a: :class:`float`
        :param b: side length two
        :type b: :class:`float`
        :param c: side length three
        :type c: :class:`float`
        :raises ValueError: side lengths must all be positive
        :raises ValueError: one side is too long to make a triangle
        """
        self.a, self.b, self.c = float(a), float(b), float(c)
        if any( s <= 0 for s in (a, b, c) ):
            raise ValueError('side lengths must all be positive')
        if any( a >= b + c for a, b, c in self._rotations() ):
            raise ValueError('one side is too long to make a triangle')

    def is_equivalent(self, triangle):
        """
        Return whether this triangle equals another triangle.

        :param triangle: another :class:`~trianglelib.shape.Triangle` object
        :type triangle: :class:`~trianglelib.shape.Triangle`
        :return: whether the two :class:`~trianglelib.shape.Triangle` objects are equivalent
        :rtype: :class:`bool`
        """
        return self == triangle

    def is_similar(self, triangle):
        """
        Return whether this :class:`~trianglelib.shape.Triangle` object is similar to another triangle.

        :param triangle: another :class:`~trianglelib.shape.Triangle` object
        :type triangle: :class:`~trianglelib.shape.Triangle`
        :return: whether the two :class:`~trianglelib.shape.Triangle` objects are similar
        :rtype: :class:`bool`
        """
        return any( (self.a / a == self.b / b == self.c / c)
                    for a, b, c in triangle._rotations() )