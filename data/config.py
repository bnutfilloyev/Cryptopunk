from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
STRIPE = env.str("STRIPE")
GROUP_ID = env.int("GROUP_ID")
COLOR_IMAGE = env.str("COLOR_IMAGE")
PRICE = 29
ENDPOINT_SECRET = env.str("ENDPOINT_SECRET")

