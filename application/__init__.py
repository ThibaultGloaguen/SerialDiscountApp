from flask import Flask, render_template
from flask_cors import CORS
import pickledb
import os


app = Flask(__name__,
            static_folder="../frontend/dist/static",
            template_folder="../frontend/dist")
CORS(app)

app.config.update(dict(
    DATABASE_DISCOUNT=os.path.join(app.root_path, '../discount_codes.db')
))
app.config.update(dict(
    DATABASE_SERIAL=os.path.join(app.root_path, '../serial_discount.db')
))

discount_db = pickledb.load(app.config['DATABASE_DISCOUNT'], True)
serial_number_db = pickledb.load(app.config['DATABASE_SERIAL'], True)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


from application import discount_route

app.register_blueprint(discount_route.views)
