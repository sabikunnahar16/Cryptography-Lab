import numpy as np

input = "jagannathuniversity"
col = 4
reminder = len(input) % col
if reminder == 0:
    row = len(input) // col
else:
    row = (len(input) // col) + 1
array = np.array([["z"] * col] * row)

index = 0
for i in range(row):
    for j in range(col):
        if index < len(input):
            array[i][j] = input[index]
            index += 1
print(array)
array2 = np.transpose(array)
print(array2)
ciphertext = ""
for i in range(col):
    for j in range(row):
        if array2[i][j] != "z":
            ciphertext += array2[i][j]
print(ciphertext)