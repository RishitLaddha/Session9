import math

class Polygon:
    def __init__(self, num_edges: int, circumradius: float):
        self._num_edges = num_edges
        self._circumradius = circumradius
    
    def num_edges(self):
        return self._num_edges
    
    def num_vertices(self):
        return self._num_edges
    
    def interior_angle(self):
        return (self._num_edges - 2) * 180 / self._num_edges
    
    def edge_length(self):
        return 2 * self._circumradius * math.sin(math.pi / self._num_edges)
    
    def apothem(self):
        return self._circumradius * math.cos(math.pi / self._num_edges)
    
    def area(self):
        return (self.num_edges() * self.edge_length() * self.apothem()) / 2
    
    def perimeter(self):
        return self.num_edges() * self.edge_length()
    
    def __repr__(self):
        return f"Polygon(num_edges={self.num_edges()}, circumradius={self._circumradius})"
    
    def __eq__(self, other):
        if isinstance(other, Polygon):
            return self.num_edges() == other.num_edges() and self._circumradius == other._circumradius
        return False
    
    def __gt__(self, other):
        if isinstance(other, Polygon):
            return self.num_edges() > other.num_edges()
        return NotImplemented
