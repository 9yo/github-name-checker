# generating short nikcnames

from string import ascii_lowercase, digits


MAX_NICKNAME_LENGTH = 1


def generate():
    nicknames: list = [el for el in (ascii_lowercase + digits)]
    base = nicknames

    for _ in range(MAX_NICKNAME_LENGTH):
        nick_buff = nicknames
        for symbol in base:
            for nick in nick_buff:
                nicknames.append(one_letter_nick + symbol)


if __name__ == '__main__':
    Generator.generate()
