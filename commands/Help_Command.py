import nextcord
from nextcord import *
from nextcord.ext import commands
from nextcord import Interaction, SlashOption


embed_colour = 0x36393F
TESTING_GUILD_ID = 893564988936040548

class Help(commands.Cog):
    '''Help Command'''
    
    
    def __init__(self, bot):
        self.bot=bot
        
            
    @nextcord.slash_command(description="Shows Help Command")
    async def help(self,interaction: nextcord.Interaction):
        em = nextcord.Embed(title = "Scam Protector Bot Here for Assistance")
        em.description = "This help cog"
        em.color=embed_colour
        em.add_field(name="Help Command",value="`Shows this message!!`")
        em.add_field(name="Config Log_channel",value="`Configure your logs channel where logs would appear`")
        await interaction.response.send_message(embed=em)

        

    
        
        
        
def setup(bot):
    bot.add_cog(Help(bot))
    print('Help Commands - ✔')