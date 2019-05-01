import time

class personality:
    def __init__(self):
        self.low = "Introvert"
        self.high = "Extrovert"
        self.score = 0

    def test(self):
        number = 0
        print("Please answer these questions honestly:)")
        time.sleep(1)
        where_go = input("Would you Rather (1)go outside with friends, or (2) stay inside with a book?")
        if where_go == '1':
            print('you chose one')
            number += 1
        elif where_go == '2':
            print('you chose two')
            number -= 1
        '''test1 = input("1,2")
        if test1 == 1:
            self.score += 1
        elif test1 == 2:
            number -= 1
        test2 = input("1,2")
        if test2 == 1:
            number += 1
        elif test2 == 2:
            number -= 1
        test3 = input("1,2")
        if test3 == 1:
            number += 1
        elif test3 == 2:
            number -= 1
        test4 = input("1,2")
        if test4 == 1:
            number += 1
        elif test4 == 2:
            number -= 1'''
        return number

    def __repr__(self):
        return '{score}'.format(score = self.score)

p_test = personality()

score = p_test.test()
print(score)
