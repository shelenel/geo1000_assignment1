# GEO1000 -- Assignment 1 -- Circle Intersections
# Authors: Shelene Low
# Studentnumbers: 6797687

from math import sqrt

# Epsilon tolerance value
eps = 1e-7

# Default error message for invalid inputs
error = "Invalid input(s). Function accepts only float inputs."

def center_distance(x1, y1, x2, y2):
    """Calculates and returns the Euclidean distance between two center points."""
    if not all(isinstance(v, float) for v in (x1, y1, x2, y2)): # Return error message for invalid inputs
        return error
    else:
        euclid_dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return euclid_dist

def classify_circles(x1, y1, r1, x2, y2, r2):
    """Classifies and prints the spatial relationship between two circles."""
    euclid_dist = center_distance(x1, y1, x2, y2)
    if not all(isinstance(v, float) for v in (x1, y1, r1, x2, y2, r2)): # Return error message for invalid inputs
        return error
    if euclid_dist < eps and abs(r1 - r2) < eps:
        print("Identical/coincident circles. There are infinite intersection points.")
    elif euclid_dist < eps and abs(r1 - r2) >= eps:
        print("Concentric and disjoint intersection. There are no intersection points.")
    elif euclid_dist > (r1 + r2 + eps):
        print("Separate (disjoint outside) circles. There are no intersection points.")
    elif abs(euclid_dist - (r1 - r2)) < eps:
        print("Two circles touch externally. There is 1 intersection point.")
    elif abs(r1 - r2) < euclid_dist < (r1 + r2):
        print("Two circles intersect. There are 2 intersection points.")
    elif abs(euclid_dist- abs(r1 - r2)) < eps:
        print("Two circles touch internally. There is 1 intersection point.")
    else:
        print("Two circles are nested inside each other. There are no intersection points.")


# Test execution calls
#classify_circles(0.0, 0.0, 5.0, 10.0, 0.0, 3.0)  # Separate
#classify_circles(0.0, 0.0, 5.0, 8.0, 0.0, 3.0)   # Touch externally
#classify_circles(0.0, 0.0, 5.0, 3.0, 0.0, 4.0)   # Intersect (2 points)
#classify_circles(0.0, 0.0, 5.0, 2.0, 0.0, 3.0)   # Touch internally
#classify_circles(0.0, 0.0, 5.0, 1.0, 0.0, 2.0)   # Nested inside
#classify_circles(0.0, 0.0, 5.0, 0.0, 0.0, 5.0)   # Identical


