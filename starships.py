import requests
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["starwars"]
starships = db["starships"]
characters = db["characters"]

def get_data(url):

    '''This function takes a URL and returns the JSON data from the API'''
    
    response = requests.get(url)
    return response.json()

def add_pilots(starship):

    '''This function takes a starship object and returns the IDs of its pilots. 
    If a pilot cannot be found in the characters collection, a new character document is created.'''
    
    pilots = starship["pilots"]
    pilot_ids = []
    for pilot in pilots:
        char = get_data(pilot)
        if char:
            char_name = char["name"]
            existing_char = characters.find_one({"name": char_name})
            if existing_char:
                pilot_ids.append(existing_char["_id"])
            else:
                char_id = characters.insert_one(char).inserted_id
                pilot_ids.append(char_id)
        else:
            pilot_ids.append(None)
    return pilot_ids

def add_starships_to_starwars_db() -> None:

    '''This function retrieves data from the SWAPI and stores it in the MongoDB database. 
    If a starship already exists in the database, its information is updated. 
    If a pilot cannot be found in the characters collection, their information is added to the characters collection.'''
    
    url = "https://swapi.dev/api/starships/"
    while url:
        data = get_data(url)
        if data:
            for starship in data["results"]:
                existing_starship = starships.find_one({"name": starship["name"]})
                if existing_starship:
                    pilot_ids = add_pilots(starship)
                    starships.update_one({"_id": existing_starship["_id"]}, {"$set": {"pilots": pilot_ids}})
                else:
                    pilot_ids = add_pilots(starship)
                    starship["pilots"] = pilot_ids
                    starships.insert_one(starship)
            url = data["next"]

add_starships_to_starwars_db()


