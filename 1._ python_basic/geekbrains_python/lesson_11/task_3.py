class OwnExeption(Exception):
    num_list = list()

    def __init__(self):
        self.txt = 'Ошибка,введите цифру'

    def list_append(self, input_str):
        try:
            if input_str == 'stop':
                print(self.num_list)
                raise SystemExit
            elif input_str.isdigit():
                self.num_list.append(int(input_str))
            else:
                raise OwnExeption
        except OwnExeption:
            print(self.txt)


num = OwnExeption()


def inp():
    while True:
        num.list_append(input('введите цифру: '))


if __name__ == '__main__':
    inp()
