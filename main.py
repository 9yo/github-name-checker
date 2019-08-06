from requests import get
from typing import List
from termcolor import colored
from threading import Thread
from concurrent.futures import ThreadPoolExecutor


GITHUB_LINK: str = 'https://github.com/'
BASE_FILE_NAME: str = 'base.txt'


def get_names() -> List[str]:
    names: List[str] = list()
    for name in open(BASE_FILE_NAME):
        names.append(name.replace('\n', ''))

    names = names[::-1]
    return names


def check_name(name: str, print_is_busy: bool = False):
    profile_link: str = GITHUB_LINK + name
    req = get(profile_link)
    status_code: int = req.status_code
    if status_code == 200 and print_is_busy:
        print(colored('Name is busy: ' + name, 'red'))
    elif status_code == 404:
        print(colored('Name is free: ' + name, 'green'))


def check_names(names_list: List[str]):
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(check_name, names_list)


if __name__ == "__main__":
    names: List[str] = get_names()
    check_names(names)