from vk_api.keyboard import VkKeyboard, VkKeyboardColor

class Keyboards:
    @staticmethod
    def show_default():
        keyboard = VkKeyboard(one_time=False)
        keyboard.add_button('Поиск', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Картинка', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Спрячь клавиатуру', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_openlink_button('RICKROLL', link='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        return keyboard.get_keyboard()

    @staticmethod
    def hide():
        return VkKeyboard.get_empty_keyboard()

    # @staticmethod
    # def show_default():
    #     keyboard = VkKeyboard(one_time=False)
    #     keyboard.add_button('Поиск', color=VkKeyboardColor.PRIMARY)
    #     keyboard.add_button('Картинка', color=VkKeyboardColor.PRIMARY)
    #     keyboard.add_button('Пока', color=VkKeyboardColor.NEGATIVE)
    #     keyboard.add_line()
    #     keyboard.add_button('Спрячь клавиатуру', color=VkKeyboardColor.POSITIVE)
    #     keyboard.add_line()
    #     keyboard.add_openlink_button('RICKROLL', link='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    #     return keyboard.get_keyboard()
