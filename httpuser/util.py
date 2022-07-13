import string, random


class Util:
    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def get_random_int(start_range, end_range):
        return random.randint(start_range, end_range)
