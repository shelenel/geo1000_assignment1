# GEO1000 -- Assignment 1 -- Point-in-Triangle Test
# Authors:
# Studentnumbers:

import math


def cross_product(x1, y1, x2, y2, px, py):
    """Calculates 2D cross product determinant for orientation test."""
    pass


def triangle_area(xa, ya, xb, yb, xc, yc):
    """Calculates and returns the area of triangle ABC."""
    pass


def point_in_triangle(xa, ya, xb, yb, xc, yc, px, py):
    """Determines whether point P is inside, outside, or on the boundary of triangle ABC."""
    pass


# Test execution calls
print(point_in_triangle(0, 0, 10, 0, 0, 10, 2, 2))   # Expected output: inside
print(point_in_triangle(0, 0, 10, 0, 0, 10, 12, 5))  # Expected output: outside
print(point_in_triangle(0, 0, 10, 0, 0, 10, 5, 0))   # Expected output: boundary
print(point_in_triangle(0, 0, 10, 0, 0, 10, 0, 0))   # Expected output: boundary
