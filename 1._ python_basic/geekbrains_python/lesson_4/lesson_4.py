import hello_module
import sys
from datetime import datetime

hello_module.say_hello('fox')

date_1 = datetime(year=2020, month=6, day=5)
date_2 = datetime(year=2019, month=12, day=25)
date_delta = date_1 - date_2
print(date_delta.days)


def main(argv):
    program, *args = argv
    result = sum(map(int, args))
    print(f'результат: {result}')
    return 0


if __name__ == '__main__':
    import sys

exit(main(sys.argv))
