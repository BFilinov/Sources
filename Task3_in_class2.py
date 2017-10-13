

# 2
def sort_int_array(*array):
    for i in array:
        try:
            int_i = int(i)
        except TypeError as ve:
            raise ValueError(ve.args)
    return  sorted(array)


try:
    print(sort_int_array(1,2,3,4,5, ' HELLO I AM A STRING LOL ^^'))
except ValueError as e:
    print('Unable to sort:', e.args)
print(sort_int_array(14, 22, 55, 23, 51, 123))

print('Zero')