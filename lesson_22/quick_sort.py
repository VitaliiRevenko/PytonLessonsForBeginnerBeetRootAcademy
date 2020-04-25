import random

def qs(array):
    if len(array) <= 1:
        return array
    else:
        r_choice = random.choice(array)
        print(r_choice)
        left = []
        middle = []
        right = []
        for i in array:
            if i < r_choice:
                left.append(i)
            elif i > r_choice:
                right.append(i)
            else:
                middle.append(i)
    print(left, middle, right)
    return qs(left) + middle + qs(right)
if __name__ == '__main__':
    print(qs([3,2,3,1]))
