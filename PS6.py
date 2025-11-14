"""
    Course     : CMPSC 131, Fall 2025
    File       : PS6.py 

    Name       : Devin Myers 
    GitHub User:  DM5706
    Collaboration Statement: N/A
"""

#-YOUR CODE STARTS HERE  (TODO) 
#Q1

def ensure_min_salary(wages, min_salary):
    """
    Enforces a minimum salary floor across all teams.
    Modifies the wages list in place.
    
    Args:
        wages: 2D list where each inner list is a team's hourly wages
        min_salary: minimum hourly wage floor
    """
    
    for i in range(len(wages)):
        
        for j in range(len(wages[i])):
         
            if wages[i][j] < min_salary:
                wages[i][j] = min_salary

#Q2
def inventory_totals(filename):
    """
    Reads a CSV file and returns the sum of each row, rounded to 2 decimals.
    
    Returns:
        List of floats, each representing the sum of a row rounded to 2 decimals
    """
    totals = []  
    

    with open(filename, 'r') as file:

        for line in file:

            values = line.strip().split(',')
            
            row_sum = 0
            for value in values:
                row_sum += float(value)
            
            rounded_sum = round(row_sum, 2)
            totals.append(rounded_sum)
    
    return totals

#Q3
def sensor_sums(filename):
    """
    Reads a CSV file and returns the sum of each column (sensor), rounded to 2 decimals.
    Handles missing data where rows may have different lengths.
    
    
    Returns:
        List of floats, each representing the sum of a column rounded to 2 decimals
    """

    data = []
    with open(filename, 'r') as file:
        for line in file:

            row = []
            values = line.strip().split(',')
            for value in values:
                if value:  
                    row.append(float(value))
            data.append(row)
    

    max_cols = 0
    for row in data:
        if len(row) > max_cols:
            max_cols = len(row)
    
    totals = []
    for col in range(max_cols):
        col_sum = 0
        for row in data:
            if col < len(row):  
                col_sum += row[col]
        

        rounded_sum = round(col_sum, 2)
        totals.append(rounded_sum)
    
    return totals

#Part 2 
#2.1
def daily_sales_summary(filename):
    """
    Reads a sales CSV file and returns a summary of valid sales.
    
    Returns:
        Tuple of (count, total_revenue):
    """
    valid_count = 0
    total_revenue = 0.0
    

    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                parts = line.strip().split(',')
                
                if len(parts) >= 2:
                    item = parts[0].strip() 
                    price_str = parts[1].strip() 
                    
                
                    if item and price_str:
                        price = float(price_str)
                        valid_count += 1
                        total_revenue += price
    
    total_revenue = round(total_revenue, 2)
    
    return (valid_count, total_revenue)

#2.2
def sum_row(matrix, row_index):
    """
    Returns the sum of a specific row in the matrix.
    """
    row_sum = 0
    for value in matrix[row_index]:
        row_sum += value
    return row_sum


def sum_column(matrix, col_index):
    """
    Returns the sum of a specific column in the matrix.
    """
    col_sum = 0
    for row in matrix:
        col_sum += row[col_index]
    return col_sum


def sum_main_diagonal(matrix):
    """
    Returns the sum of the main diagonal 
    The main diagonal is where row index = column index.
    """
    diag_sum = 0
    n = len(matrix)
    for i in range(n):
        diag_sum += matrix[i][i]
    return diag_sum


def sum_anti_diagonal(matrix):
    """
    Returns the sum of the anti-diagonal 
    The anti-diagonal is where row index + column index = n - 1.
    """
    diag_sum = 0
    n = len(matrix)
    for i in range(n):
        diag_sum += matrix[i][n - 1 - i]
    return diag_sum


def is_magic_square(filename):
    """
    Reads a file containing a square matrix and determines if it's a magic square.
    
    Returns:
        True if the matrix is a magic square, False otherwise
    """
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = []
            values = line.strip().split(',')
            for value in values:
                if value:
                    row.append(int(value))
            matrix.append(row)
    
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return False  
    
   
    magic_constant = sum_row(matrix, 0)
    
    for i in range(n):
        if sum_row(matrix, i) != magic_constant:
            return False
    
    for j in range(n):
        if sum_column(matrix, j) != magic_constant:
            return False
    
    if sum_main_diagonal(matrix) != magic_constant:
        return False
    
    if sum_anti_diagonal(matrix) != magic_constant:
        return False
    
    return True

