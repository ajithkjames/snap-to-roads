import csv


class FileHandler:

    def read_coordinates(self, file_path):

        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            coordinates_lst = []
            for row in csv_reader:
                if line_count >= 1:
                    coordinates_lst.append((row[0], row[1]))
                line_count += 1
            return "|".join("%s,%s" % tup for tup in coordinates_lst)

    def write_csv(self, points):

        with open('output.csv', mode='w') as output:
            output_writer = csv.writer(output, delimiter=',')
            output_writer.writerow(['latitude', 'longitude'])
            for point in points:
                output_writer.writerow(
                    [point.get('location').get('latitude'), point.get('location').get('longitude')])