class Point:
    """Represents a 2D point"""
    def __init__(self, x, y):
        self.x_cod = x
        self.y_cod = y
    
    def __str__(self):
        return f'<{self.x_cod}, {self.y_cod}>'
    
    def euclidean_distance(self, other):
        """Calculate distance between two points"""
        dx = self.x_cod - other.x_cod
        dy = self.y_cod - other.y_cod
        return (dx**2 + dy**2)**0.5
    
    def distance_from_origin(self):
        """Calculate distance from origin"""
        return (self.x_cod**2 + self.y_cod**2)**0.5

class Line:
    """Represents a line: Ax + By + C = 0"""
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
    
    def __str__(self):
        return f'{self.A}x + {self.B}y + {self.C} = 0'
    
    def point_on_line(self, point):
        """Check if point lies on line"""
        result = self.A * point.x_cod + self.B * point.y_cod + self.C
        return result == 0
    
    def shortest_distance(self, point):
        """Calculate shortest distance from point to line"""
        numerator = abs(self.A * point.x_cod + 
                       self.B * point.y_cod + self.C)
        denominator = (self.A**2 + self.B**2)**0.5
        return numerator / denominator

# Usage
p1 = Point(1, 2)
p2 = Point(4, 6)
print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"Distance: {p1.euclidean_distance(p2):.2f}")

line = Line(1, 1, -3)  # x + y - 3 = 0
print(f"Line: {line}")
print(f"Point on line: {line.point_on_line(p1)}")
print(f"Distance to line: {line.shortest_distance(p1):.2f}")