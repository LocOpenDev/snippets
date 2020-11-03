import random, sys, unittest

def guest_num(max=20):
    """Random a number from 1 to 100 and let user guest that number up to max of tries.
    """
    rand_num = random.randint(1, 101)
    retries = 0
    while retries <= max:
        try:
            n = int(input('Input a number: '))
            if n == rand_num:
                print('YOU WIN!')
                break
            elif n > rand_num:
                print('Iputed number is great than result number. Just retry!')
                retries += 1
            else:
                print('Iputed number is less than result number. Just retry!')
                retries += 1
        except ValueError:
            print('Only can input a number!')
        except:
            print('Only can input a number!')
    else:
        print('YOU LOST!')

class TestGuestNum(unittest.TestCase):
    pass

if __name__ == '__main__':
    guest_num(int(sys.argv[1]))