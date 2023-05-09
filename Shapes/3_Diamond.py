num_rows = 7
mid_row = num_rows // 2

for i in range(mid_row):
    spaces = " " * (mid_row - i)
    stars = "*" * (i * 2 + 1)
    print(spaces + stars)

print("*" * num_rows)

for i in range(mid_row):
    spaces = " " * (i + 1)
    stars = "*" * ((mid_row - i) * 2 - 1)
    print(spaces + stars)
