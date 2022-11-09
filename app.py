from columnar import columnar
import mysql.connector
import discord

from sellix_api import SellixApi



from discord.ext import commands

from dotenv import dotenv_values


vars = dotenv_values(".env")

whitelisted = vars["WHITELIST_IDS"]
syntax = vars["SYNTAX"]
TOKEN = vars["TOKEN"]


client = commands.Bot(intents=discord.Intents.all() , command_prefix=syntax , description='Im a big manager here', help_command = None)




config = {
    'user': vars["USERNAME"],
    'password': vars["PASSWORD"],
    'host': vars["HOSTNAME"],
    'database': vars["DATABASE"],
    'raise_on_warnings': True
}









try:

    
    cnx = mysql.connector.connect(**config)
    

    cursor = cnx.cursor()
    
    print("MySQL Connection Created Successfully")
except Exception as e:
    print("Error at:")
    print(e)
    print()
    print("Exiting...")
    exit()

def exec(query, value):
    try:
        
        cursor.execute(query, value)
        return cursor.fetchall()
    except Exception as e:
        return str(e)

        # return ['ERR', e]


def exec(query, value):
    try:
        cursor.execute(query, value)
        
        return cursor.fetchall()
    except Exception as e:
        return str(e)

        # return ['ERR', e]

@client.command()
async def help(ctx):


    if str(ctx.author.id) in whitelisted:

            await ctx.message.delete()
            embed = discord.Embed(description=f'Youre a good little support kitten, you get to stay alive',color=discord.Color.purple())
            embed = embed.set_author(name="George Floyd", icon_url="https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/rockcms/2022-10/210704-george-floyd-mb-1922-bd9085.jpg")
            await ctx.send(embed=embed)
    else:
            embed = discord.Embed(description=f'Only help I can give you is. Down the road, not across the street. Fucking twink.',color=discord.Color.purple())
            embed = embed.set_author(name="George Floyd", icon_url="https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/rockcms/2022-10/210704-george-floyd-mb-1922-bd9085.jpg")
            await ctx.send(embed=embed)






@client.command()
async def bonk(ctx, member : discord.Member):




            await ctx.message.delete()
            embed = discord.Embed(description=f'I just sent {member} to horny jail. Get ready for that Floyd BBC',color=discord.Color.purple())
            embed = embed.set_image(url="https://media.tenor.com/TKbDxDPCkegAAAAC/horny-jail-go-to-horny-jail.gif")
            embed = embed.set_author(name="George Floyd", icon_url="https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/rockcms/2022-10/210704-george-floyd-mb-1922-bd9085.jpg")
            await ctx.send(embed=embed)









    


@client.command()
async def adduser(ctx, arg1, arg2):

    
    #checks if user is authorized to use command
    if str(ctx.author.id) in whitelisted:
            #connects to mysql database
        
            cnx = mysql.connector.connect(**config)
            #closes connection to renew
            cnx.close()
            
            cnx = mysql.connector.connect(**config)
            #initilizing cursor
            cursor = cnx.cursor()
            
            sql = "INSERT INTO user (user_name, user_password, user_status) VALUES (%s, %s, '1');"
            val = (arg1, arg2)
            #executes quary
            cursor.execute(sql, val)
            cnx.commit()
            #closes connection
            cnx.close()
            cursor.close()
            
            await ctx.message.delete()
            embed = discord.Embed(description=f'Successfully added {arg1} to the database for Release Live',color=discord.Color.purple())
            embed = embed.set_author(name="George Floyd", icon_url="https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/rockcms/2022-10/210704-george-floyd-mb-1922-bd9085.jpg")
            
            await ctx.send(embed=embed)
    else:
            embed = discord.Embed(description=f'You must be mentally retarded I swear, monkeyboy. Unblack yoursef',color=discord.Color.purple())
            embed = embed.set_author(name="George Floyd", icon_url="https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/rockcms/2022-10/210704-george-floyd-mb-1922-bd9085.jpg")
            
            await ctx.send(embed=embed)


