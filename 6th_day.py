#write a programm to count spy numbers present in a list not use control flow use nested loops, L = [1124,132,91,67,34,321,27]
'''L = [1124,132,91,67,34,321,27]
count = 0
for num in L:
    sum_of_digits = 0
    product_of_digits = 1
    for digit in (L):
        sum_of_digits += (digit)
        product_of_digits *= (digit)
    if sum_of_digits == product_of_digits:
        count += 1
print("Number of spy numbers:", count) '''

L = [1124,132,91,67,34,321,27]
c = 0
for n in L:
    s = 0 
    p = 1
    while n>0:
        digit = n%10
        s += digit
        p *= digit

        n = n//10
    if s == p:
        c += 1
print(c) 