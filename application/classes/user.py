import vk_api

from application.settings import vk_login, vk_password, api_version
from application.utilites.logger import set_logger

logger = set_logger(__name__)

class User:
    def __init__(self, input_id):
        self.session = self._auth()
        self.input_id = input_id

    def _auth(self):
        session = vk_api.VkApi(vk_login,
                               vk_password,
                               app_id=204586087,
                               api_version=api_version,
                               auth_handler=self.auth_handler)

        try:
            session.auth(token_only=True)
        except vk_api.AuthError as error:
            logger.error(error)
            return None

        logger.info(f'{vk_login} авторизовался')
        return session

    @staticmethod
    def auth_handler():
        """ при двухфактороной аутентификации вызывается это функция"""
        key = input("Enter authentication code:")
        remember_device = True
        logger.info('введен код аутентификации')
        return key, remember_device
