__author__ = 'Cátedra de AED'

import recursion


def test():
    for m in range(4):
        for n in range(7):
            ack1 = recursion.ackermann(m, n)
            print('A(', m, ', ', n, '): ', ack1, '\t-\t', sep='', end='')
        print()


if __name__ == '__main__':
    test()

