from telegram import ParseMode, Update, Bot, Chat, MessageEntity
from telegram.ext import CommandHandler, MessageHandler, BaseFilter, run_async

from tg_bot import dispatcher

from requests import get
from tg_bot.modules.disable import DisableAbleCommandHandler

import json
from urllib.request import urlopen



@run_async
def covidi(bot: Bot, update: Update):
  update.effective_message.reply_text(
      "*ð¦  COVID-19 Stats In India ð¦ :*\n\n"
        "â¥ *Total Confirmed* \nã¤ã¤âÂ» `" + str(JHU.India.confirmed) + "`\n"
        "â¥ *Total Deaths* \nã¤ã¤âÂ» `" + str(JHU.India.deaths) + "`\n"
        "â¥ *Total Recovered* \nã¤ã¤âÂ» `" + str(JHU.India.recovered) +"`\n"
        "â¥ *Active Cases* \nã¤ã¤âÂ» `"+ str(JHU.India.cases) + "`\n\n"
        "â¥ *Tips*\nâ ð· Wear A Mask.\n â ð§» Use Tissue When Sneezing Or Blowing Nose.\nâ ð§¼ Wash Your Hands Frequently.\nâï¸ï¸ï¸ ð¬ Avoid Contact With Others.\nâï¸ï¸ï¸ ð Wash Foods Before Eating It.\nâï¸ï¸ï¸ ð Maintain Good Hygiene", parse_mode=ParseMode.MARKDOWN)
  
@run_async
def covidc(bot: Bot, update: Update):
  update.effective_message.reply_text(
      "*ð¦  COVID-19 Stats In China ð¦ :*\n\n"
        "â¥ *Total Confirmed* \nã¤ã¤âÂ» `" + str(JHU.China.confirmed) + "`\n"
        "â¥ *Total Deaths* \nã¤ã¤âÂ» `" + str(JHU.China.deaths) + "`\n"
        "â¥ *Total Recovered* \nã¤ã¤âÂ» `" + str(JHU.China.recovered) +"`\n"
        "â¥ *Active Cases* \nã¤ã¤âÂ» `"+ str(JHU.China.cases) + "`\n\n"
        "â¥ *Tips*\nâ ð· Wear A Mask.\n â ð§» Use Tissue When Sneezing Or Blowing Nose.\nâ ð§¼ Wash Your Hands Frequently.\nâï¸ï¸ï¸ ð¬ Avoid Contact With Others.\nâï¸ï¸ï¸ ð Wash Foods Before Eating It.\nâï¸ï¸ï¸ ð Maintain Good Hygiene", parse_mode=ParseMode.MARKDOWN)
  
@run_async
def covidp(bot: Bot, update: Update):
  update.effective_message.reply_text(
      "*ð¦  COVID-19 Stats In Pakistan ð¦ :*\n\n"
        "â¥ *Total Confirmed* \nã¤ã¤âÂ» `" + str(JHU.Pakistan.confirmed) + "`\n"
        "â¥ *Total Deaths* \nã¤ã¤âÂ» `" + str(JHU.Pakistan.deaths) + "`\n"
        "â¥ *Total Recovered* \nã¤ã¤âÂ» `" + str(JHU.Pakistan.recovered) +"`\n"
        "â¥ *Active Cases* \nã¤ã¤âÂ» `"+ str(JHU.Pakistan.cases) + "`\n\n"
        "â¥ *Tips*\nâ ð· Wear A Mask.\n â ð§» Use Tissue When Sneezing Or Blowing Nose.\nâ ð§¼ Wash Your Hands Frequently.\nâï¸ï¸ï¸ ð¬ Avoid Contact With Others.\nâï¸ï¸ï¸ ð Wash Foods Before Eating It.\nâï¸ï¸ï¸ ð Maintain Good Hygiene", parse_mode=ParseMode.MARKDOWN)
  
@run_async
def covida(bot: Bot, update: Update):
  update.effective_message.reply_text(
      "*ð¦  COVID-19 Stats In Australia ð¦ :*\n\n"
        "â¥ *Total Confirmed* \nã¤ã¤âÂ» `" + str(JHU.Australia.confirmed) + "`\n"
        "â¥ *Total Deaths* \nã¤ã¤âÂ» `" + str(JHU.Australia.deaths) + "`\n"
        "â¥ *Total Recovered* \nã¤ã¤âÂ» `" + str(JHU.Australia.recovered) +"`\n"
        "â¥ *Active Cases* \nã¤ã¤âÂ» `"+ str(JHU.Australia.cases) + "`\n\n"
        "â¥ *Tips*\nâ ð· Wear A Mask.\n â ð§» Use Tissue When Sneezing Or Blowing Nose.\nâ ð§¼ Wash Your Hands Frequently.\nâï¸ï¸ï¸ ð¬ Avoid Contact With Others.\nâï¸ï¸ï¸ ð Wash Foods Before Eating It.\nâï¸ï¸ï¸ ð Maintain Good Hygiene", parse_mode=ParseMode.MARKDOWN)
  
  
  

  
__help__ = """

 â¥ /covindia - Get Corona Status Of India
 â¥ /covchina - Get Corona Status Of China
 â¥ /covpakistan - Get Corona Status Of Pakistan
 â¥ /covaustralia - Get Corona Status Of Australia 
 
"""

__mod_name__ = 'Covid Tracker'



COVIDI_HANDLER = CommandHandler("covindia", covidi, admin_ok=True)
COVIDC_HANDLER = CommandHandler("covchina", covidc, admin_ok=True)
COVIDP_HANDLER = CommandHandler("covpakistan", covidp, admin_ok=True)
COVIDA_HANDLER = CommandHandler("covaustralia", covida, admin_ok=True)



dispatcher.add_handler(COVIDI_HANDLER)
dispatcher.add_handler(COVIDC_HANDLER)
dispatcher.add_handler(COVIDP_HANDLER)
dispatcher.add_handler(COVIDA_HANDLER)


