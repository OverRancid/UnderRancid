import discord
import random
from discord.ext import commands


class Card_Jitsu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def jitsu_help(self, ctx):
        embed=discord.Embed(title="Card Jitsu", description="Card Jitsu - Discord Edition ( based off the popular Club Penguin mini-game ) Bot Name - UnderRancid.py, created by OverRancid#0590")
        embed.add_field(name="How To Play:", value=" The game works similar to Rock Papers Scissors except with Fire ( :fire: ), Ice ( :ice_cube: ), and Water ( :droplet: ).", inline=False)
        embed.add_field(name="឵឵", value="Fire defeats Ice, Ice defeats Water, and Water defeats Fire. If both players play the same element, the card with the higher numerical value wins the round. Note that the numerical value only matters if both players play the same element .", inline=False)
        embed.add_field(name="឵឵", value=" To challenge a user, use the command ~play @[mention user]. The user reacts to the bot's message with either a :white_check_mark: to accept or :negative_squared_cross_mark: to decline the challenge.", inline=False)
        embed.add_field(name="឵឵", value="The bot DM's you your cards as a reaction message. React to the message accordingly to decide what card you wish to play. ", inline=False)
        embed.add_field(name="឵឵", value=" If the bot does not respond after both users have played, the person who was challenged must re-react their card as the bot reads the  challenger's card first. (This does not in any way affect the outcome of the round).", inline=False)
        embed.add_field(name="឵឵", value="When a round is won, the winnings are displayed as [user]'s winnings: [winning card element].", inline=False)
        embed.add_field(name="឵឵", value=" Cards that have been played once are automatically removed from the players roster and the player is given a new card.", inline=False)
        embed.add_field(name="឵឵", value=" In order to win, a player is required to either acquire 3 wins with the same element or one win each with all three elements.", inline=False)
        embed.set_footer(text=f"credits : @VivviTheGreat#9532 ")
        await ctx.send(embed=embed)

    @commands.command()
    async def challenge(self , ctx , member : discord.Member ):
        channel = ctx.channel
        embed = discord.Embed(title = "Jitsu Match",
                              description=f"{member.mention}, you have been challenged to a Card Jitsu match by {ctx.author.mention}" ,
                              color = 0xa2a2fe)
        message = await channel.send(embed = embed)

        await message.add_reaction('✅')
        await message.add_reaction('❎')

        def check(reaction, user):
            return user == member and str(reaction.emoji) in ['✅','❎']


        reaction, user = await self.client.wait_for('reaction_add', check=check)
        if reaction.emoji == "❎":
            embed = discord.Embed(title= "Challenged declined" , color = 0xFF0000)
            await channel.send(embed = embed)

        elif reaction.emoji == '✅' :
            cards = ['` 1🧊` ','` 2🧊` ','` 3🧊` ','` 4🧊` ','` 5🧊` ','` 6🧊` ','` 7🧊` ','` 8🧊` ','` 9🧊` ','`10🧊` ',
                     '` 1💧` ','` 2💧` ','` 3💧` ','` 4💧` ','` 5💧` ','` 6💧` ','` 7💧` ','` 8💧` ','` 9💧` ','`10💧` ',
                     '` 1🔥` ','` 2🔥` ','` 3🔥` ','` 4🔥` ','` 5🔥` ','` 6🔥` ','` 7🔥` ','` 8🔥` ','` 9🔥` ','`10🔥` '
                     ]
            handA = []
            handB = []
            p = 29
            for i in range(10):
                x = random.randint(0,p)
                if i > 4 :
                    handA.append(cards[x])
                    cards.remove(cards[x])
                    p -= 1
                else :
                    handB.append(cards[x])
                    cards.remove(cards[x])
                    p -= 1
            winner = None
            loser = None
            iceA = []
            iceB = []
            waterA = []
            waterB = []
            fireA = []
            fireB = []

            while winner == None :
                for i in range(2):
                    x = random.randint(0,p)
                    if i > 0 :
                        handA.append(cards[x])
                        cards.remove(cards[x])
                        p -= 1
                    else:
                        handB.append(cards[x])
                        cards.remove(cards[x])
                        p -= 1


                embedA = discord.Embed(title = "Your cards are :",
                                       description = "".join(handA),
                                       color =  0xa2a2fe
                                       )

                embedB= discord.Embed(title = "Your cards are :",
                                      description = "".join(handB),
                                      color =  0xa2a2fe
                                      )

                playA = ""
                playB = ""

                embed = discord.Embed(title = "Cards have been dealt" , color = 0x00FF00)
                await ctx.send(embed = embed)

                reactions = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣"]

                messageA = await ctx.author.send(embed = embedA)
                def checkA(reaction , user):
                    return user == ctx.author and str(reaction.emoji) in reactions

                messageB = await member.send(embed = embedB)
                def checkB(reaction , user):
                    return user == member and str(reaction.emoji) in reactions

                for i in range(6):
                    await messageA.add_reaction(reactions[i])
                    await messageB.add_reaction(reactions[i])

                reaction , user = await self.client.wait_for("reaction_add", check = checkA)
                for i in range(6):
                    if reaction.emoji == str(reactions[i]):
                        playA = str(handA[i])
                        handA.remove(handA[i])

                reaction , user = await self.client.wait_for("reaction_add", check = checkB)
                for i in range(6):
                    if reaction.emoji == str(reactions[i]):
                        playB = str(handB[i])
                        handB.remove(handB[i])

                embed=discord.Embed(color = 0x00FF00)
                embed.add_field(name=f"{ctx.author} played:", value=playA, inline=True)
                embed.add_field(name=f"{member} played:", value=playB, inline=True)
                await channel.send(embed=embed)

                elementA = playA[3:4]
                elementB = playB[3:4]

                numberA = int(playA[1:3])
                numberB = int(playB[1:3])

                if elementA == "🔥" and elementB == "🧊":
                    fireA.append("🔥")

                elif elementA == "🧊" and elementB == "💧":
                    iceA.append("🧊")

                elif elementA == "💧" and elementB == "🔥":
                    waterA.append("💧")

                elif elementB == "🔥" and elementA == "🧊":
                    fireB.append("🔥")

                elif elementB == "🧊" and elementA == "💧":
                    iceB.append("🧊")

                elif elementB == "💧" and elementA == "🔥":
                    waterB.append("💧")

                elif elementA == elementB :
                    if numberA > numberB:
                        if elementA == "🔥":
                            fireA.append("🔥")
                        elif elementA == "🧊":
                            iceA.append("🧊")
                        else:
                            waterA.append("💧")

                    else:
                        if elementB == "🔥":
                            fireB.append("🔥")
                        elif elementB == "🧊":
                            iceB.append("🧊")
                        else:
                            waterB.append("💧")


                embed = discord.Embed(color = 0x0000FF)
                embed.add_field(name=f"{ctx.author}'s winings: ", value = "".join(fireA) + "".join(iceA) + "".join(waterA) + "‎‎‎‎‎‎‎", inline=True)
                embed.add_field(name=f"{member}'s winings: ", value = "".join(fireB) + "".join(iceB) + "".join(waterB) + "‎‎‎", inline=True)
                await channel.send(embed=embed)

                if len(fireA) == 3 or len(iceA) == 3 or len(waterA) == 3:
                    winner = ctx.author
                    loser = member

                elif len(fireA) >= 1 and len(iceA) >= 1 and len(waterA) >= 1:
                    winner = ctx.author
                    loser = member

                elif len(fireB) == 3 or len(iceB) == 3 or len(waterB) == 3:
                    winner = member
                    loser = ctx.author

                elif len(fireB) >= 1 and len(iceB) >= 1 and len(waterB) >= 1:
                    winner = member
                    loser = ctx.author

                if winner != None :
                    embed = discord.Embed(title = str(winner) , description = "defeated " + str(loser) + " in a jitsu match" , color = 0x080808)
                    await channel.send(embed = embed)

                else :
                    continue


def setup(client):
    client.add_cog(Card_Jitsu(client))
