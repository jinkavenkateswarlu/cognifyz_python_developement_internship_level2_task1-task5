def fibonacci_sequence(num_terms):
    sequence = [0, 1]

    for i in range(2, num_terms):
        next_term = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_term)

    return sequence

num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    print(fibonacci_sequence(num_terms))
