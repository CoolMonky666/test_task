import requests

def find_tallest_hero(gender, work):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.request("GET", url)
    result = response.json()
    max_height = 0
    id_hero = None
    for elements in result:
        appearance = elements.get("appearance")

        if appearance.get("gender") == gender:
            if (elements.get("work")).get("occupation") == "-":
                w = False
            else:
                w = True

            if w == work:
                height = appearance.get("height")
                height_in_cm = height[1]
                height_hero = float((height_in_cm.split())[0])

                if max_height < height_hero:
                    max_height = height_hero
                    id_hero = elements.get("id")

    return (id_hero, max_height)
#find_tallest_hero("Female", False)