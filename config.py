from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')

# CHANNEL_ID1 = env.str('CHANNEL_ID1')

CHAT_ID = {
    'CHANNEL_ID1': env.str('CHANNEL_ID1'),
    'sssss': env.str('CHAT_ID1'),
    'test': env.str('CHAT_ID2'),
}

MAIN_CHAT_ID = env.str('MAIN_CHAT_ID')
