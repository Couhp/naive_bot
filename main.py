from chatbot import MyBot

bot = MyBot(name="HiHi")
input_chat = ""

while True :
    input_chat = str(input())
    if input_chat == "end" : break
    print ("\n-" + bot.get_response(input_str=input_chat))