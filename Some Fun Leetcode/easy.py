x = 121
x_str = str(x)
x_len = len(str(x))
x_list = [x]
reverse = ""


# for i in x_len:
# print(x_len[-1])
# print(x_len[-2])
# print(x_len[-3])


for i in range(1, x_len + 1):
    reverse += x_str[-i]
if x_str == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
 
print(reverse)

    