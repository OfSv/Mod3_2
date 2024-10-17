# Задача "Рассылка писем"

def send_email(message, recipient, *, sender="university.help@gmail.com"):

    a="@" in recipient and "@" in sender and recipient.endswith(('.com', '.net', '.ru')) and sender.endswith(('.com', '.net', '.ru')) 

    if a == False:
        print(
            f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(
            f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")                 
    else:
        print(
            f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание',
           'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре',
           'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email('Это сообщение с ошибкой в адресе', 'vasyok1337@gmail.comp')