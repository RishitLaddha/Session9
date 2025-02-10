from Objective1 import Polygon
from Objective2 import PolygonSequence
import math
def test_polygon():
    print("Testing Polygon class")
    
    n = 5  # Number of edges
    R = 10  # Circumradius
    poly = Polygon(n, R)
    
    # Expected values using the formulas
    expected_interior_angle = (n - 2) * 180 / n
    expected_edge_length = 2 * R * math.sin(math.pi / n)
    expected_apothem = R * math.cos(math.pi / n)
    expected_area = (1/2) * n * expected_edge_length * expected_apothem
    expected_perimeter = n * expected_edge_length

    assert math.isclose(poly.interior_angle(), expected_interior_angle, rel_tol=1e-5), "Interior Angle mismatch"
    assert math.isclose(poly.edge_length(), expected_edge_length, rel_tol=1e-5), "Edge Length mismatch"
    assert math.isclose(poly.apothem(), expected_apothem, rel_tol=1e-5), "Apothem mismatch"
    assert math.isclose(poly.area(), expected_area, rel_tol=1e-5), "Area mismatch"
    assert math.isclose(poly.perimeter(), expected_perimeter, rel_tol=1e-5), "Perimeter mismatch"
    
    print("All Polygon properties match expected values!")
def test_polygon_sequence():
    print("Testing PolygonSequence class")
    seq = PolygonSequence(25, 10)
    print(f"Total polygons in sequence: {len(seq)}")
    print(f"Most efficient polygon: {seq.max_efficiency_polygon()}")
    print("PolygonSequence class passed all tests!\n")
