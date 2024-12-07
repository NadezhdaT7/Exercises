immutable_var = 1, 2, 3, 4, True, 'string'
print(immutable_var)
#immutable_var[0] = 2 - операция недопустима, т.к. кортеж - неизменяемый тип данных
#print(immutable_var)
mutable_list = [1, 2, 5, False, 'apple']
mutable_list[0] = 9
mutable_list[4] = 'pineapple'
print(mutable_list)