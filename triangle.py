# GEO1000 -- Assignment 1 -- Point-in-Triangle Test
# Authors: Shelene Low
# Studentnumbers: 6797687

import math

# Epsilon tolerance value
eps = 1e-7

# Default error message for invalid inputs
error = "Invalid input(s). Function accepts only integer/float inputs."

def cross_product(x1, y1, x2, y2, px, py):
    """Calculates 2D cross product determinant for orientation test."""
    if not all(isinstance(v, (int, float)) for v in (x1, y1, x2, y2, px, py)): # Return error message for invalid inputs
        return error
    else:
        crossproduct_determinant = (x2 - x1)*(py - y1) - (y2 - y1)*(px - x1)
        return crossproduct_determinant

def triangle_area(xa, ya, xb, yb, xc, yc):
    """Calculates and returns the area of triangle ABC."""
    area = 1/2 * abs(cross_product(xa, ya, xb, yb, xc, yc))
    return area

def point_in_triangle(xa, ya, xb, yb, xc, yc, px, py):
    """Determines whether point P is inside, outside, or on the boundary of triangle ABC."""
    # --- Error message for invalid inputs --- #
    if not all(isinstance(v, (int, float)) for v in (xa, ya, xb, yb, px, py)):
        return error

    # --- Assumes one direction of triangle AB -> BC -> CA --- #
    ab = cross_product(xa,ya,xb,yb,px,py) # Cross product of points AB and P
    bc = cross_product(xb,yb, xc, yc, px, py) # Cross product of points BC and P
    ca = cross_product(xc, yc, xa, ya, px, py) # Cross product of points CA and P

    # --- Consider CW and CCW directions --- #
    # This is not exactly necessary since vertex ordering is consistent here, but in case we have triangles with mixed orientations...
    orientation = cross_product(xa, ya, xb, yb, xc, yc)
    if orientation < -eps: # if determinant is negative, triangle is clockwise
        ab, bc, ca = -ab, -bc, -ca # flip ordering of vertices

    # Set boolean flag
    has_zero = has_neg = has_pos = False

    if (abs(ab) <= eps) or (abs(bc) <= eps) or (abs(ca) <= eps):
        has_zero = True
    if (ab < -eps) or (bc < -eps) or (ca < -eps):
        has_neg = True
    if (ab > eps) or (bc > eps) or (ca > eps):
        has_pos = True

    if has_pos and has_neg:
        return("outside")
    elif has_zero:
        return("boundary")
    else:
        return("inside")


# Test execution calls
#print(point_in_triangle(0, 0, 10, 0, 0, 10, 2, 2))   # Expected output: inside
#print(point_in_triangle(0, 0, 10, 0, 0, 10, 12, 5))  # Expected output: outside
#print(point_in_triangle(0, 0, 10, 0, 0, 10, 5, 0))   # Expected output: boundary
#print(point_in_triangle(0, 0, 10, 0, 0, 10, 0, 0))   # Expected output: boundary

# Extra tests on another different triangle with different points
#print(point_in_triangle(3, 4, 1, 1, 4, 1, 3, 2))     # Expected output: inside
#print(point_in_triangle(3, 4, 1, 1, 4, 1, 2, -2))    # Expected output: outside
#print(point_in_triangle(3, 4, 1, 1, 4, 1, 2, 1))     # Expected output: boundary

# Test triangle_area function
#print(triangle_area(0, 0, 10, 0, 0, 10))    # Expected output: 50.0
#print(triangle_area(3, 4, 1, 1, 4, 1))      # Expected output: 4.5

