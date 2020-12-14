import os
import discord
from importlib import reload
from importlib import import_module
async def handle(execute, prefix, message, client):
	if message.content.startswith(prefix):
		command_and_args = message.content[len(prefix):]
		command_and_args = command_and_args.split(" ")
		command = command_and_args[0]
		args = command_and_args[1:]
		if command != "reload":
			for cmd in execute:
				if cmd.cmd == command or command in cmd.aliases:
					if cmd.typing == True:
						await message.channel.trigger_typing()
					if cmd.executable_by == "bot_owner":
						if message.author.id == 563980783828860944:
							await cmd.execute(command, args, message, client)
						else:
							await message.channel.send("You are not the bot owner!")
					else:
						if cmd.executable_by == "permissions":
							required_permissions = cmd.permissions
							if message.author.guild_permissions.is_superset(required_permissions):
								await cmd.execute(command, args, message, client)
							else:
								await message.channel.send("Missing permissions! Required permissions: " + ", ".join(cmd.permstxt))
						else:
							await cmd.execute(command, args, message, client)
		else:
			await message.channel.trigger_typing()
			if message.author.id == 563980783828860944:
				execute = []
				for filename in os.listdir('/home/container/commands'):
					if filename.endswith('.py'):
						module = "commands." + filename[0:-3]
						if module != "main":
							cmd = import_module(module, package=None)
							reload(cmd)
							execute.append(cmd)
				await message.channel.send("Success!")
			else:
				await message.channel.send("You are not the bot owner!")

async def cmdInit(execute):
	for filename in os.listdir('/home/container/commands'):
		if filename.endswith('.py'):
			module = "commands." + filename[0:-3]
			#print(module)
			if module != "main":
				cmd = import_module(module, package=None)
				execute.append(cmd)
