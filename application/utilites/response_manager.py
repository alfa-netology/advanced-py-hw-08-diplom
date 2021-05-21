def get_message(event):
    received_message = event.text.lower()
    sender_name = self.get_user_name(event.user_id)
    sender_id = dict(sender_id=event.user_id)

    if received_message in ('начать', 'привет', 'зравствуй', 'здоров', 'старт', 'погнали', 'hi'):
        message = f'Приветствую тебя, {sender_name}!\n' \
                  f'Отправь мне одну из этих команд:\n' \
                  f'Поиск, Картинка или Пока.\n\n' \
                  f'Ну или воспользуйся клавиатуркой &#128521;\n' \
                  f'Ах, а клавиатурки то и нет, но не беда.\n' \
                  f'Отправь мне команду Клавиши.'
        return dict(**sender_id, message=message)

    elif received_message == 'клавиши':
        return dict(**sender_id, message='А вот и кнопочки', keyboard=self.show_keyboard())

    elif received_message == 'спрячь клавиатуру':
        message = 'Клавитура убрана.\n' \
                  'Помни про команду Клавиши.'
        return dict(**sender_id, message=message, keyboard=self.hide_keyboard())

    elif received_message == 'поиск':
        return dict(**sender_id, message='Данная функция находится в разработке')

    elif received_message == 'пока':
        return dict(**sender_id, sticker_id='3143')

    elif received_message == 'картинка':
        attachments = list()
        upload_image = self.upload.photo_messages(photos=self.image)[0]
        attachments.append(f'photo{upload_image.get("owner_id")}_{upload_image.get("id")}')
        return dict(**sender_id, message='Держи картиночку', attachments=attachments)

    else:
        message = 'Неизвестная команда.\n Доступные команды:\n' \
                  'Поиск, Картинка, Клавиши, Пока, Спрячь клавиатуру'
        return dict(**sender_id, message=message)