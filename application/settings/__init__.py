from application.utilites.dotenv import load_env_values
import os

if load_env_values():
    api_token = os.getenv('api_token')
    api_version = os.getenv('api_version')
    vk_login = os.getenv('vk_login')
    vk_password = os.getenv('vk_password')
