# Arithmetic Formatter

This project involves developing a Python function, `arithmetic_arranger()`, that arranges arithmetic problems vertically and side-by-side. The problems are provided as a list of strings, and the function has the option to display the answers as well.

## Getting Started

1. Import the project on Replit.
2. In the .replit window, select "Use run command" and click the "Done" button.

## Functionality

The function `arithmetic_arranger()` takes a list of strings as input, where each string represents an arithmetic problem. It arranges the problems vertically and side-by-side. Optionally, when the second argument is set to True, the answers are also displayed.

## Examples

### Example 1:

```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

**Output:**

```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

### Example 2:

```python
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

**Output:**

```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

## Rules and Error Handling

- The function returns an error if there are more than five problems supplied.
- Only addition and subtraction operators are accepted; others will result in an error.
- Operands should only contain digits; otherwise, an error is returned.
- Each operand has a max width of four digits; exceeding this will return an error.
- The conversion follows specific formatting rules for alignment and spacing.

## Development

Write your code in `arithmetic_arranger.py`. Use `main.py` for testing your `arithmetic_arranger()` function.

## Testing

Unit tests are in `test_module.py`. Run the tests by hitting the "run" button or inputting `pytest` in the console.

## Submission

Copy your project's URL and submit it to freeCodeCamp.