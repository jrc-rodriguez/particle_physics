
x = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11]
y = [ 2, 4, 3, 7, 1, 29, 432, 45, 4832, 56, 532]
x_data = []
y_data = []

for i, j in zip(x, y):
    if i > 3 and i < 7:
        x_data.append(i)
        y_data.append(j)
        
print(x_data)
print(y_data)