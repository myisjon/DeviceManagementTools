from json import dumps

from flask import request, render_template
from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    query = request.args
    if query:
        return dumps(query)
    print(request.data)
    return render_template('auth/login.html')
