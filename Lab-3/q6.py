my_dict = {
    'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3',
    'key_4': 'value_4',
    'key_5': 'value_5'
}
remove_keys = ['key_1', 'key_3']
for key in remove_keys:
    del my_dict[key]

print(my_dict)