#2.3
def buy_ticket(filename, seat):
    seats = []
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                row = line.strip().split(' ')
                if row:
                    seats.append(row)
    
    row_letter = seat[0]
    col_number = seat[1:]
    
    if ord(row_letter) >= ord('a') and ord(row_letter) <= ord('z'):
        row_letter = chr(ord(row_letter) - 32)
    
    
    row_index = ord(row_letter) - ord('A')
    
    
    col_index = int(col_number) - 1
    
  
    if row_index < 0 or row_index >= len(seats):
        return False
    
   
    if col_index < 0 or col_index >= len(seats[row_index]):
        return False
    
   
    if seats[row_index][col_index] != 'O':
        return False
    
    seats[row_index][col_index] = 'X'
    
    with open(filename, 'w') as file:
        for i in range(len(seats)):
            line = ' '.join(seats[i])
            file.write(line)
            if i < len(seats) - 1:
                file.write('\n')
    
    return True

################################################################################

def main():
    # YOUR ASSERTIONS TO TEST ALL YOUR FUNCTIONS STARTS HERE
    
    wages1 = [[15.0, 22.5], [10.0, 30.0, 18.0]]
    print(f"Before: {wages1}")
    ensure_min_salary(wages1, 20.0)
    print(f"After: {wages1}")
    print(f"Expected: [[20.0, 22.5], [20.0, 30.0, 20.0]]")
    
    with open('test_quantities.csv', 'w') as f:
        f.write("3.25,1.50,2.10\n")
        f.write("10\n")
        f.write("5.0,2.0\n")
        f.write("0.99,1.01,1.00,0.50")
    
    result = inventory_totals('test_quantities.csv')
    print(f"Result: {result}")
    print(f"Expected: [6.85, 10.0, 7.0, 3.5]")
    
    

    with open('test_sensors.csv', 'w') as f:
        f.write("5.0,1.0,2.0\n")
        f.write("1.0,2.0\n")
        f.write("0.5,0.5,0.5")
    
    result = sensor_sums('test_sensors.csv')
    print(f"Result: {result}")
    print(f"Expected: [6.5, 3.5, 2.5]")    
    
    
    with open('test_magic.txt', 'w') as f:
        f.write("2,7,6\n")
        f.write("9,5,1\n")
        f.write("4,3,8")
    
    result = is_magic_square('test_magic.txt')
    print(f"Magic square result: {result}")
    print(f"Expected: True")
    
    with open('test_not_magic.txt', 'w') as f:
        f.write("1,2,3\n")
        f.write("4,5,6\n")
        f.write("7,8,9")
    
    result = is_magic_square('test_not_magic.txt')
    print(f"Non-magic square result: {result}")
    print(f"Expected: False")
    
    

    with open('test_sales.csv', 'w') as f:
        f.write("latte,4.50\n")
        f.write("cappuccino,5.00\n")
        f.write(",\n")
        f.write("espresso,2.50\n")
        f.write("tea,")
    
    result = daily_sales_summary('test_sales.csv')
    print(f"Result: {result}")
    print(f"Expected: (3, 12.0)")
    
    
    with open('test_seats.txt', 'w') as f:
        f.write("X O O X X\n")
        f.write("O O O X O X X X X X X\n")
        f.write("X X X X X X X\n")
        f.write("X X X X X X X\n")
        f.write("O O X X O X")
    
    result1 = buy_ticket('test_seats.txt', 'a1')
    print(f"buy_ticket('test_seats.txt', 'a1'): {result1}")
    
    result2 = buy_ticket('test_seats.txt', 'B3')
    print(f"buy_ticket('test_seats.txt', 'B3'): {result2}")
    
    result3 = buy_ticket('test_seats.txt', 'A10')
    print(f"buy_ticket('test_seats.txt', 'A10'): {result3}")
    print()


if __name__ == "__main__":
    main()