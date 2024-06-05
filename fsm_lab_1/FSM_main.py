def security_input():
    x = input("Введите 1 или 0: ")
    if x in (1, 0, '1', '0'):
        return x
    else:
        print("Введено неверное значение...")
        security_input()
def len_content_and_index_checker(content = '', index=0):
    if index >= len(content):
        return True
    else:
        return False
def op_line_debugger(string_line=''):
    new_line = ''
    for i in string_line:
        if i in ('0', '1'):
            new_line += i
    return new_line
def fsm_string(state = 0):                      #fsm == Finite State Machine
    def GDG(x):                                 #Graphical Display of the Graph state history 
        for i in range(len(x)):
            if (i != len(x)-1):
                print(f"{x[i]} ->", end=" ")
            else:
                print(f"{x[i]}")
    content = ""
    index = 0
    while True:
        print("Введите строку операндов")
        content = input()
        if (len(content) > 0):
            break
        else:
            print("Попробуйте ввести ещё раз...")
            continue
    content = op_line_debugger(content)
    print("Вариант №6")                   
    Y0, Y1, Y2, Y3, Y4, Y5 = (0, 1, 2, 3, 4, 5)
    list_of_states = list() 
    while True:
        print(f"Текущее состояние автомата: Y{state}")
        if (index >= len(content)):
            GDG(list_of_states)
            print("Конец работы автомата, операции кончились...")
            break
        if (state == Y0):
            list_of_states.append('Yн')
            print("Прохождение через Y1")
            state = Y1
        elif (state == Y1):
            list_of_states.append('Y1')
            print("Прохождение через Y2")
            state = Y2
        elif (state == Y2):
            list_of_states.append('Y2')
            if ( content[index] == '1'):
                print("X1 = 1")
                index += 1
                if (len_content_and_index_checker(content, index)):
                    continue
                if (content[index] == '1'):
                    print("X2 = 1")
                    index += 1
                    state = Y1
                else:
                    print("X2 = 0")
                    if (len_content_and_index_checker(content, index)):
                        continue
                    if (content[index] == '1'):
                        print("X3 = 1")
                        index += 1
                        print("Прохождение через Y4")
                        state = Y4
                    else:
                        print("X3 = 0")
                        index += 1
                        print("Прохождение через Y3")
                        state = Y3
            else:
                print("X1 = 0")
                index += 1
                state = Y0
        elif (state == Y3):
            list_of_states.append('Y3')
            if (len_content_and_index_checker(content, index)):
                    continue
            if (content[index] == '1'):
                print("X4 = 1")
                index += 1
                print("Прохождение через Y5")
                state = Y5
            else:
                print("X4 = 0")
                index += 1
                state = Y3
        elif (state == Y4):
            list_of_states.append('Y4')
            if (len_content_and_index_checker(content, index)):
                continue
            if (content[index] == '1'):
                print("X4 = 1")
                index += 1
                print("Прохождение через Y5")
                state = Y5
            else:
                print("X4 = 0")
                index += 1
                print("Прохождение через Y3")
                state = Y3
        else:                                                   #state == Y5\
            list_of_states.append('Yк')
            print("Конечное состояние!")
            GDG(list_of_states)
            break            
