# 38803160272
while True:
    try:
        isikukood = input('Enter ID code: ')
        int(isikukood)
        if len(isikukood) != 11:
            raise UserWarning
    except ValueError:
        print('Code you entered is not numeric!')
        continue
    except UserWarning:
        if len(isikukood) > 11:
            print('Too long code!')
        else:
            print('Too short code!')
        continue
    else:
        print('ID CODE:', isikukood)

    while True:
        user_choice = input('Please choose:\n1.Print Gender\n2.Print date of birth\n3.Print Region\n4.Validate ID\n'
                            '5.Change ID\n0.Exit\n--> ')
        if user_choice == '1':
            if int(isikukood[0]) % 2 == 0:
                print('You are Female')
            else:
                print('You are Male')
        elif user_choice == '2':
            if isikukood[0] in '12':
                bcent = '18'
            elif isikukood[0] in '34':
                bcent = '19'
            elif isikukood[0] in '56':
                bcent = '20'
            elif isikukood[0] in '78':
                bcent = '21'
            else:
                print('Can\'t determine date of birth!')
                continue
            print(f'DOB: {isikukood[5:7]}.{isikukood[3:5]}.{bcent}{isikukood[1:3]}')
        elif user_choice == '3':
            if '001' <= isikukood[7:10] <= '010':
                print('Kuressaare haigla')
            elif int(isikukood[7:10]) in range(11, 20):
                print('Tartu Ülikooli Naistekliinik')
        elif user_choice == '4':
            chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
            chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
            res = 0
            for num in range(10):
                res += chk1[num] * int(isikukood[num])
            if int(isikukood[-1]) == res % 11:
                print('Valid!')
            elif res % 11 in [0, 10]:
                res = 0
                for num in range(10):
                    res += chk2[num] * int(isikukood[num])
                if int(isikukood[-1]) == res % 11:
                    print('Valid!')
                else:
                    print('Invalid')
        elif user_choice == '5':
            break
        elif user_choice == '0':
            print('Good bye!')
            quit()
        else:
            print('Your choice is out of range!')