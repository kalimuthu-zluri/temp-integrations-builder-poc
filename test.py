import uncurl

msg = "curl --location 'https://pokeapi.co/api/v2/pokemon?offset=0&limit=10' --data ''"
msg = msg.replace("--location", "")

msg = uncurl.parse_context(msg)

print(msg)
