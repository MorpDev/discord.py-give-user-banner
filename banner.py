req = await bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
banner_id = req["banner"]
if banner_id:
    banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
#31
