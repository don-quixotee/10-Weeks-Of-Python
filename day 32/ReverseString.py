def reverse(str):
    str = ''.join(reversed(str))
    return str


if __name__ == '__main__':
    str = input('Enter a string to reverse\n')
    print(reverse(str))
