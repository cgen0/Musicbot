from telethon import TelegramClient, sync, events
from telethon.tl.types import  DocumentAttributeAudio
import os, Metadata

import logging
logging.basicConfig(level=logging.ERROR)


#--------------enter your own values--------------

api_id= 123456
api_hash='exampleapihash'
phone='phonenumber'
target_chat_id= -10012345678
myID=12345678

#-------------------------------------------------

client=TelegramClient("client", api_id, api_hash)

def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]


@client.on(events.NewMessage)
async def handler(event):
    if '/add' in event.raw_text and event.sender_id == myID:
        dir = str(event.raw_text)[5:]
        for dirname, dirnames, filenames in walklevel('./' + dir, 0):
            for subdirname in dirnames:
                print(os.path.join(dirname, subdirname))

                for file in os.listdir(os.path.join(dirname, subdirname)):
                    if file.endswith(".flac"):
                        metadata = Metadata.fetch_metadata(os.path.join(dirname, subdirname, file))

                        break

                os.system("zip -r '" + subdirname + "'.zip " +"'" + os.path.join(dirname, subdirname)+"'")
                zip = subdirname + ".zip"
                Metadata.fetch_images(os.path.join(dirname, subdirname, file))
                await client.send_file(target_chat,file='copertina.jpg',caption=metadata['total'])
                await client.send_file(target_chat,file=zip,force_document=True)


                for file in os.listdir(os.path.join(dirname, subdirname)):
                    if file.endswith(".flac"):
                        print(os.path.join(dirname, subdirname, file))

                        metadata = Metadata.fetch_metadata(os.path.join(dirname, subdirname, file))
                        duration = int(metadata['duration'])
                        title = (metadata['title'])
                        performer =(metadata['artist'])

                        await client.send_file(target_chat, file=os.path.join(dirname, subdirname, file),
                                               thumb='copertina.jpg', mime_type="audio/flac",
                                               attributes=[DocumentAttributeAudio(duration=duration, title=title, performer=performer)])

                os.system("rm ./copertina.jpg")
                os.system("rm ./*.zip")


client.start()
client.get_dialogs()
target_chat = client.get_entity(target_chat_id)
print(target_chat)
client.run_until_disconnected()