def fsm_file(state = 0): #fsm == Finite State Machine
    def GDG(x): #Graphical Display of the Graph state history 
        for i in range(len(x)):
            if (i != len(x)-1):
                print(f"{x[i]} ->", end=" ")
            else:
                print(f"{x[i]}")

    content = ""
    index = 0
    while True:
        try:
            file = open(r'C:\text.txt', 'r')
            content = "".join([i.strip() for i in file.read()])
            content = op_line_debugger(content)
            file.close()
            break
        except FileNotFoundError:
            print("Не нашёлся файл с названием text.txt")
            break
        except:
            print("Ошибка во время открытия файла или чего нибудь ещё...")
            break
        finally:
            file.close()
            break
    print("Вариант №6")                   
    Y0, Y1, Y2, Y3, Y4, Y5 = (0, 1, 2, 3, 4, 5)
    list_of_states = list() 
    while True:
        print(f"Текущее состояние автомата: Y{state}")
        if (index >= len(content)):
            GDG(list_of_states)
            print("Конец работы автомата, операции кончились...")
            break
        if (state == Y0):
            list_of_states.append('Yн')
            print("Прохождение через Y1")
            state = Y1
        elif (state == Y1):
            list_of_states.append('Y1')
            print("Прохождение через Y2")
            state = Y2
        elif (state == Y2):
            list_of_states.append('Y2')
            if ( content[index] == '1'):
                print("X1 = 1")
                index += 1
                if (len_content_and_index_checker(content, index)):
                    continue
                if (content[index] == '1'):
                    print("X2 = 1")
                    index += 1
                    state = Y1
                else:
                    print("X2 = 0")
                    if (len_content_and_index_checker(content, index)):
                        continue
                    if (content[index] == '1'):
                        print("X3 = 1")
                        index += 1
                        print("Прохождение через Y4")
                        state = Y4
                    else:
                        print("X3 = 0")
                        index += 1
                        print("Прохождение через Y3")
                        state = Y3
            else:
                print("X1 = 0")
                index += 1
                state = Y0
        elif (state == Y3):
            list_of_states.append('Y3')
            if (len_content_and_index_checker(content, index)):
                    continue
            if (content[index] == '1'):
                print("X4 = 1")
                index += 1
                print("Прохождение через Y5")
                state = Y5
            else:
                print("X4 = 0")
                index += 1
                state = Y3
        elif (state == Y4):
            list_of_states.append('Y4')
            print("Прохождение через X4")
            if (len_content_and_index_checker(content, index)):
                continue
            if (content[index] == '1'):
                index += 1
                print("Прохождение через Y5")
                state = Y5
            else:
                index += 1
                print("Прохождение через Y3")
                state = Y3
        else:                                                   #state == Y5\
            list_of_states.append('Yк')
            print("Конечное состояние!")
            GDG(list_of_states)
            break            
def main_fsm(state = 0): #fsm == Finite State Machine
    def GDG(x): #Graphical Display of the Graph state history 
        for i in range(len(x)):
            if (i != len(x)-1):
                print(f"{x[i]} ->", end=" ")
            else:
                print(f"{x[i]}")
    Y0, Y1, Y2, Y3, Y4, Y5 = (0, 1, 2, 3, 4, 5)
    list_of_states = list() 
    print("Вариант №6")
    while True:
        print(f"Текущее состояние автомата: Y{state}")
        if (state == Y0):
            list_of_states.append('Yн')
            print("Прохождение через Y1")
            state = Y1
        elif (state == Y1):
            list_of_states.append('Y1')
            print("Прохождение через Y2")
            state = Y2
        elif (state == Y2):
            list_of_states.append('Y2')
            if ( security_input() == '1'):
                print("X1 = 1")
                if (security_input() == '1'):
                    print("X2 = 1")
                    state = Y1
                else:
                    print("X2 = 0")
                    if (security_input() == '1'):
                        print("X3 = 1")
                        print("Прохождение через Y4")
                        state = Y4
                    else:
                        print("X3 = 0")
                        print("Прохождение через Y3")
                        state = Y3
            else:
                print("X1 = 0")
                print(security_input())
                state = Y0
        elif (state == Y3):
            list_of_states.append('Y3')
            if (security_input() == '1'):
                print("X4 = 1")
                print("Прохождение через Y5")
                state = Y5
            else:
                print("X4 = 0")
                state = Y3
        elif (state == Y4):
            list_of_states.append('Y4')
            if (security_input() == '1'):
                print("X4 = 1")
                print("Прохождение через Y5")
                state = Y5
            else:
                print("X4 = 0")
                print("Прохождение через Y3")
                state = Y3
        else:                                         #state == Y5
            list_of_states.append('Yк')
            print("Конечное состояние!")
            GDG(list_of_states)
            break            
