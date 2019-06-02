import sys

from snaproads import SmoothenRoads
from files.file_utils import FileHandler

roads_handler = SmoothenRoads()

file_handler = FileHandler()


class SmoothRoads:

    def get_route(self):

        #checking if input file path is passed
        if len(sys.argv) > 1:
            file_path = sys.argv[1]
        else:
            file_path = 'input.csv'

        #reading the file
        coordinates = file_handler.read_coordinates(file_path)

        #getting the adjusted coordinates from google snap to roads
        points = roads_handler.get_smoth_roads(coordinates)

        #writing the new coordinates to output.csv file
        file_handler.write_csv(points)



if __name__ == '__main__':
    roads = SmoothRoads()
    roads.get_route()