import googlemaps


API_key = 'AIzaSyAtJ7llR6PgPC5skxCee2ao4umEAaXBfg8'
client = googlemaps.Client(API_key)

print(client.geolocate())