#reset hwid of user command
@client.command()
async def reset(ctx, arg1, arg2):


    if str(ctx.author.id) in whitelisted:
            
            cnx = mysql.connector.connect(**config)
            
            cnx.close()
            
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
            
            
            sql = "UPDATE user SET user_password = %s WHERE user_name = %s"
            val = (arg2,arg1)
            cursor.execute(sql, val)

            cnx.commit()

            cnx.close()
            cursor.close()




            
            
            await ctx.message.delete()
            embed = discord.Embed(description=f'Successfully reset hwid of {arg1}',color=discord.Color.purple())
            embed = embed.set_author(name="George Floyd", icon_url="https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/rockcms/2022-10/210704-george-floyd-mb-1922-bd9085.jpg")
            await ctx.send(embed=embed)
    else:
            embed = discord.Embed(description=f'You must be mentally retarded I swear.',color=discord.Color.purple())
            embed = embed.set_author(name="George Floyd", icon_url="https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/rockcms/2022-10/210704-george-floyd-mb-1922-bd9085.jpg")
            await ctx.send(embed=embed)



#delete user
@client.command()
async def delete(ctx, arg1):


    if str(ctx.author.id) in whitelisted:
            
            cnx = mysql.connector.connect(**config)
            
            cnx.close()
            
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
            
            
            sql = "DELETE FROM user WHERE user_name = %s"
            val = (arg1,)
            cursor.execute(sql, val)
            
            cnx.commit()

            cnx.close()
            cursor.close()
            

    


            
            
            await ctx.message.delete()
            embed = discord.Embed(description=f'{arg1} got beamed, what a retard',color=discord.Color.purple())
            embed = embed.set_author(name="George Floyd", icon_url="https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/rockcms/2022-10/210704-george-floyd-mb-1922-bd9085.jpg")
            await ctx.send(embed=embed)
    else:
            embed = discord.Embed(description=f'You must be mentally retarded I swear.',color=discord.Color.purple())
            embed = embed.set_author(name="George Floyd", icon_url="https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/rockcms/2022-10/210704-george-floyd-mb-1922-bd9085.jpg")
            await ctx.send(embed=embed)
            

#ban user command
@client.command()
async def ban(ctx, arg1):


    if str(ctx.author.id) in whitelisted:
            
            cnx = mysql.connector.connect(**config)
            
            cnx.close()
            
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
           
            
            sql = "UPDATE user SET user_status = '2' WHERE user_name = %s"
            val = (arg1,)
            cursor.execute(sql, val)
            
            cnx.commit()

            cnx.close()
            cursor.close()



            
            
            await ctx.message.delete()
            embed = discord.Embed(description=f'{arg1} got blasted to the ban zone + I fucked your wife',color=discord.Color.purple())
            embed = embed.set_author(name="George Floyd", icon_url="https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/rockcms/2022-10/210704-george-floyd-mb-1922-bd9085.jpg")
            
            await ctx.send(embed=embed)
    else:
            embed = discord.Embed(description=f'You must be mentally retarded I swear.',color=discord.Color.purple())
            embed = embed.set_author(name="George Floyd", icon_url="https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/rockcms/2022-10/210704-george-floyd-mb-1922-bd9085.jpg")
            
            await ctx.send(embed=embed)


#ban user command
@client.command()
async def unban(ctx, arg1):


    if str(ctx.author.id) in whitelisted:
            #opens mysql connection
            cnx = mysql.connector.connect(**config)
            #closes mysql connection
            cnx.close()
            #opens mysql connection
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
            
            #sends quary to update set brackets in the database
            sql = "UPDATE user SET user_status = '1' WHERE user_name = %s"
            val = (arg1,)
            cursor.execute(sql, val)
            #execute quary through cursor

            cnx.commit()
            #close mysql connection
            cnx.close()
            cursor.close()

            


            
            
            await ctx.message.delete()
            embed = discord.Embed(description=f'{arg1} got unbeamed, welcome back + I unfucked your wife',color=discord.Color.purple())
            embed = embed.set_author(name="George Floyd", icon_url="https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/rockcms/2022-10/210704-george-floyd-mb-1922-bd9085.jpg")
            
            await ctx.send(embed=embed)
    else:
            embed = discord.Embed(description=f'You must be mentally retarded I swear.',color=discord.Color.purple())
            embed = embed.set_author(name="George Floyd", icon_url="https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/rockcms/2022-10/210704-george-floyd-mb-1922-bd9085.jpg")
            
            await ctx.send(embed=embed)
            



    


sellix_api = SellixApi('sellix_api')





@client.command()

