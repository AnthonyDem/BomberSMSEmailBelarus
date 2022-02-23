def parse_phone_a1(phone):
    phone = phone.replace('+', '')
    phone = phone[0:3] + '+' + phone[3:5] + '+' + phone[5:8] + '+' + phone[8:10] + '+' + phone[10:12]
    phone = f"%2B{phone}"
    return phone


def parse_phone_bk(phone):
    phone = phone.replace('+', '')
    phone = phone[0:3] + '(' + phone[3:5] + ')' + '%20' + phone[5:]
    phone = f"%2B{phone}"
    return phone