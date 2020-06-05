from random import randint


class DataGenerator:
    @staticmethod
    def random_with_n_digits(n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)

    def create_new_phone(self):
        return "+" + str(self.random_with_n_digits(5))

    def create_new_email(self):
        return "test" + str(self.random_with_n_digits(1)) + "@mail.com"