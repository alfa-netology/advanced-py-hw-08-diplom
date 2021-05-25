import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api import VkUpload

from application.classes.response_manager import ResponseManager
from application.utilites.logger import set_logger

logger = set_logger(__name__)

class Bot:
    def __init__(self, api_token):
        authorize = vk_api.VkApi(token=api_token)
        self.longpoll = VkLongPoll(authorize)
        self.upload = VkUpload(authorize)
        self.vk_api = authorize.get_api()

    def start(self):
        # to do: добавить проверку на разрыв соединения со стороны VK
        logger.info('Бот успешно стартовал')
        dispatcher = ResponseManager()
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                received_message = event.text.lower().strip()
                sender_name = self._get_user_name(event.user_id)
                logger.info(f"{sender_name}[{event.user_id}]: {received_message}")

                message = dispatcher.process_message(received_message, sender_name, self.upload)
                self._send_message(sender_id=event.user_id, **message)

    def _send_message(self, sender_id='', message='', attachments='', keyboard='', sticker_id=''):
        logger.info(f"Бот: {message} {attachments} {sticker_id}")

        self.vk_api.messages.send(
            peer_id=sender_id,
            message=message,
            attachment=','.join(attachments),
            keyboard=keyboard,
            sticker_id=sticker_id,
            random_id=get_random_id()
        )

    def _get_user_name(self, user_id):
        return self.vk_api.users.get(user_id=user_id)[0].get('first_name')
