import math

def calculate_distance(point1, point2):
    """
    Calculate the Euclidean distance between two 3D points.

    Parameters:
    point1 (tuple): A tuple containing the (x, y, z) coordinates of the first point.
    point2 (tuple): A tuple containing the (x, y, z) coordinates of the second point.

    Returns:
    float: The Euclidean distance between the two points.
    """
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    # Euclidean distance formula
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    return distance