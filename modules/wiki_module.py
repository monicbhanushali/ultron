import wikipedia


def get_page_details( page_name ):
    page_url = wikipedia.page(page_name).url
    return page_url


def get_wiki_content ( search_term ):
    search_item = wikipedia.search( search_term )
    if( len(search_item)==0):
        return "Nothing matched your query on wikipedia"
    else:
        try :
            print("Searching wikipedia for " + search_item[0])
            page_url = get_page_details( search_item[0])
            content = get_page_content( search_item[0] )
            formatted_response = "\n" + search_item[0] + " :\n" + content + "\n\nFor more details visit below wiki page:\n" + page_url
            return formatted_response
        except wikipedia.exceptions.DisambiguationError as e:
            print (e.options)

def get_page_content ( page_name ):
    return wikipedia.summary( page_name, sentences=3)

#print(get_wiki_content("jeff besos"))
#sugg = wikipedia.search("apple",suggestion=True)
#print(sugg)
    
