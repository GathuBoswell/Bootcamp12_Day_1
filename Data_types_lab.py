#data_types_lab.py
def data_type(param):
    if type(param) == str:
        return len(param)
    elif param == None:
        return 'no value'
    elif type(param) == bool:
        return param
    elif type(param) == int:
        if param < 100:
            return 'less than 100'
        elif param > 100:
            return 'more than 100'
        else:
            return 'equal to 100'
    elif type(param) == list:
        try:
            if param[2]:
                return param[2]
        except IndexError:
            return None
    elif type(param) in [dict, tuple, set]:
        return (param, ' is of ', (type(param)))
    return 'Unrecognized Data type'

print(data_type([1,2]))