def fsm_sort_through(state = 0):                      #fsm == Finite State Machine
    def GDG(x):                                       #Graphical Display of the Graph state history 
        for i in range(len(x)):
            if (i != len(x)-1):
                print(f"{x[i]} ->", end=" ")
            else:
                print(f"{x[i]}", '\n')
    list_of_options = ['0000', '0001', '0010', '0011',
                       '0100', '0101', '0110', '0111',
                       '1000', '1001', '1010', '1011',
                       '1100', '1101', '1110', '1111']
    Y0, Y1, Y2, Y3, Y4, Y5 = (0, 1, 2, 3, 4, 5)
    print("Вариант №6")                   
    for index_of_option in range(0, 16):
        index = 0; list_of_states = list(); content = list_of_options[index_of_option]
        state = 0
        print(f"X1 = {content[0]}, X2 = {content[1]}, X3 = {content[2]}, X4 = {content[3]}", end=': ')
        while True:
            if (index >= len(content) and state != Y5):
                GDG(list_of_states)
                break
            if (state == Y0):
                list_of_states.append('Yн')
                state = Y1
            elif (state == Y1):
                list_of_states.append('Y1')
                state = Y2
            elif (state == Y2):
                list_of_states.append('Y2')
                if (len_content_and_index_checker(content, index)):
                    continue
                if ( content[index] == '1'):                                    # -> X1
                    index += 1
                    if (len_content_and_index_checker(content, index)):
                        continue
                    if (content[index] == '1'):                                
                        index += 1
                        state = Y1
                    else:
                        index += 1                                              # -> X2
                        if (len_content_and_index_checker(content, index)):
                            continue
                        if (content[index] == '1'):                             # -> X3
                            index += 1
                            state = Y4
                        else:
                            index += 1
                            state = Y3
                else:
                    index += 1 
                    state = Y0
            elif (state == Y3):
                list_of_states.append('Y3')
                if (len_content_and_index_checker(content, index)):
                    continue
                if (content[index] == '1'):
                    index += 1
                    state = Y5
                else:
                    index += 1
                    state = Y3
            elif (state == Y4):
                list_of_states.append('Y4')
                if (len_content_and_index_checker(content, index)):
                    continue
                if (content[index] == '1'):
                    index += 1
                    state = Y5
                else:
                    index += 1
                    state = Y3
            else:                                                   #state == Y5
                list_of_states.append('Yк')
                GDG(list_of_states)
                break            
def mode_of_input():
    def security_input_2():
        x = input("Введите 1, 2 , 3 или 4: ")
        if x in ('1', '2', '3', '4'):
            if  (x == '1'):
                print("Убедитесь, что название файла text.txt и что он размещён в пути C:\\text.txt")
            elif(x == '2'):
                print("Посимвольный ввод команд, все неподходящие значения будут игнорироваться")
            elif(x == '3'):
                print("Выбран ввод команд одной строкой, все неподходящие значения будут игнорироваться")
            elif(x == '4'):
                print("Перебор всех значений")
            return int(x)
        else:
            print("Введено неверное значение...")
            security_input_2()
    print("Выберите режим ввода")
    print("Ввод из файла - наберите \'1\'")
    print("Ввод посимвольно - наберите \'2\'")
    print("Ввод строкой команд - наберите \'3\'")
    print("Перебор всех значений - наберите \'4\'")
    dict_of_modes = {1: 1, 2: 2, 3: 3, 4: 4}
    return dict_of_modes[security_input_2()]
def start_fsm():
    input_mode = mode_of_input()
    if (input_mode == 1):
        fsm_file()
    elif (input_mode == 2):
        main_fsm()
    elif (input_mode == 4):
        fsm_sort_through()
    else:
        fsm_string()
while True:
    start_fsm()
    print("Для повторного запуска программы введите любой символ")
    print("Для завершения программы нажмите Enter")

    x = input()
    if x == '':
        break
    else:
        continue

