
all_commands = [
"check weather [city/region/country] :- gives weather detail of specified city/region/country",
"country [country-name] :- Provides details about country",
"wiki [search_term] :- Searches infomation on wikipedia about given query.",
"quote :- Gets a random quote",
"help :- List all the commands supported by Ultron."
]

formatted_commands = ""

for index in range(len(all_commands)):
	formatted_commands = formatted_commands + str(index+1) + ")" + all_commands[index] + "\n"
	
def get_all_cmd():
	return formatted_commands