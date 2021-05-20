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

    @staticmethod
    def keyboard():
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Привет', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Поиск', color=VkKeyboardColor.SECONDARY)
        keyboard.add_line()
        keyboard.add_button('Послать фото', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Пока', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
        keyboard.add_openlink_button('Дипломное задание',
                                     link='https://github.com/netology-code/py-advanced-diplom/tree/new_diplom')
        return keyboard.get_keyboard()

    def start(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                received_message = event.text.lower()
                sender_id = event.user_id
                sender_name = self.get_user_name(sender_id)

                # отправка фото
                attachments = list()
                upload_image = self.upload.photo_messages(photos=self.image)[0]
                attachments.append(f'photo{upload_image.get("owner_id")}_{upload_image.get("id")}')

                if received_message == "привет":
                    self.send_message(sender_id, f'Добрый день, {sender_name}',  keyboard=self.keyboard())
                elif received_message == 'послать фото':
                    self.send_message(sender_id, 'Держи фоточку', attachments)
                else:
                    self.send_message(sender_id, 'Неизвестная команда.')

    def send_message(self, sender_id, message, attachments='', keyboard=''):
        self.vk_api.messages.send(
            peer_id=sender_id,
            message=message,
            random_id=get_random_id(),
            attachment=','.join(attachments),
            keyboard=keyboard
        )

    def get_user_name(self, user_id):
        return self.vk_api.users.get(user_id=user_id)[0].get('first_name')

    def test(self):
        self.send_message(8301129, 'Hi from net!')
