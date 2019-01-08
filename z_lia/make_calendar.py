def my_calendar():
    Month = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']
    Date = ['일|', '월|', '화|', '수|', '목|', '금|', '토']
    Day = {
    '1월': list(range(1, 32)), '2월': list(range(1, 29)), '3월': list(range(1, 32)),
    '4월': list(range(1, 31)), '5월': list(range(1, 32)), '6월': list(range(1, 31)),
    '7월': list(range(1, 32)), '8월': list(range(1, 32)), '9월': list(range(1, 31)),
    '10월': list(range(1, 32)), '11월': list(range(1, 31)), '12월': list(range(1, 32)),
    }
    for i in range(12):
        print(Month[i])
        print('----' * len(Date))
        if i >= 1:
                if len(Day[Month[i]]) < 42:
                    blank = ["  "] * (len(Day[Month[i-1]]) % 7)
                    Day[Month[i]] = blank + Day[Month[i]]
                else:
                    Day[Month[i]].remove("  ")
        for j in range(7):
            print(Date[j], end=' ')
        print()
        for k in Day[Month[i]]:
            if k != "  ":
                print(k, end='   ') if k < 10 else print(k, end='  ')
            else:
                print(k)
            if Day[Month[i]].index(k) % 7 == 0:
                print()
        print('\n')
my_calendar()