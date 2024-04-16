from datatypes import bot
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dnd_rpg_discord_bot"]
mycol = mydb["config"]

bot.Bot(mycol.find_one({"option": "token"}).get("value")).run()
