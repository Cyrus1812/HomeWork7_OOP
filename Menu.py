def calc_menu():
    stop_work = False
    while(stop_work != True):
        print("Какую операцию вы хотите выполнить?")
        print("1 +; 2 -; 3 *; 4 /; 5 выход ")
        user_input = int(input())
        if(user_input == 1 ):
            from Addition import Addit
            print('')
        elif(user_input == 2):
            from Substraction import Substract
            print('')
        elif(user_input == 3):
            from Multiplication import Multi
            print('')
        elif(user_input == 4):
            from Division import Divi
            di = Divi
            print(di)
            print('')
        elif(user_input == 5):
            print("Завершение работы")
            stop_work = True
        else:
            print("ВВедено некорректное значение")
calc_menu()