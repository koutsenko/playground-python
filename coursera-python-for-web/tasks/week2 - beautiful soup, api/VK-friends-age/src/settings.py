import dotenv
import os

dotenv.load_dotenv()

ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
URL_API_FRIENDS = "https://api.vk.com/method/friends.get"
URL_API_USERID = "https://api.vk.com/method/users.get"
VK_API_VER = 5.71
