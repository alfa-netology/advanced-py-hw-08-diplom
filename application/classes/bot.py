import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id


class Bot:
    def __init__(self, api_token):
        authorize = vk_api.VkApi(token=api_token)
        self.longpoll = VkLongPoll(authorize)
        self.vk_api = authorize.get_api()

    def start(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                received_message = event.text
                sender_id = event.user_id
                sender_name = self.get_user_name(sender_id)
                
                if received_message.lower() == "привет":
                    self.send_message(sender_id, f'Добрый день, {sender_name}')

    def send_message(self, sender_id, message):
        self.vk_api.messages.send(peer_id=sender_id, message=message, random_id=get_random_id())

    def get_user_name(self, user_id):
        return self.vk_api.users.get(user_id=user_id)[0].get('first_name')

    def test(self):
        self.send_message(8301129, 'Hi from net!')
