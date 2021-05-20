from application.utilites.dotenv import load_env_values
import os

if load_env_values():
    api_token = os.getenv('api_token')
    group_id = os.getenv('group_id')
    vk_login = os.getenv('vk_login')
    vk_password = os.getenv('vk_password')