#!/usr/bin/env python3.5
from wxpy import *
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot("deepThought")# 用于回复消息的机器人
# chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot=ChatterBotCorpusTrainer(chatbot)
chatbot.train("chatterbot.corpus.chinese")# 使用该库的中文语料库
bot = Bot(cache_path=True)# 用于接入微信的机器人
tuling = Tuling(api_key="0f5639cdfe0a4f7e94e7d745eab23667")




# group_2 = bot.groups("哈哈群")[0]# 进行测试的群
group_2 = bot.groups().search('哈哈群')[0]
# group_2 = bot.search('wxpy')[0]
group_2.send("大家好,我是人工智能")

@bot.register(group_2)
def reply_my_friend(msg):
   print(msg)
   tuling.do_reply(msg)
   # return chatbot.get_response(msg.text).text# 使用机器人进行自动回复

# 堵塞线程，并进入 Python 命令行
embed()