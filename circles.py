# GEO1000 -- Assignment 1 -- Circle Intersections
# Authors:
# Studentnumbers:

from math import sqrt


def center_distance(x1, y1, x2, y2):
    """Calculates and returns the Euclidean distance between two center points."""
    pass


def classify_circles(x1, y1, r1, x2, y2, r2):
    """Classifies and prints the spatial relationship between two circles."""
    pass


# Test execution calls
classify_circles(0.0, 0.0, 5.0, 10.0, 0.0, 3.0)  # Separate
classify_circles(0.0, 0.0, 5.0, 8.0, 0.0, 3.0)   # Touch externally
classify_circles(0.0, 0.0, 5.0, 3.0, 0.0, 4.0)   # Intersect (2 points)
classify_circles(0.0, 0.0, 5.0, 2.0, 0.0, 3.0)   # Touch internally
classify_circles(0.0, 0.0, 5.0, 1.0, 0.0, 2.0)   # Nested inside
classify_circles(0.0, 0.0, 5.0, 0.0, 0.0, 5.0)   # Identical
