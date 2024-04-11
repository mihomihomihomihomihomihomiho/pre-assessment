def print_times_table_variant_1():
    # Creating the top header row
    header_row = "     "  # Initial spacing for the left header column
    for i in range(1, 13):
        header_row += f"{i:4}"  # Allocate 4 spaces for each number, adjusting for initial spacing
    print(header_row)
    
    # Printing the multiplication values
    for i in range(1, 13):
        row = f"{i:2} |"  # Allocate 2 spaces for the row label, followed by a separator
        for j in range(1, 13):
            row += f"{i*j:4}"  # Multiply and allocate 4 spaces for each product
        print(row)

# Call the function to display the times table
print_times_table_variant_1()
