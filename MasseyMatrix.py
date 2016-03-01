import numpy
import json

__author__ = 'Jenna Schachner'


class Massey:

    def __init__(self, file_name):
        #self.initialize_components(file_name)
        self.initialize_components2(file_name)

    """ Read file and create M, teams, etc. """
    def initialize_components(self, f):
        json_d = []
        with open(f) as fp:
            for line in fp.read().split("\"}, "):
                # add line without brackets
                json_s = line.translate(None, '[')
                json_s = json_s.translate(None, ']')
                json_s += '"}'
                json_d.append(json_s)
        parsed_json = json.loads(json_d[0])
        print(parsed_json['date'])

    """ Reads file and creates M, teams, etc. """
    def initialize_components2(self, f):
        data = None
        self.teams = []
        try:
            # open the file
            with open(f) as data_file:
                data = json.load(data_file)
            # takes out each game in data
            for game in data:
                print(game)
                # extract team data
                home_inf = game['home']
                home_team = home_inf['team']
                away_inf = game['away']
                away_team = away_inf['team']
                self.teams.append(home_team)
                self.teams.append(away_team)
            print(self.teams)
        except ValueError:
            print("Invalid file.")

def main():
    m = Massey('2line.json')

if __author__ == 'Jenna Schachner':
    main()