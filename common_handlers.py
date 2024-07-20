import telebot

def register_common_handlers(bot):
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Welcome to the Cosmos SDK Voting Bot!\nUse /register to start registration.\nUse /commands to see the list of available commands.")
    
    @bot.message_handler(commands=['/commands'])
    def list_commands(message):
        bot.reply_to(message, "Available commands:\n/start or /help - Show this message\n/register - Register your wallet\n/proposals - List active proposals\n/networks - List registered networks\n/granted_proposals - List proposals you ted for\n/revoke_permissions - Revoke granted permissions")
