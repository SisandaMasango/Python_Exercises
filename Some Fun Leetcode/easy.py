x = input("Choose a number: ")
# x_str = str(x)
# x_len = len(x_str)
reverse = ""


# for i in x_len:
# print(x_len[-1])
# print(x_len[-2])
# print(x_len[-3])


for i in range(1, len(x) + 1):
    reverse += x[-i]
if x == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
 
print(reverse)

    