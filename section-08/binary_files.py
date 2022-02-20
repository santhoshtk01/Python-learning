# Program to read and write binary files in a basic way..

# # Creating a binary file and writing 1 to 15 `int` objects to it
# with open('binary', mode='bw') as binary_file:
#     for index in range(1, 16):
#         binary_file.write(bytes([index]))
#
# # Reading the written binary file and printing the data object in it..
# # TODO: Read the binary files in the form as we wrote it
# with open('binary', mode='br') as binaryFile:
#     for data in binaryFile:
#         print(data)


# Writing integer data and read back them as we stored..
# 65535 - 2bytes
values = [value for value in range(1000, 200000, 10000)]

with open('binary_int', mode='bw') as bin_file:
    for value in values:
        if value > 65535:
            length = 4
        else:
            length = 2
        bin_file.write(value.to_bytes(length, byteorder='big'))

# Reading the binary file the form as we written
with open('binary_int', mode='br') as binFile:
    value = int.from_bytes(binFile.read(2), 'big')
    while value:
        print(value)
        value = int.from_bytes(binFile.read(2), byteorder='big')

