from brainaic.bot import Bot


data_path = "./data"
bot = Bot(data_path=data_path)
ans = bot.get_response("What did the president say about Ketanji Brown Jackson")
print(ans)
