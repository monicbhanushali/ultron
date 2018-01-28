import weather_module as wthr
import country_module as country
import wiki_module as wiki
import quote_module as quote

print("Hi! I am ULTRON")

while True:
        print("\nHow can I help master?\n")
        user_input = input().lower()
        spiltted_input = user_input.split()
        if spiltted_input[0]=="check":
                if spiltted_input[1]=="weather":
                        result = wthr.get_weather_at(spiltted_input[2])
                        print(result)
        elif spiltted_input[0]=="country":
                        result = country.get_country_details(spiltted_input[1])
                        print(result)
        elif spiltted_input[0]=="wiki":
                        result = wiki.get_wiki_content(spiltted_input[1])
                        print(result)
        elif spiltted_input[0]=="quote":
                        print(quote.get_quote())
                
		
