def square_sequence(limit):
    n = 1
    while n <= limit:
        yield n * n
        n += 1

for square in square_sequence(10): 
    print(square)
