import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import datetime
import asyncio

TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = 123456789012345678  # Ersetze mit der ID des gewünschten Kanals
IMAGE_PATHS = ["bild1.jpg", "bild2.jpg"]  # Ersetze mit den Dateinamen der Bilder im selben Ordner

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
scheduler = AsyncIOScheduler()

async def send_scheduled_message(messages):
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        for msg in messages:
            embed = discord.Embed(
                title=msg["title"],
                description=msg["description"],
                color=discord.Color.blue()
            )
            embed.set_footer(text=f"Gesendet am {datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
            
            delete_after = msg.get("delete_after", None)  # Zeit in Sekunden, nach der die Nachricht gelöscht wird
            
            if "image" in msg and msg["image"]:
                with open(msg["image"], "rb") as image_file:
                    image = discord.File(image_file, filename="image.jpg")
                    embed.set_image(url=f"attachment://image.jpg")
                    message = await channel.send(embed=embed, file=image)
            else:
                message = await channel.send(embed=embed)
            
            if delete_after:
                await asyncio.sleep(delete_after)
                await message.delete()

@bot.event
async def on_ready():
    print(f'Bot ist eingeloggt als {bot.user}')
    
    # Liste der geplanten Nachrichten
    scheduled_messages = [
        {
            "time": (0, 12, 0),
            "messages": [
                {"title": "Erste Nachricht", "description": "Dies ist die erste geplante Nachricht!", "image": "bild1.jpg", "delete_after": 60},
                {"title": "Zweite Nachricht", "description": "Hier ist eine zweite Nachricht mit Infos.", "image": "bild2.jpg", "delete_after": 120}
            ]
        },
        {
            "time": (4, 18, 30),
            "messages": [
                {"title": "Freitagsnachricht", "description": "Endlich Wochenende!", "image": None, "delete_after": 180}
            ]
        }
    ]
    
    for entry in scheduled_messages:
        day, hour, minute = entry["time"]
        scheduler.add_job(send_scheduled_message, 'cron', day_of_week=day, hour=hour, minute=minute, args=[entry["messages"]])
    
    scheduler.start()

bot.run(TOKEN)
