from . import dmt


@dmt.route('/', methods=['GET', 'HEAD'])
@dmt.route('/index', methods=['GET', 'HEAD'])
def index():
    return 'index'
