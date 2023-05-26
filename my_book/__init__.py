import json

def answer_yesno():
    answer = None
    flag = False
    while not flag:
        input_answer = input(local_phrase[set_local]["yes_no"])
        print()
        if input_answer in ["lf", "yes", "да", "нуы"]:
            answer = input_answer
            flag = True
        elif input_answer == "exit":
            break
        else:
            print(local_phrase[set_local]["wrong_answer"])
            flag = False

    return answer


def answer_number():
    mylist = []
    flag = False
    while not flag:
        input_answer = input(local_phrase[set_local]["wait_num"])
        if input_answer.isalpha():
            if input_answer == "stop":
                flag = True
            else:
                print(local_phrase[set_local]["not_num"])
                break
        else:
            mylist.append(int(input_answer))
            flag = False

    return mylist


def main():
    print(local_phrase["ru"]["en_num"])
    main_answer = answer_yesno()
    if main_answer in ["lf", "yes", "да", "нуы"]:
        print(answer_number())
    else:
        pass



if __name__ == "__main__":

    with open("local.json", "r", encoding="utf-8") as local:
        local_phrase = json.load(local)


    with open(".settings", "r", encoding="utf-8") as settings:
        set_local = settings.read().strip("\n")[6:]

    print(local_phrase[set_local]["set_lang"] + "\n")
    print(local_phrase[set_local]["grt"])

    main()
