def get_ruler(kingdom):
    ruler = ''
    if kingdom[-1] in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
        ruler = 'Alice'
    elif kingdom[-1] != 'y':
        ruler = "Bob"
    else:
        ruler = 'nobody'
    return ruler


def main():
    # Get the number of test cases
    T = int(input())
    for t in range(T):
        # Get the kingdom
        kingdom = input()
        print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom)))


if __name__ == '__main__':
    main()
