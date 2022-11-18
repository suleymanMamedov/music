# importing packages
from pytube import YouTube
import telebot
import os

bot = telebot.TeleBot("5793875135:AAHTTFmszU5fyjxbVTZ5rYSLlYwQgAp9nbU")


@bot.message_handler(commands=['start'])
def shoot(message):
    bot.send_message(message.chat.id, "Linki gonderin")


@bot.message_handler()
def run(message):
    if "https://" not in message.text:

        return bot.send_message(message.chat.id, "Yanlis linkdir")
        

    bot.send_message(message.chat.id, "Zehmet olmasa gozleyin...")
    yt = YouTube(
        str(message.text,))

    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download()
    
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    bot.send_audio(message.chat.id, audio=open(new_file, 'rb'))
    print(yt.title + " has been successfully downloaded.")
    bot.send_message(message.chat.id, "Audio uqurla yuklendi")


bot.polling()


# url input from user


# extract only audio
# video = yt.streams.filter(only_audio=True).first()

# check for destination to save file
# print("Enter the destination (leave blank for current directory)")
# destination = str(input(">> ")) or '.'

# download the file
# out_file = video.download(output_path=destination)

# save the file
# base, ext = os.path.splitext(out_file)
# new_file = base + '.mp3'
# os.rename(out_file, new_file)

# # result of success
# print(yt.title + " has been successfully downloaded.")
