def tribo(n):
    """
    Computes the n-th value of the Tribonacci sequence, a modified Fibonacci sequence
    where each term is the sum of the previous three terms.

    Args:
        n (int): The position in the Tribonacci sequence.

    Returns:
        int: The n-th Tribonacci number.
    """
    a, b, c = 1, 1, 1  # Initialize the first three values of the sequence
    if n < 4:  # Return 1 for the first three positions
        return 1
    for _ in range(3, n):  # Compute the Tribonacci number iteratively
        a, b, c = b, c, a + b + c
    return c

def main():
    """
    Prompts the user for an integer input and prints the corresponding Tribonacci number.
    If the user enters a non-positive integer, the program exits.
    """
    while True:
        try:
            n = int(input("Please enter the n-th value of the Tribonacci sequence: "))
            if n < 1:
                print("Program over.")
                exit()
            else:
                print(f"The {n}-th element of the Tribonacci sequence is {tribo(n)}.")
        except ValueError:
            print("Incorrect value, try again.")

if __name__ == "__main__":
    main()
