from pyramid.response import Response
from pyramid.view import view_config

from cornice import Service
from cornice.resource import resource, view



@resource(collection_path='/nba/ats/', path='/nba/ats/{year}')
class nba_ats(object):
  def __init__(self, request):
    self.request = request
    self.fakedata = [{'id':'2013'},{'id':'2014'},{'id':'2015'}]

  def collection_get(self):
    return {'d': self.fakedata}

  @view_config(renderer='json')
  def get(self):
    year = self.request.matchdict['year']
    if year == "2014":
      return {"d": static_nba_ats_data}
    else:
      return {"error": "year '%s' not found." % year}

static_nba_ats_data = [
  {"teamname": "Phoenix Suns", "ats_record": "25-11-1",  "win_percentage": 0.694},
  {"teamname": "Indiana Pacers", "ats_record": "25-12-0",  "win_percentage": 0.676},
  {"teamname": "Los Angeles Clippers", "ats_record": "23-16-0",  "win_percentage": 0.590},
  {"teamname": "Toronto Raptors", "ats_record": "22-15-0",  "win_percentage": 0.595},
  {"teamname": "Portland Trail Blazers", "ats_record": "21-16-0",  "win_percentage": 0.568},
  {"teamname": "Atlanta Hawks", "ats_record": "21-17-0",  "win_percentage": 0.553},
  {"teamname": "Charlotte Bobcats", "ats_record": "21-18-1",  "win_percentage": 0.538},
  {"teamname": "Dallas Mavericks", "ats_record": "21-18-0",  "win_percentage": 0.538},
  {"teamname": "Washington Wizards", "ats_record": "20-16-1",  "win_percentage": 0.556},
  {"teamname": "Minnesota Timberwolves", "ats_record": "20-18-0",  "win_percentage": 0.526},
  {"teamname": "Oklahoma City Thunder", "ats_record": "20-18-0",  "win_percentage": 0.526},
  {"teamname": "Houston Rockets", "ats_record": "20-18-2",  "win_percentage": 0.526},
  {"teamname": "San Antonio Spurs", "ats_record": "20-19-0",  "win_percentage": 0.513},
  {"teamname": "Boston Celtics", "ats_record": "20-20-0",  "win_percentage": 0.500},
  {"teamname": "Los Angeles Lakers", "ats_record": "19-18-1",  "win_percentage": 0.514},
  {"teamname": "Golden State Warriors", "ats_record": "19-19-1",  "win_percentage": 0.500},
  {"teamname": "Utah Jazz", "ats_record": "19-20-1",  "win_percentage": 0.487},
  {"teamname": "Denver Nuggets", "ats_record": "17-19-1",  "win_percentage": 0.472},
  {"teamname": "Brooklyn Nets", "ats_record": "17-20-0",  "win_percentage": 0.459},
  {"teamname": "Detroit Pistons", "ats_record": "17-21-0",  "win_percentage": 0.447},
  {"teamname": "Cleveland Cavaliers", "ats_record": "17-21-0",  "win_percentage": 0.447},
  {"teamname": "Sacramento Kings", "ats_record": "16-20-1",  "win_percentage": 0.444},
  {"teamname": "Memphis Grizzlies", "ats_record": "16-20-2",  "win_percentage": 0.444},
  {"teamname": "Chicago Bulls", "ats_record": "16-21-0",  "win_percentage": 0.432},
  {"teamname": "New Orleans Pelicans", "ats_record": "16-21-1",  "win_percentage": 0.432},
  {"teamname": "Philadelphia 76ers", "ats_record": "16-22-0",  "win_percentage": 0.421},
  {"teamname": "Miami Heat", "ats_record": "16-22-0",  "win_percentage": 0.421},
  {"teamname": "Orlando Magic", "ats_record": "16-22-1",  "win_percentage": 0.421},
  {"teamname": "New York Knicks", "ats_record": "16-22-0",  "win_percentage": 0.421},
  {"teamname": "Milwaukee Bucks", "ats_record": "13-25-0",  "win_percentage": 0.342, "test": False}
]