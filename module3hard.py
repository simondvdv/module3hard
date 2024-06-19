def sum_collection(collection):
    summator = 0
    print('start')
    for i in collection:
        print(i)
        match type_check(i):
            case 'list':
                summator += sum_list(i)
            case 'dict':
                pass
                print('dict')
            case 'str':
                summator += len(i)
            case 'int':
                summator += i
    return summator

def type_check(list_arg):
    if isinstance(list_arg, (list, set, tuple)):
        return 'list'
    elif isinstance(list_arg, dict):
        return 'dict'
    elif isinstance(list_arg, str):
        return 'str'
    else:
        return 'int'


def sum_list(list_):
    summator = 0
    for i in list_:
        if isinstance(i, int):
            summator += i
        elif isinstance(i, str):
            summator += len(i)
        else:
            sum_collection(i)
    return summator


def sum_dict(dict_):
    summator = 0

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
#sum_collection(data_structure)
test = [1, 2, [4, 5], 'qwert', 3]
print(sum_collection(test))


