def sum_collection(collection):
    summator = 0
    for i in collection:
        print(f'элемент: {i} _______ сумма:{summator}')
        match type_check(i):
            case 'list':
                summator += sum_list(i)
                print('list')
            case 'dict':
                summator += sum_dict(i)
                print('dict')
            case 'str':
                summator += len(i)
                print('str')
            case 'int':
                summator += i
                print('int')
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
        elif isinstance(i, dict):
            summator += sum_dict(i)
        else:
            return summator + sum_list(i)
    return summator


def sum_dict(dict_):
    summator = 0
    for key, value in dict_.items():
        print(key)
        print(value)
        summator += len(key)
        summator += value
    return summator


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
answer = sum_collection([[1, 2, 3], {'a': 4, 'b': 5}])
answer = sum_collection(data_structure)
print(answer)

print(type(()))