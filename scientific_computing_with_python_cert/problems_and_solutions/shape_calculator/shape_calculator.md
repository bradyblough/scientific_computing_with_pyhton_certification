# Shape Calculator

In this project, you will use object-oriented programming to create a `Rectangle` class and a `Square` class. The `Square` class will be a subclass of `Rectangle` and inherit methods and attributes.

## Getting Started

1. Import the project on Replit.
2. In the .replit window, select "Use run command" and click the "Done" button.

## Rectangle Class

The `Rectangle` class should be initialized with width and height attributes. It should contain the following methods:

- `set_width(width)`: Set the width attribute.
- `set_height(height)`: Set the height attribute.
- `get_area()`: Returns the area (width * height).
- `get_perimeter()`: Returns the perimeter (2 * width + 2 * height).
- `get_diagonal()`: Returns the diagonal ((width ** 2 + height ** 2) ** .5).
- `get_picture()`: Returns a string representing the shape using lines of "*". The number of lines should be equal to the height, and the number of "*" in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, return the string: "Too big for picture."
- `get_amount_inside(shape)`: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed-in shape could fit inside the shape (with no rotations).

If an instance of a `Rectangle` is represented as a string, it should look like: `Rectangle(width=5, height=10)`

## Square Class

The `Square` class should be a subclass of `Rectangle`. When a `Square` object is created, a single side length is passed in. The `__init__` method should store the side length in both the width and height attributes from the `Rectangle` class.

The `Square` class should be able to access the `Rectangle` class methods but should also contain a `set_side(side)` method. If an instance of a `Square` is represented as a string, it should look like: `Square(side=9)`

Additionally, the `set_width` and `set_height` methods on the `Square` class should set both the width and height.

## Usage Example

```python
rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```

The output should be:

```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```

## Development

Write your code in `shape_calculator.py`. For development, use `main.py` to test your `shape_calculator` functions. Click the "run" button, and `main.py` will run.

## Testing

The unit tests for this project are in `test_module.py`. We imported the tests to `main.py` for your convenience. The tests will run automatically when you hit the "run" button.

## Submission

Copy your project's URL and submit it to freeCodeCamp.