import requests

class SmoothenRoads:

    def __init__(self):
        self.api_key = 'YOUR_KEY'

    def get_smoth_roads(self, coordinates):
        req = requests.get(
            'https://roads.googleapis.com/v1/snapToRoads?path=%s&interpolate=true&key=%s' %(coordinates, self.api_key))
        points = req.json().get('snappedPoints')
        return points
