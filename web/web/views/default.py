from pyramid.view import view_config
from . .models import Note, User, Session, Base, engine
from pyramid.response import Response
from pyramid.renderers import render_to_response
from pyramid.httpexceptions import HTTPFound
from sqlalchemy.sql import exists


DBSession = Session(bind=engine)


@view_config(route_name='home')
def MainPage(request):
    return render_to_response('templates/index.jinja2', {'title': 'Welcome to NoteYou'}, request=request)

@view_config(route_name='add')
def add_render(request):
    return render_to_response('templates/add.jinja2', {'success' : 'success'}, request=request)

@view_config(route_name='sign_in')
def SignIn(request):

    try:
        query = DBSession.query(User).filter(
            User.name == request.params['name'], User.password == request.params['password']).first()

        if(query is None):
            user = User(
                name=request.params['name'],
                password=request.params['password']
            )
            DBSession.add(user)
            DBSession.commit()

            return Response("Вы успешно зарегистрировались")
        else:
            DBSession.commit()

            return Response("Вы уже зарегистрированы")

    except Exception as err:
        print("Error", str(err))
        return Response("Произошла ошибка")

@view_config(route_name='login')
def login(request):

    try:
        query = DBSession.query(User).filter(
            User.name == request.params['name'], User.password == request.params['password']).first()

        if(query is None):
            DBSession.commit()
            return HTTPFound(location="/")
        else:
            DBSession.commit()
            return HTTPFound(location='/notes')

    except Exception as err:
        print("Error", str(err))
        return Response("Произошла ошибка")


    
# ============= CRUD =================



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


