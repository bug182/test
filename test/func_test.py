answer = input('y/n: ')

def test(a):
    if a.lower() == 'y' or a.lower() == 'n':
        print('THIS WORKS!!!')
    else:
        print('THIS STILL WORKS!!!')


test(answer)
