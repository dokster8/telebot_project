# программа вычисления арифметического выражения заданного строкой.
# Используются операции +,-,/,*. приоритет операций стандартный.
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;

def razlozhenie_stroki(some_string):            # Разбиение строки в список
    i = 0
    razlozhenie = []
    temp = ''
    while i < len(some_string):
        if some_string[i].isdigit():
            temp += some_string[i]
            # print(temp)
        else:
            if len(temp):
                razlozhenie.append(temp)
            razlozhenie.append(some_string[i])
            temp = ''
        i += 1
    if len(temp):
        razlozhenie.append(temp)
    # print(razlozhenie)
    return(razlozhenie)


def skobki(sl):                                 # Рекурсия для учёта скобок по всему списку
    demo_list = []
    if not len(sl):
        # print('not')
        return(sl)
    else:
        for j in range(0, len(sl)):
            print(sl[-(j+1)])
            if sl[-(j+1)] == '(':
                s = -(j+1)
                c = s + sl[-(j+1):].index(')')
                demo_list = [k for k in sl[:-(j+1)]]
                demo_list.append(
                    str(vichitanie(slozhenie(delenie(peremnozhenie(sl[s+1:c]))))[0]))
                demo_list += [k for k in sl[c+1:]]
                # print(s, c)
                # print(demo_list)
                return skobki(demo_list)
        return(sl)


def peremnozhenie(sl):                          # Рекурсия для перемножения по всему списку
    demo_list = []
    if not len(sl):
        # print('not')
        return(sl)
    else:
        for j in range(len(sl)):
            if sl[j] == '*':
                demo_list = [k for k in sl[:j-1]]
                demo_list.append(str(float(sl[j-1])*float(sl[j+1])))
                demo_list += [k for k in sl[j+2:]]
                # print(demo_list)
                return peremnozhenie(demo_list)
        return(sl)


def delenie(sl):                                # Рекурсия для деления по всему списку
    demo_list = []
    if not len(sl):
        # print('not')
        return(sl)
    else:
        for j in range(len(sl)):
            if sl[j] == '/':
                demo_list = [k for k in sl[:j-1]]
                demo_list.append(str(float(sl[j-1])/float(sl[j+1])))
                demo_list += [k for k in sl[j+2:]]
                # print(demo_list)
                return delenie(demo_list)
        return(sl)


def slozhenie(sl):                              # Рекурсия для сложения по всему списку
    demo_list = []
    if not len(sl):
        # print('not')
        return(sl)
    else:
        for j in range(len(sl)):
            if sl[j] == '+':
                demo_list = [k for k in sl[:j-1]]
                demo_list.append(str(float(sl[j-1])+float(sl[j+1])))
                demo_list += [k for k in sl[j+2:]]
                # print(demo_list)
                return slozhenie(demo_list)
        return(sl)


def vichitanie(sl):                             # Рекурсия для вычитания по всему списку
    demo_list = []
    if not len(sl):
        # print('not')
        return(sl)
    else:
        for j in range(len(sl)):
            if sl[j] == '-':
                demo_list = [k for k in sl[:j-1]]
                demo_list.append(str(float(sl[j-1])-float(sl[j+1])))
                demo_list += [k for k in sl[j+2:]]
                # print(demo_list)
                return vichitanie(demo_list)
        return(sl)


def calc_result(some_string):                   # Итоговое решение
    return vichitanie(slozhenie(delenie(peremnozhenie(skobki(razlozhenie_stroki(some_string))))))
