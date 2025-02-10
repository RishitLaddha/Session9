
# Polygon Class - Objective1.py

## Overview

The `Polygon` class in this Python script models polygons with a specific number of edges (vertices) and a circumradius, which is the distance from the polygon's center to any of its vertices. The class offers methods to compute several geometric properties of the polygon, including the number of edges, vertices, interior angle, edge length, apothem, area, and perimeter. It also provides comparison operations for equality and size between two polygons.

## Attributes

- **num_edges**: Represents the number of edges (or vertices) of the polygon.
- **circumradius**: Refers to the circumradius, which is the radius of the circle in which the polygon is inscribed.

## Methods

- **num_edges()**: Returns the number of edges of the polygon, which is also equal to the number of vertices in a regular polygon.
  
- **num_vertices()**: This method is synonymous with `num_edges()` and returns the number of vertices of the polygon.

- **interior_angle()**: Calculates the interior angle of the polygon. This is computed using the formula from the sum of interior angles of the polygon.

- **edge_length()**: Computes the length of each edge of the polygon. The length is derived from the circumradius using the formula leveraging basic trigonometric properties.

- **apothem()**: Calculates the apothem, which is the distance from the center of the polygon to the midpoint of any edge. 

- **area()**: Computes the area of the polygon using the formula for the area of a regular polygon.

- **perimeter()**: Computes the perimeter by multiplying the number of edges by the edge length, as the perimeter is simply the total length of all the edges.

## Comparison Methods

- **__eq__(self, other)**: This method allows for comparing two Polygon objects to see if they are equal. Two polygons are considered equal if they have the same number of edges and the same circumradius.

- **__gt__(self, other)**: Compares two Polygon objects to determine if the current polygon has more edges than the other. This comparison is based solely on the number of edges, and returns `True` if the current polygon has more edges.

## Usage

The `Polygon` class can be instantiated by specifying the number of edges and the circumradius. For example, to create a polygon with 5 edges and a circumradius of 10 units, you would instantiate the class as follows:

```python
polygon = Polygon(5, 10)
```

Once the polygon object is created, you can call any of the methods to compute the properties of the polygon. For instance:

- `polygon.num_edges()` will return the number of edges of the polygon.
- `polygon.area()` will return the area of the polygon.
- `polygon.perimeter()` will return the perimeter.

## Conclusion

The `Polygon` class is a comprehensive and straightforward tool for performing geometric calculations related to polygons with a given number of edges and circumradius. It offers methods for deriving key properties such as area, perimeter, and edge length, along with comparison functionality to assess the size or equality of different polygon objects.


# PolygonSequence Class - Objective2.py

## Overview

The `PolygonSequence` class generates a sequence of polygons with a specified maximum number of edges and circumradius. It provides methods to calculate key properties for the polygons in the sequence, as well as identify the polygon with the highest efficiency (maximum area-to-perimeter ratio).

## Attributes

- **max_edges**: The maximum number of edges for the largest polygon in the sequence.
- **circumradius**: The circumradius for all polygons in the sequence.
- **polygons**: A list of `Polygon` objects with edge counts ranging from 3 to `max_edges`.

## Methods

- **__init__(self, max_edges, circumradius)**: Initializes the sequence by generating polygons with edge counts from 3 up to `max_edges` and with the given circumradius. It raises a `ValueError` if `max_edges` is less than 3.

- **__len__(self)**: Returns the number of polygons in the sequence.

- **__getitem__(self, index)**: Allows index-based access to the polygons in the sequence.

- **max_efficiency_polygon(self)**: Finds and returns the polygon with the maximum area-to-perimeter ratio, which is considered the most efficient polygon.

- **__repr__(self)**: Provides a string representation of the `PolygonSequence` object for easy display.

## Usage

Let's go for example : `PolygonSequence(25, 10)`.

### **1. Understanding the Inputs**  
- **25** → This is the maximum number of sides a polygon in the sequence can have. The sequence starts from **3-sided (triangle)** and goes up to **25-sided (icosikaipentagon)**.  
- **10** → This is the **circumradius**, meaning every polygon in the sequence is inscribed in a circle of radius **10 units**.


### **2. What Happens Internally?**  
When we create `PolygonSequence(25, 10)`, the following polygons are generated:  
- A **triangle (3 sides)** with circumradius **10**  
- A **square (4 sides)** with circumradius **10**  
- A **pentagon (5 sides)** with circumradius **10**  
- A **hexagon (6 sides)** with circumradius **10**  
- …  
- Finally, a **25-sided polygon** (icosikaipentagon) with circumradius **10**  

Each of these polygons shares the same circumradius but has different **side lengths, areas, and perimeters**.



### **3. Accessing Elements (`__getitem__`)**  
Since `PolygonSequence` supports **indexing**, we can access individual polygons like:

```python
seq[1]  # Returns the square (4-sided polygon with circumradius 10)
seq[-1] # Returns the 25-sided polygon (circumradius 10)
```


### **4. Finding the Most Efficient Polygon (`max_efficiency_polygon`)**  
- Efficiency is measured by **area-to-perimeter ratio**.
- The higher the ratio, the more "efficient" the polygon is in enclosing space.
- Generally, as the number of sides increases, polygons become closer to a **circle**, which has the **maximum efficiency**.
- So, the **25-sided polygon** will likely be the most efficient.

```python
best_polygon = seq.max_efficiency_polygon()
print(best_polygon)
```

This will return the **polygon with the highest area-to-perimeter ratio** in the sequence.



### **5. Representation (`__repr__`)**  
When we print the object:

```python
print(seq)
```

It will output:

```
PolygonSequence(max_edges=25, circumradius=10)
```

This makes it easy to understand the **range of polygons** stored in the sequence.



### **Final Summary**  
For `PolygonSequence(25, 10)`, we have a **list of polygons** from **triangle (3 sides) to 25-sided polygon**, all with **circumradius 10**. The **polygon with the highest efficiency** is likely the one with the most sides, and we can access individual polygons using **indexing**.


## Conclusion

The `PolygonSequence` class allows easy manipulation and exploration of polygons with varying numbers of edges. Its functionality includes finding the polygon with the highest efficiency, providing both flexibility and insight into geometric properties.

#### **Testing the Implementation (`polygon_tests_notebook.py`)**
The `polygon_tests_notebook.py` script contains unit tests for verifying the correctness of the `Polygon` and `PolygonSequence` classes.

- **`test_polygon()`**  
  - Creates a **Polygon** with `n=5` edges and `circumradius=10`.
  - Computes **expected values** (interior angle, edge length, apothem, area, perimeter).
  - Uses `assert` statements to compare computed results with expected values.
  - If all assertions pass, it confirms that the `Polygon` class is working correctly.

- **`test_polygon_sequence()`**  
  - Creates a **PolygonSequence** with a maximum of **25 sides** and a circumradius of **10**.
  - Checks the total number of polygons.
  - Identifies the **most efficient polygon** based on the **area-to-perimeter ratio**.
  - Confirms that `PolygonSequence` is functioning correctly.

**To Run the Tests:**  
Simply execute the script in Python:
```python
test_polygon()
test_polygon_sequence()
```
If no assertion errors occur, the implementation is correct.
