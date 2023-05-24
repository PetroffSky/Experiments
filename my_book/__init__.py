def answer_yesno():
    answer = None
    flag = False
    while not flag:
        input_answer = input("Введите да - если ответ утвердителен.\n"
                             "Введите нет - если ответ отрицателен.\n"
                             "Ожидаю ввод: ")
        if input_answer in ["lf", "yes", "да", "нуы"]:
            answer = input_answer
            flag = True
        elif input_answer == "exit":
            break
        else:
            print("Введён недопустимый ответ! Повторите ввод!\n")
            flag = False

    return answer


def answer_number():
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


def main():
    print("Вводим числа?")
    main_answer = answer_yesno()
    if main_answer in ["lf", "yes", "да", "нуы"]:
        print(answer_number())
    else:
        pass



if __name__ == "__main__":
    print("Начинаем работать!")
    main()