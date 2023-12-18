import pymongo

def get_database():
    
   try:
      # Provide the mongodb atlas url to connect python to mongodb using pymongo
      CONNECTION_STRING = "mongodb+srv://franmb:w6v6NtJtZmcgjIjo@mbdmora.7yhtkqz.mongodb.net/?retryWrites=true&w=majority"

      # Create a connection using MongoClient
      client = pymongo.MongoClient(CONNECTION_STRING, serverSelectionTimeoutMS=5000)

      # Check if the database and collection exist
      db_name = 'dbSpeakers'
      collection_name = 'Speakers'

      db = client[db_name]
   
      if collection_name not in db.list_collection_names():
         print(f"Collection '{collection_name}' does not exist. Creating collection.")
         global collection
         collection = db[collection_name]
         fill_initial_data()
      else:
         collection = db[collection_name]

      print("Database and collection are ready.")

   except pymongo.errors.ServerSelectionTimeoutError:
        print("Unable to connect to the MongoDB server. Please check your connection.")

  
def fill_initial_data():
      
   # Sample data for 5 speakers
   speakers_data = [
        {'brand': 'Sony', 'model': 'SRS-X9', 'power': 100, 'impedance': 8},
        {'brand': 'Bose', 'model': 'SoundLink Revolve', 'power': 30, 'impedance': 4},
        {'brand': 'JBL', 'model': 'Charge 4', 'power': 50, 'impedance': 6},
        {'brand': 'Logitech', 'model': 'UE Megaboom', 'power': 40, 'impedance': 5},
        {'brand': 'Samsung', 'model': 'Level Box Slim', 'power': 20, 'impedance': 4},
    ]
   
   # Insert the speaker data into the collection
   result = collection.insert_many(speakers_data)

   # Print the inserted ID
   print(f'{len(result.inserted_ids)} speakers inserted with IDs: {result.inserted_ids}')


def insert_speaker(brand, model, power, impedance):

   # Create the speaker data
   speaker_data = {
      'brand': brand,
      'model': model,
      'power': power,
      'impedance': impedance
   }

   # Insert the speaker data into the collection
   result = collection.insert_one(speaker_data)

   # Print the inserted ID
   print(f'Speaker {brand} {model} inserted with ID: {result.inserted_id}')

def drop_speaker_by_brand_model(brand, model):

   # Delete the speaker with the given brand and model
   result = collection.delete_many({'brand': brand, 'model': model})

   if result.deleted_count > 0:
      print(f'Speakers with brand {brand} and model {model} deleted successfully')
   else:
      print(f'No speakers found with brand {brand} and model {model}')


def find_speaker_by_brand(brand):
   result = collection.find({'brand': brand})
   return list(result)

