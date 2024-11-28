def send_email(message, recipient, sender =  "university.help@gmail.com"):
    if '@' not in recipient or not (recipient.endswith('.ru') or recipient.endswith('.com') or recipient.endswith('.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif '@' not in sender or not (sender.endswith('.ru') or sender.endswith('.com') or sender.endswith('.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif 'university.help@gmail.com' not in sender:
        print(f'Нестандартный отправитель! Письмо отправлено с {recipient} на адрес {sender}')
    else:
        print('Письмо успешно отправлено!')

send_email('Привет!', 'student')
send_email('Привет!', 'student@mail.ru')
send_email('Привет!','university.help@gmail.com')
send_email('Привет!', 'student@mail.com', 'Urban.net')