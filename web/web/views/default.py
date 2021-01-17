from pyramid.view import view_config
from . .models import User, Session, Base, engine
from pyramid.response import Response
from pyramid.renderers import render_to_response
from pyramid.httpexceptions import HTTPFound


DBSession = Session(bind=engine)


@view_config(route_name='home')
def home_render(request):
    return render_to_response('templates/mytemplate.jinja2', {'success' : 'success'}, request=request)

@view_config(route_name='add')
def add_render(request):
    return render_to_response('templates/add.jinja2', {'success' : 'success'}, request=request)

@view_config(route_name='create')
def create_user(request):

    try:
        user = User(name=request.params['name'])
        DBSession.add(user)
        DBSession.commit()
        return HTTPFound(location='/users')
    except:
        return Response("Произошла ошибка")

@view_config(route_name='users')
def users_render(request):

    try:
        user_list = DBSession.query(User).all()
        DBSession.commit()
        return render_to_response('templates/users.jinja2', {'users' : user_list}, request=request)
    except:
        return Response("Произошла ошибка")

