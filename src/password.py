import string
import random


class Password:
    def __init__(self):
        self._length = 16
        self._uppercase = self._lowercase = self._digits = self._special_chars = True

    @property
    def uppercase(self) -> bool:
        return self._uppercase

    @uppercase.setter
    def uppercase(self, value: bool) -> None:
        self._uppercase = value

    @property
    def lowercase(self) -> bool:
        return self._lowercase

    @lowercase.setter
    def lowercase(self, value: bool) -> None:
        self._lowercase = value

    @property
    def digits(self) -> bool:
        return self._digits

    @digits.setter
    def digits(self, value: bool) -> None:
        self._digits = value

    @property
    def specialChars(self) -> bool:
        return self._special_chars

    @specialChars.setter
    def specialChars(self, value: bool) -> None:
        self._special_chars = value

    @property
    def length(self) -> int:
        return self._length

    @length.setter
    def length(self, value: int) -> None:
        self._length = value

    def generate(self) -> str:
        chars = [x for x in f'{string.ascii_lowercase if self._lowercase else ""}{string.ascii_uppercase if self._uppercase else ""}{string.digits if self._digits else ""}{string.punctuation if self._special_chars else ""}']
        for _ in range(3):
            random.shuffle(chars)
        password = ""
        for _ in range(self._length):
            password += random.choice(chars)
        return password
