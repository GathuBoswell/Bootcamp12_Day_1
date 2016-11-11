#data_types_lab.py
def data_type(test_data):
    if type(test_data) == str:
        return len(test_data)
    elif test_data == None:
        return 'no value'
    elif type(test_data) == bool:
        return test_data
    elif type(test_data) == int:
        if test_data < 100:
            return 'less than 100'
        elif test_data > 100:
            return 'more than 100'
        else:
            return 'equal to 100'
    elif type(test_data) == list:
        try:
            if test_data[2]:
                return test_data[2]
        except IndexError:
            return None
    elif type(test_data) in [dict, tuple, set]:
        return (test_data, ' is of ', (type(test_data)))
    return 'Unrecognized Data type'

print(data_type([1,2]))