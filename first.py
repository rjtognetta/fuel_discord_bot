# (c) 2020, Lucas Benedito <llucasdias@icloud.com>
# (c) 2020, Rodrigo Tognetta <rjtognetta@me.com>

import discord
import os
from fuel import calc_fuel


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
          return

        if message.content.startswith('!gas'):
          discMsg = message.content.split(' ')
          failCheck = False
          n = 1
          for n in range(1,5):
            try:
              tmpN = float(discMsg[n])
            except:
              failCheck = True
          if not failCheck:
            stintTime = float(discMsg[1])
            lapTime = float(discMsg[2])
            fuelLap = float(discMsg[3])
            tankCap = float(discMsg[4])
            fuelOut = calc_fuel(stintTime, lapTime, fuelLap, tankCap)
            await message.channel.send(message.author.mention + " " + fuelOut)
          else:
            await message.channel.send(message.author.mention + ', Sorry, but there was an error with your request. Type !help to see the correct syntax needed.')

        if message.content.startswith('!help'):
          helpMsg = f"""
Usage:     !gas (Race/Stint Length in Minutes) (Lap Time) (Fuel Per Lap) (Tank Capacity)
Example: !gas 30 1.56 3.1 90"""
          await message.channel.send(message.author.mention + " " + helpMsg)

def main():
    client = MyClient()
    client.run(os.environ['TOKEN'])

if __name__ == "__main__":
    main()