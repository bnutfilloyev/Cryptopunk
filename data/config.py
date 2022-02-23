from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
STRIPE = env.str("STRIPE")
CHANEL = "CHANELID"
GROUP_ID = "GROUPID"
COLOR_IMAGE = "IMAGE ID"
PRICE = 29
ENDPOINT_SECRET = env.str("ENDPOINT_SECRET")
