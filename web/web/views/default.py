from pyramid.view import view_config
from . .models import User, Session, Base, engine
import time
from pyramid.response import Response


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):

    DBSession = Session(bind=engine)
    new_user = User(name="Vasya")
    user = User(name="Vasy")
    user_list = DBSession.query(User).all()
    DBSession.add(new_user)
    DBSession.add(user)
    DBSession.commit()
    return {'project': user_list}
