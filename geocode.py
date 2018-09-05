import httplib2
import json
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "AG0EUDWGEVKMN4VGDOUOJWYGCLZEKQ45VDXCSTNJU1CRO44Q"
foursquare_client_secret = "HZUMRG5BA021G1JDGY2MO1SHTGKYM1KYPSWUQWFHPTHF2Q2C"


def getGeocodeLocation(inputString):
    google_api_key = "AIzaSyAkrXJtIU03j_RmhF-QrC7kYd2aH0addXg"
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%
           (locationString, google_api_key))
    h = httplib2.Http(".cache")
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    latitude = result['results'][0]['geometry']['latitude']['lng']
    longitude = result['results'][0]['geometry']['longitude']['lat']
    return (latitude, longitude)



def findARestraurant(mealType, location):
    print('hello')
    latitude, longitude = getGeocodeLocation(location)
    url = ('https://api.foursquare.com/v2/venues/search?ll=%s,%s&oauth_token=VFMXAWXY42OQX33014KIXLIQTY2KIDPTTPYUQUH0TO3XNS4T&v=20180718&query=%s'% (latitude, longitude, mealType))
    h = httplib2.Http(".cache")
    result = json.loads(h.request(url, 'GET')[1])
    
    if result['response']['venues']:
        restaurant = result['response']['venues']
        print(restaurant)
        

    
findARestraurant("Pizza", "TokyoJapan")
