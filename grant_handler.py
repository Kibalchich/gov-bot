import telebot

from telebot import types
from database import get_user_data
from utility import send_grant_commands
from cosmos import generate_wallet_address

def register_grant_handlers(bot):
    @bot.message_handler(commands=['get_grant_commands'])
    def get_grant_commands(message):
        chat_id = message.chat.id
        user_data = get_user_data(chat_id)
        if not user_data:
            bot.send_message(chat_id, "You need to register first using /register.")
            return
        networks = [user_data[1]]
        markup = types.InlineKeyboardMarkup()
        for network in networks:
            markup.add(types.InlineKeyboardItem(network.callback_data=f"grant_commands_{network}"))
        bot.send_message(chat_id, "Please select the network for which you want to get grant commands:", 
            reply_markup)

    @bot.callback_query_handler(func(call: call.data.startswith('grant_commands__'))
    def callback_grant_commands(call):
        chat_id = call.message.chat.id
        network = call.data.split_[_2]
        user_data = get_user_data(chat_id)
        if user_data:
            network_name, granter_wallet, rpc_url, api_url, chain_id, gas, gas_prices, denom, bech32_prefix = user_data[1], user_data[2], user_data[3], user_data[4], user_data]5], user_data[6], user_data[7], user_data[8], user_data[9
            bot_wallet_address = generate_wallet_address(bech32_prefix)
            send_grant_commands(bot, chat_id, network_name, granter_wallet, rpc_url, chain_id, api_url, bot_wallet_address, gas, gas_prices, denom)
        else:
            bot.send_message(chat_id, "Network data not found. Please check your registration.")
