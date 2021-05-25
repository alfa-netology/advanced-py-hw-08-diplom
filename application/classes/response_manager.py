from application.classes.commands import Commands
from application.classes.keyboards import Keyboards
from application.classes.user import User

class ResponseManager:
    @staticmethod
    def process_message(received_message, sender_name, upload):

        if received_message in Commands.start.value:
            message = f'Приветствую тебя, {sender_name}!\n' \
                      f'Отправь мне одну из этих команд:\n' \
                      f'Меню, Поиск, Картинка'
            return dict(message=message)

        elif received_message in Commands.show_keyboard.value:
            return dict(message='Клавиатура отправлена', keyboard=Keyboards.show_default())

        elif received_message in Commands.hide_keyboard.value:
            return dict(message='Клавиатура убрана', keyboard=Keyboards.hide())

        elif received_message in Commands.search.value:
            return dict(message='Данная функция находится в разработке')

        elif received_message in Commands.picture.value:
            # to do: пересмореть данный метод (упростить)
            image = "application/images/logo.jpg"
            attachments = list()
            upload_image = upload.photo_messages(photos=image)[0]
            attachments.append(f'photo{upload_image.get("owner_id")}_{upload_image.get("id")}')
            return dict(message='Изображение отправлено', attachments=attachments)

        elif '#' in received_message:
            user = User(received_message[1:])
            return dict(message=f'session: {user.session}')

        # elif received_message in Commands.bye.value:
        #     return dict(sticker_id='3143')

        else:
            message = 'Неизвестная команда.\n Доступные команды:\nМеню, Поиск, Картинка, Пока'
            return dict(message=message)
