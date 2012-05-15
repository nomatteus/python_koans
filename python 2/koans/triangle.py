#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    if a == 0 or b == 0 or c == 0:
        raise TriangleError("Sides can not be 0")
    if a < 0 or b < 0 or c < 0:
        raise TriangleError("Sides can not be negative")
    # check that the two smallest side (a and b) are less that longer side (c)
    # That is, a + b > 0    (this is a valid triangle)
    sides = [a, b, c]
    max_side = max(a, b, c)
    min_side = min(a, b, c)
    sides.remove(max_side)
    sides.remove(min_side)
    # The only one left is the mid value
    mid_side = sides[0]
    if not (min_side + mid_side) > max_side:
        raise TriangleError("Sides cannot form a valid triangle.")

    if a == b == c:
        return 'equilateral'
    elif a == b or b == c or c == a:
        return 'isosceles'
    else:
        return 'scalene'


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
