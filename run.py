from werkzeug.middleware.dispatcher import DispatcherMiddleware
from application import app
# if __name__ == '__main__':
#     app.run()

# run : uwsgi --http 127.0.0.1:8000 --wsgi-file app.py --callable app_dispatch

app_dispatch = DispatcherMiddleware(app)
