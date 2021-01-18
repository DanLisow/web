from pyramid.view import view_config
from . .models import Note, Session, Base, engine
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
        title = request.params['title']
        text = request.params['text']
        note = Note(title=title, text=text)
        DBSession.add(note)
        DBSession.commit()
        return HTTPFound(location='/notes')
    except:
        return Response("Произошла ошибка")

@view_config(route_name='delete')
def delete_user(request):

    try:
        note = DBSession.query(Note).filter(Note.id == request.params['id']).first()
        DBSession.delete(note)
        DBSession.commit()
        return HTTPFound(location='/notes')
    except:
        return Response("Произошла ошибка")


@view_config(route_name='update')
def update_user(request):

    try:
        note = DBSession.query(Note).filter(Note.id == request.params['id']).first()
        setattr(note, 'text', request.params['text'])
        DBSession.commit()
        return HTTPFound(location='/notes')
    except:
        return Response("Произошла ошибка")

@view_config(route_name='notes')
def users_render(request):

    try:
        notes_list = DBSession.query(Note).all()
        DBSession.commit()
        return render_to_response('templates/notes.jinja2', {'notes' : notes_list}, request=request)
    except:
        return Response("Произошла ошибка")

