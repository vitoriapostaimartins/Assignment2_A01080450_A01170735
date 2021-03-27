Assignment 2 : The Supply Chain
===================

## How it works
Start the program by running the `driver.py` module

A menu for the store should display choices for
1. **Process Orders**
2. **Check Inventory**
3. **Exit**

### Processing Orders
You will be prompted to enter a `.xlsx` file to read orders from, or
you may choose the default by entering `d`.

### Check Inventory
After processing orders, you can check the status of each item in the inventory.

### Exit
This prints all the orders placed into a daily transaction record `.txt` file and then exits the program.

## Features
### Requirements as outlined in the assignment:
- Display a user menu with the following actions: process web orders, check inventory, exit
- Read values from an Excel file to create Orders
- Factory methods for each holiday(Christmas, Halloween, Easter) that create the corresponding item types for that holiday
    - for Christmas`make_toy`: Santa's Workshop, for Halloween `make_toy` = RC Spider, etc.
- Use the appropriate factory classes and create methods to create Items from an Order if not enough stock
- Print the orders into a Daily Transaction txt file with name formatted as `DTR_DDMMYY_HHMM.txt`

### Error Handling
- Handle string inputs in menus that prompt a user for a number
- Negative or zero values in user menu
- Negative or zero values for Santa's Workshop dimensions & number of rooms, order number and quantity


#### InvalidDataError
- Exception for when any Item or Order has an invalid attribute
  - i.e. negative values, string for number values, blank values,duplicate order number
- The exception message is added to the printed daily transaction record to alert the user why the Order wasn't successful

## References
- Ascii Art from: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20