async def redeem(ctx, sellix_code):

    discord_username = ctx.author

    discord_id = ctx.author.id

    order_id = sellix_code

    # check if the user already exists in the database
    file = open('users.json', 'r')
    data = file.read()

    if order_id in data:
        await ctx.message.delete()
        embed = discord.embeds.Embed(title='Error', description='You have already redeemed this code', color=0xFF0000)
        await ctx.send(embed=embed)
        
        return


    # lets authorize the user now
    if len(order_id) > 0:
        auth = sellix_api.authorize(order_id)
    else:
        embed = discord.embeds.Embed(title='Error', description='No order id provided!', color=0xFF0000)
        await ctx.message.delete()
        await ctx.send(embed=embed)
        
        return


    if auth == 'beta':
        await ctx.message.delete()
        # send the message to the user

        embed = discord.embeds.Embed(title='Success', description='You have been granted Beta, Enjoy ' + ctx.author.name , color=0x4287f5)
        await ctx.send(embed=embed)
        

        # set his role
        role = discord.utils.get(discord_username.guild.roles, name='Beta')
        await discord_username.add_roles(role)

        await ctx.author.send(f"**{'You have been granted Beta'}**")
        # lets make an object real quick

        user = {
            'discord_id': discord_id,
            'order_id': order_id
        }

        # then we write it to file

        with open('users.json', 'a') as outfile:
            outfile.write(str(user))


    elif auth == 'live':
        await ctx.message.delete()
        # send the message to the user

        embed = discord.embeds.Embed(title='Success', description='You have been granted Live, Enjoy ' + ctx.author.name , color=0x4287f5)
        await ctx.send(embed=embed)
        

        # set his role
        role = discord.utils.get(discord_username.guild.roles, name='Live')
        await discord_username.add_roles(role)

        await ctx.author.send(f"**{'You have been granted Live'}**")
        # lets make an object real quick

        user = {
            'discord_id': discord_id,
            'order_id': order_id
        }

        # then we write it to file

        with open('users.json', 'a') as outfile:
            outfile.write(str(user))
    elif auth == 'upgrade':
      # send the message to the user
      
                  
                  

        role = discord.utils.get(discord_username.guild.roles, name='Beta')
        
        roler = discord.utils.get(discord_username.guild.roles, name='Live')

        if roler in ctx.author.roles:
            await ctx.message.delete()
            role = discord.utils.get(discord_username.guild.roles, name='Beta')
            embed = discord.embeds.Embed(title='Success', description='You have been upgraded to Beta, Enjoy ' + ctx.author.name , color=0x4287f5)
            await ctx.send(embed=embed)
            

            # set his role

            await discord_username.add_roles(role)
            await discord_username.remove_roles(roler)

            await ctx.author.send(f"**{'You have been upgraded from Live to Beta.'}**")
            

            # lets make an object real quick

            user = {
                'discord_id': discord_id,
                'order_id': order_id
            }

            # then we write it to file

            with open('users.json', 'a') as outfile:
                outfile.write(str(user))
        else:
            await ctx.message.delete()
            embed = discord.embeds.Embed(title='Error', description='To upgrade you need to own Live first ' + str(ctx.author.name) , color=0x4287f5)
            await ctx.send(embed=embed)



    elif auth == 'error':
        embed = discord.embeds.Embed(title='Error', description='Invalid Key!', color=0xFF0000)
        await ctx.message.delete()
        
        
        return

    elif auth == 'pending':
        embed = discord.embeds.Embed(title='Error', description='Boy, your order is not completed.', color=0xffae00)
        await ctx.message.delete()
        await ctx.send(embed=embed)
        
        return

    else:
        embed = discord.embeds.Embed(title='Error', description='Something went wrong....', color=0xFF0000)
        await ctx.message.delete()
        await ctx.send(embed=embed)
        
        return







#debug information on load
@client.event
async def on_ready():
    print(f"Bot | Status:   Operational")
    print(f"Bot | ID:       {format(client.user.id)}")
    print(f"Bot | Name:     {format(client.user.name)}")
    print(f"Bot | Guilds:   {len(client.guilds)}")
    print(f"Bot Configurations set to:\n Your moms place")
    print(f"Bot is ready to use")
    # ? Custom Activity
    await client.change_presence(
        status=discord.Status.dnd,
        activity=discord.Activity(type=discord.ActivityType.listening, name="Big Daddy Zaptons Orders" ))


client.run(TOKEN)
