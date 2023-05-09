num_rows = 7
mid_row = num_rows // 2

# upper part of the star
for i in range(mid_row):
    spaces = " " * (mid_row - i)
    stars = "*" * (i * 2 + 1)
    print(spaces + stars)

# middle row of the star
print("*" * num_rows)

# lower part of the star
for i in range(mid_row):
    spaces = " " * (i + 1)
    stars = "*" * ((mid_row - i) * 2 - 1)
    print(spaces + stars)
