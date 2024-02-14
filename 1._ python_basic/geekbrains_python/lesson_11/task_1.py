class Date:
    def __init__(self, date):
        self.data = self.valid_data(date)

    @staticmethod
    def valid_data(str_data):
        int_data = str_data.split('-')
        day = int(int_data[0])
        month = int(int_data[1])
        year = int(int_data[2])
        if month < 1 or month > 12 or day < 1 or day > 31 \
                or year < 1 or year > 2024:
            raise ValueError('Invalid month or day')
        return f'Valid month day and year\n{day} {month} {year}'

    def __str__(self):
        return f'{self.data}'


print(Date('05-12-1991'))
