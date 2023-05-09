arrow_size = 5 
tail_size = 5

for i in range(arrow_size):
    print(' ' * (arrow_size-i-1) + '*' * (2*i+1))
for i in range(tail_size):
    print(' ' * (tail_size-1) + '*')
