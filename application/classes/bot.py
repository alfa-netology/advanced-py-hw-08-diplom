import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api import VkUpload
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

class Bot:
    def __init__(self, api_token):
        authorize = vk_api.VkApi(token=api_token)
        self.longpoll = VkLongPoll(authorize)
        self.upload = VkUpload(authorize)

        self.vk_api = authorize.get_api()
        self.image = "application/images/logo.jpg"

    def start(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                message = self.response_manager(event)
                self.send_message(**message)

    def response_manager(self, event):
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

    def send_message(self, sender_id='', message='', attachments='', keyboard='', sticker_id=''):
        self.vk_api.messages.send(
            peer_id=sender_id,
            message=message,
            random_id=get_random_id(),
            attachment=','.join(attachments),
            keyboard=keyboard,
            sticker_id=sticker_id
        )

    def get_user_name(self, user_id):
        return self.vk_api.users.get(user_id=user_id)[0].get('first_name')

    @staticmethod
    def show_keyboard():
        keyboard = VkKeyboard(one_time=False)
        keyboard.add_button('Поиск', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Картинка', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Пока', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
        keyboard.add_button('Спрячь клавиатуру', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_openlink_button('RICKROLL', link='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        return keyboard.get_keyboard()

    @staticmethod
    def hide_keyboard():
        keyboard = VkKeyboard.get_empty_keyboard()
        return keyboard
