import discord
from discord.ext import commands
import random
from ayarlar import ayarlar

intents = discord.Intents.default()
intents.message_content = True  # Komutların çalışması için gerekli
bot = commands.Bot(command_prefix='/', intents=intents)

veritabani = {
    "plastik şişe": {"tür": "geri dönüştürülebilir", "süre": "450 yıl"},
    "cam şişe": {"tür": "geri dönüştürülebilir", "süre": "4000 yıl"},
    "pil": {"tür": "özel atık kutusu", "süre": "100 yıl"},
    "muz kabuğu": {"tür": "organik atık", "süre": "1 hafta"},
    "çikolata ambalajı": {"tür": "çöp", "süre": "200 yıl"},
    "kağıt": {"tür": "geri dönüştürülebilir", "süre": "2-5 ay"},
    "teneke kutu": {"tür": "geri dönüştürülebilir", "süre": "200-500 yıl"}
}

tavsiyeler = [
    "Plastik yerine cam ya da metal kullanmaya çalış.",
    "Bez çanta taşı, plastik poşetten uzak dur.",
    "Geri dönüşüm kutularını etiketle, herkes için kolaylaştır.",
    "Gıda artıklarını kompost yapmayı dene!",
    "Elektronik atıkları asla çöpe atma, geri dönüşüm merkezine götür."
]

@bot.event
async def on_ready():
    print(f'{bot.user} çalışıyor!')

@bot.command()
async def ayristir(ctx, *, item):
    item = item.lower()
    if item in veritabani:
        tür = veritabani[item]["tür"]
        await ctx.send(f"♻️ **{item}** -> {tür}")
    else:
        await ctx.send(f"🤷 Bilgim yok: **{item}**")

@bot.command()
async def bilgi(ctx, *, item):
    item = item.lower()
    if item in veritabani:
        süre = veritabani[item]["süre"]
        await ctx.send(f"🕒 **{item}** doğada yaklaşık {süre} içinde yok olur.")
    else:
        await ctx.send(f"🔍 Bu maddenin doğadaki çözünme süresini bilmiyorum: **{item}**")

@bot.command()
async def tavsiye(ctx):
    öneri = random.choice(tavsiyeler)
    await ctx.send(f"🌿 Tavsiye: {öneri}")

@bot.command()
async def yardim(ctx):
    await ctx.send("""
🛠️ Kullanabileceğin komutlar:
`/ayristir <eşya>` – Eşyanın türünü söyler.
`/bilgi <eşya>` – Ne kadar sürede doğada kaybolur?
`/tavsiye` – Geri dönüşüm hakkında rastgele bir öneri.
`/yardim` – Komut listesini gösterir.
""")


bot.run(ayarlar["TOKEN"])