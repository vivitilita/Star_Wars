### Star Wars API Database


**Introduction**

This project is designed to store Star Wars data from SWAPI. This project uses the Python programming language and the PyMongo library to connect to a MongoDB database. The database contains information about characters and starships from the Star Wars universe. 


**Data Structure**

The database consists of two collections:

> characters: This collection contains information about Star Wars characters, such as their name, height, mass, hair_color, eye_color, birth year, gender, homeworld, films and species.

> starships: This collection contains information about Star Wars starships, such as their name, model, manufacturer, cost_in_credits, length, max_atmosphering_speed, crew, passengers, cargo_capacity, consumables, hyperdrive_rating, MGLT, starship_class, films, created and edited date, url and the IDs of their pilots.


**Code**

The code uses the ***PyMongo*** library to connect to a ***MongoDB*** database, and the ***Requests*** library to retrieve data from the SWAPI. The main.py file contains the following functions:

- get_data(url): 
  >This function takes a URL and returns the JSON data from the API.

- add_pilots(starship): 
  > This function takes a starship object and returns the IDs of its pilots. If a pilot cannot be found in the characters collection, a new character document is created.

- add_starships_to_starwars_db(): 
  > This function retrieves data from the SWAPI and stores it in the MongoDB database. If a starship already exists in the database, its information is updated. If a pilot cannot be found in the characters collection, their information is added to the characters collection.
