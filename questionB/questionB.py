import ast

def equality(str1,str2):

    try:
        num1 = ast.literal_eval(str1)
        num2 = ast.literal_eval(str2)

    except SyntaxError:
        return 'non-number given'

    if num1 == num2:
        return str1 + ' and ' + str2 + ' are equal'
    elif num1 > num2:
        return str1 + ' is greater than ' + str2
    else:
        return str2 + ' is greater than ' + str1

if __name__ == '__main__':
    test1 = '1'
    test2 = '2'
    print(equality(test1,test2))

    test1 = '1.1'
    test2 = '2.2'

    test1 = '1L'
    test2 = '2L'
    print(equality(test1,test2))
