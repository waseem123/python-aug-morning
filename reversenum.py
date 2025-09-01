num = 456
temp = num
reverse = 0

while temp!=0:
    rem = temp % 10 #4
    reverse = (reverse * 10) + rem #654
    temp = temp // 10 #0
    
print(reverse)