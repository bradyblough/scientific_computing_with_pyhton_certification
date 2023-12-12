# Probability Calculator

In this project, you will create a program to estimate the approximate probability of drawing certain balls randomly from a hat. Follow the instructions below to complete the project.

## Getting Started

1. Import the project on Replit.
2. In the .replit window, select "Use run command" and click the "Done" button.

## Hat Class

Create a `Hat` class in `prob_calculator.py`. The class should take a variable number of arguments specifying the number of balls of each color in the hat. For example:

```python
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
```

The `Hat` class should have a `draw` method that accepts the number of balls to draw and removes balls at random from the hat without replacement. The method should return the drawn balls as a list of strings.

## Experiment Function

Create an `experiment` function in `prob_calculator.py` (outside the `Hat` class). The function should accept the following arguments:

- `hat`: A hat object containing balls that should be copied inside the function.
- `expected_balls`: An object indicating the exact group of balls to attempt to draw from the hat for the experiment.
- `num_balls_drawn`: The number of balls to draw out of the hat in each experiment.
- `num_experiments`: The number of experiments to perform.

The `experiment` function should return the estimated probability.

## Example Usage

```python
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                          expected_balls={"red":2,"green":1},
                          num_balls_drawn=5,
                          num_experiments=2000)
```

## Development

Write your code in `prob_calculator.py`. Use `main.py` for testing your `Hat` class and `experiment` function. Click the "run" button, and `main.py` will run.

## Testing

The unit tests for this project are in `test_module.py`. We imported the tests to `main.py` for your convenience. The tests will run automatically when you hit the "run" button.

## Submission

Copy your project's URL and submit it to freeCodeCamp.