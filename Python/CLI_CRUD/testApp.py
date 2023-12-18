import pymongo
import sys

uri = "mongodb+srv://franmb:w6v6NtJtZmcgjIjo@mbdmora.7yhtkqz.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
try:
    client = pymongo.MongoClient(uri)

# Send a ping to confirm a successful connection
except pymongo.errors.ConfigurationError:
  print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
  sys.exit(1)

# Use the database dbSpeakers
db = client.dbSpeakers

