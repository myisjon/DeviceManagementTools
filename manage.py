from apps import start_app
from main import config


app = start_app(config.CONFIG)
app.run(host='0.0.0.0', debug=True, port=5000)
