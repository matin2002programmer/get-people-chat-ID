import telegram

bot_token="1809854554:AAFLZRo3ekBPbdQCNRXvqDYc2acoqCs962U"

bot=telegram.Bot(bot_token)
 
bot.get_updates()    
chat_id  = bot.get_updates()[-1].message.chat_id
people_id = chat_id

x=1
bot.send_message("1149845628",x)              

                            
        
bot.send_message("1149845628",people_id)
