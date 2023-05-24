def select_answer():
    mylist = []
    flag = False
    while not flag:
        input_answer = input("Ожидаю ввод числа (для остановки, введите stop): ")
        if input_answer.isalpha():
            if input_answer == "stop":
                flag = True
            else:
                print("Введено не число! Ошибка")
                break
        else:
            mylist.append(int(input_answer))
            flag = False
    return mylist



if __name__ == "__main__":
    print("Начинаем работать!")
    print(select_answer())