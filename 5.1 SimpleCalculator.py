while True:
    f_num = int(input("Enter First number: "))
    s_num = int(input("Enter Second number: "))
    opr = str(input("Enter\n + to Add\n- to Substract\n* to multiply\n/ to divide\nQ to Quit\n"))
    rsl = 0
    if opr == "+":
        rsl = f_num + s_num
        print(f_num, " ", opr, " ", s_num, " = ", rsl)
    elif opr == "-":
        rsl = f_num - s_num
        print(f_num, " ", opr, " ", s_num, " = ", rsl)
    elif opr == "*":
        rsl = f_num - s_num
        print(f_num, " ", opr, " ", s_num, " = ", rsl)
    elif opr == "/":
        rsl = f_num - s_num
        print(f_num, " ", opr, " ", s_num, " = ", rsl)
    elif opr == "Q" or opr == "q":
        break
    else:
        print("Wrong Input")
