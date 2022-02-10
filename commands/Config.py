import nextcord
from nextcord import *
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import pymongo
from nextcord.abc import GuildChannel

mongodbai = pymongo.MongoClient('mongodb+srv://mira:immune@mira.bqrza.mongodb.net/mira?retryWrites=true&w=majority')
dbclient = mongodbai['scam']
log_collection = dbclient['logs_chan']
whitelisted = dbclient['whitelisted']
not_found = "Not Set"
embed_colour = 0x36393F

TESTING__GUILD = 893564988936040548

class Config(commands.Cog):
    '''Config Commands'''
    
    
    def __init__(self, bot):
        self.bot=bot
        
#####################################################################################################################################################
#####################################################################################################################################################   
#####################################################################################################################################################   
#####################################################################################################################################################   
     
    @nextcord.slash_command()
    async def config(self,interaction: nextcord.Interaction):
        """
        This is the config slash command that will be the prefix of all commands below.
        This will never get called since it has subcommands.
        """
        pass
 
#####################################################################################################################################################  
#####################################################################################################################################################   
#####################################################################################################################################################   
#####################################################################################################################################################   

    @config.subcommand(description="Config Logs Channel!!")
    async def log_channel(self,
                              interac : Interaction,
                              channel: GuildChannel = SlashOption(
                                                            name="channel",
                                                            channel_types=[ChannelType.text, ChannelType.public_thread],
                                                            description="Choose a channel to send embed",
                              ),
        ):
        if interac.user.guild_permissions.manage_messages:
            dictlol = {'_id': interac.guild.id , 'channel_id': channel.id}
            already_t = log_collection.find_one({'_id': int(interac.guild.id)})
            if already_t is None:
                log_collection.insert(dictlol)
                await interac.response.send_message(f'> q (￣_,￣ ) Logs channel set to {channel.mention}',ephemeral=True)
                await channel.send('> **This Channel is set as Logs Channel for Scam Protection Bot** (ˉ▽￣～)')
                print(f'Logs channel command set in {interac.guild.name} to {channel.id}')
            
            if already_t is not None:
                log_collection.update_one({"_id": interac.guild.id}, {"$set": {"channel_id": int(channel.id)}})
                await interac.response.send_message(f"logs channel updated to {channel.mention} from now on logs would appear there!!",ephemeral=True)
                await channel.send(f"> **This Channel is now set as Logs Channel for Scam Protection Bot** (ˉ▽￣～)")
                print(f"{interac.guild.name} updated logs channnel to {channel.id}")
            
        else:
            await interac.response.send_message("Hey There!! You Are Missing required permissions to execute this command!!",ephemeral=True)

#####################################################################################################################################################   
#####################################################################################################################################################   
#####################################################################################################################################################   
#####################################################################################################################################################   

    # @config.subcommand(description="Config Whitelisted Bypass Roles!!")
    # async def whitelist(
    #     self,
    #     interac:Interaction,
    #     role ):
        
    #     role__id = ''.join(x for x in role if x.isdigit())
        
        
        
    #     if interac.user.guild_permissions.manage_messages:
    #         already_t = whitelisted.find_one({'_id': int(interac.guild.id)})
    #         if already_t is None:
    #             w_role = {'_id': interac.guild.id , 'role_id': role__id}
    #             whitelisted.insert(w_role)
    #             await interac.response.send_message(f"Successfully Whitelisted {role} for scam protection ,Now they can bypass protection",ephemeral=True)
    #             print(f"{interac.guild.name} has whitelisted {role} for Bypass of protection!!")

    #         if already_t is not None:   
    #             whitelisted.update_one({"_id": interac.guild.id}, {"$set": {"role_id": role__id}})
    #             await interac.response.send_message(f"Successfully updated whitelisted {role} for scam protection ,Now they can bypass protection!!",ephemeral=True)
    #             print(f"{interac.guild.name} has updated whitelist {role} for Bypass of protection!!")

    #     else:
    #         await interac.response.send_message("Hey There!! You Are Missing required permissions to execute this command!!",ephemeral=True)    
        
#####################################################################################################################################################   
#####################################################################################################################################################   
#####################################################################################################################################################   
#####################################################################################################################################################   

        
    @config.subcommand(description="Details for already configured stuff in server")
    async def info(
        self,
        interac : Interaction,
    ):
        chan_f = log_collection.find_one({'_id': int(interac.guild.id)})
        # role_f = whitelisted.find_one({'_id': int(interac.guild.id)})
        
        if chan_f is None:
            await interac.response.send_message(f"Server Not found in database try using config commands and configure your server!!",ephemeral=True)

        # if role_f is None:
        #         chan = log_collection.find({'_id': int(interac.guild.id)})
        #         chan_info =  chan[0]["channel_id"]
        #         em = nextcord.Embed(title = "Info About Configurations of the server")
        #         em.description="Below are the Configurations for this server"
        #         em.color = embed_colour
        #         em.add_field(name="Log Channel",value= f"<#{chan_info}>")
        #         em.add_field(name="Whitelisted Role",value= "`Not Set`")
        #         await interac.response.send_message(embed=em)

        else:
            chan = log_collection.find({'_id': int(interac.guild.id)})
            # role_ = whitelisted.find({'_id': int(interac.guild.id)})

            
            if chan is None:
                await interac.response.send_message(f"Server Not found in database try using config commands and configure your server!!",ephemeral=True)
            
            else:
                chan_info =  chan[0]["channel_id"]
                em = nextcord.Embed(title = "Info About Configurations of the server")
                em.description="Below are the Configurations for this server"
                em.color = embed_colour
                em.add_field(name="Log Channel",value= f"<#{chan_info}>")
                # em.add_field(name="Whitelisted Role",value= "`Not Set`")
                await interac.response.send_message(embed=em)
            
            # else:
            #     chan_info =  chan[0]["channel_id"]
            #     role_info = role_[0]["role_id"]
            #     em = nextcord.Embed(title = "Info About Configurations of the server")
            #     em.description="Below are the Configurations for this server"
            #     em.color = embed_colour
            #     em.add_field(name="Log Channel",value= f"<#{chan_info}>")
            #     # em.add_field(name="Whitelisted Role",value= f"{role_info}")
            #     await interac.response.send_message(embed=em)

                
        
#####################################################################################################################################################   
#####################################################################################################################################################   
#####################################################################################################################################################   
#####################################################################################################################################################   
        
        
        

        
        
        
        
        
        
        
        
        
        
        
def setup(bot):
    bot.add_cog(Config(bot))
    print('Config Commands - ✔')