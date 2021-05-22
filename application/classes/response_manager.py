from application.classes.commands import Commands
from application.classes.keyboards import Keyboards

class ResponseManager:
    @staticmethod
    def process_message(received_message, sender_name, upload):

        if received_message in Commands.start.value:
            message = f'Приветствую тебя, {sender_name}!\n' \
                      f'Отправь мне одну из этих команд:\n' \
                      f'Меню, Поиск, Картинка или Пока &#128521;'
            return dict(message=message)

        elif received_message in Commands.show_keyboard.value:
            return dict(message='Клавиатура отправлена', keyboard=Keyboards.show_default())

        elif received_message in Commands.hide_keyboard.value:
            return dict(message='Клавиатура убрана', keyboard=Keyboards.hide())

        elif received_message in Commands.search.value:
            return dict(message='Данная функция находится в разработке')

        elif received_message in Commands.bye.value:
            return dict(sticker_id='3143')

        elif received_message in Commands.picture.value:
            image = "application/images/logo.jpg"
            attachments = list()
            upload_image = upload.photo_messages(photos=image)[0]
            attachments.append(f'photo{upload_image.get("owner_id")}_{upload_image.get("id")}')
            return dict(message='Изображение отправлено', attachments=attachments)

        else:
            message = 'Неизвестная команда.\n Доступные команды:\n' \
                      'Меню, Убрать меню, Поиск, Картинка.'
            return dict(message=message)
