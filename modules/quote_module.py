import requests

def get_quote():
        url = "http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en"
        http_response = requests.get(url)
        if http_response.status_code == requests.codes.ok:
                quote_json = http_response.json()
                quote_text = quote_json['quoteText']
                quote_author = quote_json['quoteAuthor']
                return "\n" + quote_text + "\n - " + quote_author
        
        else:
                return "When something is important enough, you do it even if the odds are not in your favour. \n - Elon Musk"
