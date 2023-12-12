# Budget Tracker

This project involves completing the `Category` class in `budget.py`, which is designed to instantiate objects based on different budget categories such as food, clothing, and entertainment. The class should have various methods to handle deposits, withdrawals, transfers, and balance checking.

## Getting Started

1. Import the project on Replit.
2. In the .replit window, select "Use run command" and click the "Done" button.

## Category Class

Complete the `Category` class in `budget.py` with the following methods:

- **deposit(amount, description='')**: Appends a deposit object to the ledger list.
- **withdraw(amount, description='')**: Appends a withdrawal object to the ledger list, stored as a negative number. Returns True if the withdrawal took place, False otherwise.
- **get_balance()**: Returns the current balance of the budget category.
- **transfer(amount, budget_category)**: Adds a withdrawal and deposit for a transfer between budget categories. Returns True if the transfer took place, False otherwise.
- **check_funds(amount)**: Returns False if the amount is greater than the balance, and True otherwise.

When printing a budget object, the output should include a title line, a list of ledger items, and a line displaying the category total.

## Example Output:

```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

## create_spend_chart Function

Create a function `create_spend_chart(categories)` outside the class. It takes a list of categories as an argument and returns a string representing a bar chart showing the percentage spent in each category. The chart should have labels, bars made of "o" characters, and category names written vertically below the bars.

## Example Output:

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

## Development

Write your code in `budget.py`. For development, use `main.py` to test your `Category` class. Click the "run" button, and `main.py` will run.

## Testing

The unit tests for this project are in `test_module.py`. We imported the tests to `main.py` for your convenience. The tests will run automatically when you hit the "run" button.

## Submission

Copy your project's URL and submit it to freeCodeCamp.