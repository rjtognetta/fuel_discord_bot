# (c) 2020, Lucas Benedito <llucasdias@icloud.com>

import discord
from fuel import calc_fuel


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.startswith('!fuel'):
            print(message.content.split('!fuel '))
            #fuelOut = calc_fuel(stintTime, lapTime, fuelLap, tankCap)
            #await message.channel.send(fuelOut)

def main():
    client = MyClient()
    client.run(os.getenv('TOKEN'))

if __name__ == '__main__':
    main()