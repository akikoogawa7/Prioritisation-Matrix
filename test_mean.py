
x = [10, 30, 30, 40, 80]
y = [10, 30, 30, 40, 80]


def avg_of_list(num_of_users, x_list, y_list):
    if len(x_list) and len(y_list) == num_of_users:
        x_avg = round(sum(x_list) / len(x_list), 2)
        y_avg = round(sum(y_list) / len(y_list), 2)
        return x_avg, y_avg
    else:
        print('Error! Has everyone voted or have you included the right number of voters?')

x, y = avg_of_list(5, x, y)
print(x, y)