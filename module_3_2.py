# Домашняя работа по уроку "Способы вызова функции"

def check(string):
    address = [".com", ".ru", ".net"]
    flag = False
    for elem in address:
        if string[-len(elem):] == elem:
            flag = True
    return flag


def send_email(message, recipient, sender = "university.help@gmail.com"):

    if "@" not in recipient or "@" not in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if check(recipient) and check(sender):
        pass
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    return


re = "reg@mail.ruk"
se = "regmail.ru"
mes = "jhvsdjvjsfvn"
print(send_email(mes, re, se))
