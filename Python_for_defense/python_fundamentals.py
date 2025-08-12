# n = 2_147_483_648
# print(n.bit_length())
# print(hex(n))
# print(n.to_bytes(4, "big"))


def int_to_little_endian(n, length):
    return n.to_bytes(length, "little")

def almost_equal(a, b, rel_tol=1e-9, abs_tol=0.0):
    difference = abs(a-b)       # how far apart the numbers are. absoulte value, ignores results if negative and a - b is the difference between a and b
    biggest = max(abs(a), abs(b)) #larger between a and b and used to calculate relative tolerance
    relative_check = rel_tol * biggest # how much of a difference is acceptable for these sizes of numbers
    allowed_difference = max(relative_check, abs_tol) # choose the larger of the two tolerance options. 
    # it ensures that even near zero, we have some room for close enough
    #relative_check = 0.001
    #abs_tol = 0.0000001
    #allowed_difference = max(0.001, 0.0000001) = 0.001

    return difference <=  allowed_difference

# almost_equal(0.1 + 0.2, 0.3)
#difference ≈ 0.00000000000000004

#allowed difference = 1e-9

#Is 0.00000000000000004 <= 0.000000001 → ✅ Yes

#So it returns True

# payload = b"\x90" * 16 + b"/xcc"
# mutable = bytearray(payload)
# mutable[0] = 0xcc
# view = memoryview(mutable)[1:5]
# print(view)
# print(mutable[0])
# print(bin(0x100471b40))
# print(hex(0b100000000010001110001101101000000))

#XOR Basics
#XOR(exclusive OR) is a bitwise operation: a ^ b
#if two bits are the same, the result is 0; if different, the result is 1.

"""
data: a mutable bytearray.
key: an integer (between 0 and 255).
XOR each byte in data with key, and modify data in place
"""
def xor_bytes(data: bytearray, key: int):
    for i in range(len(data)):
        data[i] ^= key


original = bytearray(b"hello")
key = 42

print("Before XOR:", original)
xor_bytes(original, key)
print("After XOR: ", original)
#To decrypt:
xor_bytes(original, key)
print("Decrypt: ", original)