from random import choice, randint, getrandbits
from string import ascii_letters, digits
import datetime


def random_number(start: int = 100, end: int = 1000) -> int:
    return randint(start, end)


def random_string(start: int = 9, end: int = 15) -> str:
    return ''.join(choice(ascii_letters + digits) for _ in range(randint(start, end)))


def random_list_of_strings(start: int = 9, end: int = 15) -> list[str]:
    return [random_string() for _ in range(randint(start, end))]


def random_id() -> str:
    # a0c9b92f - 59c0 - 4956 - 9046 - 7091a15f7de8 пример ID
    elem_id = ''.join(choice(ascii_letters[:6] + digits) for _ in range(8))
    elem_id += '-'+''.join(choice(ascii_letters[:6] + digits) for _ in range(4))
    elem_id += '-'+''.join(choice(ascii_letters[:6] + digits) for _ in range(4))
    elem_id += '-'+''.join(choice(ascii_letters[:6] + digits) for _ in range(4))
    elem_id += '-'+''.join(choice(ascii_letters[:6] + digits) for _ in range(12))
    return elem_id


def random_link(start: int = 5, end: int =10) -> str:
    link = 'http://'+''.join(choice(ascii_letters+digits) for _ in range(randint(start, end))).lower()+'.com'
    return link


def random_bool() -> bool:
    return bool(getrandbits(1))


def random_email(start: int = 5, end: int = 15) -> str:
    email = ''.join(choice(ascii_letters+digits) for _ in range(randint(start, end))).lower() + '@gmail.com'
    return email


def random_phone() -> str:
    phone = '+7' + ''.join(choice(digits) for _ in range(10))
    return phone


def random_event_status() -> str:
    status = choice(digits[:3])
    return status


def random_user_access() -> str:
    access = choice(digits[1:3])
    return access


def random_datetime() -> str:
    cur_date = datetime.datetime.today() - datetime.timedelta(randint(1, 1000))
    cur_date = cur_date.replace(second=0, microsecond=0)
    return cur_date.isoformat('T', timespec='minutes')


def random_course() -> str:
    course = choice(digits[1:5])
    return course
