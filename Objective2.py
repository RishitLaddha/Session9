from Objective1 import Polygon
class PolygonSequence:
    def __init__(self, max_edges: int, circumradius: float):
        if max_edges < 3:
            raise ValueError("Maximum number of edges must be at least 3.")
        self._max_edges = max_edges
        self._circumradius = circumradius
        self._polygons = [Polygon(i, circumradius) for i in range(3, max_edges + 1)]
    
    def __len__(self):
        return len(self._polygons)
    
    def __getitem__(self, index):
        return self._polygons[index]
    
    def max_efficiency_polygon(self):
        max_ratio = 0
        max_polygon = None
        for polygon in self._polygons:
            ratio = polygon.area() / polygon.perimeter()
            if ratio > max_ratio:
                max_ratio = ratio
                max_polygon = polygon
        return max_polygon
    
    def __repr__(self):
        return f"PolygonSequence(max_edges={self._max_edges}, circumradius={self._circumradius})"
