import requests

intelligence_dict = {}


def get_intelligence(hero_name):
    url = "https://superheroapi.com/api/2619421814940190/search/" + hero_name
    response = requests.get(url)
    for hero in response.json()["results"]:
        if hero["name"] == hero_name:
            intelligence = hero["powerstats"]["intelligence"]
            intelligence_dict[hero_name] = int(intelligence)


get_intelligence("Hulk")
get_intelligence("Captain America")
get_intelligence("Thanos")


value = list(intelligence_dict.values())
key = list(intelligence_dict.keys())
print(f"Самый умный: {key[value.index(max(value))]}")

