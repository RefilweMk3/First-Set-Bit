def rightmost_set_bit_position(n):
    if n == 0:
        return -1 
    position = 1  
    while (n & 1) == 0: 
        n = n >> 1 
        position += 1  

    return position

number = int(input("Enter number: "))
position = rightmost_set_bit_position(number)

if position == -1:
    print("There are no set bits in the number.")
else:
    print("Position of the first set bit:", position)
