# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def read_matrix(rows, cols, name="Matrix"):
    print(f"\nEntering values for {name} ({rows}*{cols}):")
    matrix = []
    for i in range(rows):
        while True:
            try:
                row_input = input(f"Enter row {i + 1}:").split()
                if len(row_input) != cols:
                    print(f"Error: Please enter exactly {cols} space seperated numbers.")
                    continue
                row = [int(val) for val in row_input]
                matrix.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
    return matrix

def display_matrix(matrix, title="Matrix"):
    print(f"\n{title}:")
    for row in matrix:
        for val in row:
            print(f"{val:5d}", end="")
        print()

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)

    return transposed

def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            sum_val = matrix_a[i][j] + matrix_b[i][j]
            row.append(sum_val)

        result.append(row)
        
    return result

def multiply_matrices(matrix_a, matrix_b):
    result = []
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            cell_sum = 0
            for k in range(cols_a):
                cell_sum += matrix_a[i][k] * matrix_b[k][j]
            row.append(cell_sum)
        result.append(row)

    return result

def main():
    print("===PART A: TRANSPOSE A MATRIX===")
    r = int(input("Enter number of rows: "))
    c = int(input("Enter numberr of columns: "))

    mat = read_matrix(r, c, "Original Matrix")
    display_matrix(mat, "Original Matrix")

    transposed = transpose(mat)
    display_matrix(transposed, "Transposed Matrix")

    print("\n" + "=" * 35)
    print("=== PART B: ADD TWO MATRICES===")
    r = int(input("Enter number of rows for matrices: "))
    c = int(input("Enter number of columns for matrices: "))

    mat_a = read_matrix(r, c, "Matrix A")
    mat_b = read_matrix(r, c, "Matrix B")

    display_matrix(mat_a, "Matrix A")
    display_matrix(mat_b, "Matrix B")

    added = add_matrices(mat_a, mat_b)
    display_matrix(added, "Sum (A + B)")

    print("\n" + "=" * 35)
    print("===PART C: MULTIPLY TWO MATRICES===")
    m = int(input("Enter rows for Matrix A (M): "))
    n = int(input("Enter columns for Matrix A / rows for Matrix B (N): "))
    p = int(input("Enter columns for Matrix B (P): "))

    mat_a = read_matrix(m, n, "Matrix A")
    mat_b = read_matrix(n, p, "Matrix B")

    display_matrix(mat_a, "Matrix A")
    display_matrix(mat_b, "Matrix B")

    product = multiply_matrices(mat_a, mat_b)
    display_matrix(product, "Product (A * B)")
if __name__ == "__main__":
    main()


