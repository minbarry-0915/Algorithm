N = int(input())

def calculate_dots(N):
    initial_dots_in_row = 2
    total_dots_in_row = initial_dots_in_row
    for _ in range(N):
        total_dots_in_row = total_dots_in_row + (total_dots_in_row - 1)

    return (total_dots_in_row) ** 2
print(calculate_dots(N))
