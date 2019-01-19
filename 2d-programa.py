def find_max(nums):
    max_num = float(0)
    for num in nums:
        if num > max_num:            
            print('{} es mayor que {}' .format(num, max_num))                
            max_num = num            
        else:
            print(f'{num} es menor que {max_num}')                
    return max_num

l1 = [9,1,22,3,4,5]
print(f'El numero Mayor es: {find_max(l1)}')