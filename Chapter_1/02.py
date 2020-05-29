input1 = "1.0"
input2 = "1.1.99"

array1 = input1.split(".")
array2 = input2.split(".")

for i in range(len(array1)):
    if int(array1[i]) > int(array2[i]):
        print(input1 + " > " + input2)
        break
    elif int(array1[i]) < int(array2[i]):
        print(input2 + " > " + input1)
        break
