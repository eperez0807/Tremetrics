from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from cornice import Service
from cornice.resource import resource, view

from .models import (
  DBSession,
  MyModel,
  )


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
  try:
    one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
  except DBAPIError:
    return Response(conn_err_msg, content_type='text/plain', status_int=500)
  return {'one': one, 'project': 'Tremetrics'}

conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_Tremetrics_db" script
    to initialize your database tables.  Check your virtual 
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

@view_config(route_name='test_route')
def test_route(request):
  return Response(request.matchdict['value'])


hello = Service(name='hello', path='/cornice/service', description="Testing cornice integration")
@hello.get()
def get_info(request):
  """Returns Hello in JSON."""
  return {'Hello': 'World'}


@resource(collection_path='/cornice/resource', path='/cornice/resource/{ID}')
class test_resource(object):
  def __init__(self, request):
    self.request = request
    self.fakedata = [{'id':'001'},{'id':'002'},{'id':'003'}]

  def collection_get(self):
    return {'d': self.fakedata}

  def get(self):
    ID = self.request.matchdict['ID']
    result = filter(lambda item: item['id']==ID, self.fakedata)
    if result != []:
      return result[0]
    else:
      return "ID '%s' not found." % ID

