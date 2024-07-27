import requests

while(input() != 'q'):
    joke_responce = requests.get("https://official-joke-api.appspot.com/jokes/random")
    jokes_data = joke_responce.json()
    print(jokes_data["setup"])
    print(jokes_data["punchline"])
    if(input() == 'n'):
        pass
