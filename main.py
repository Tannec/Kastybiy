import os
from flask import Flask, render_template
from data import db_session
from data.resource import cuisine_resource, culture_resource, places_resource
from flask_restful import Api

#Initialization
db_session.global_init("db/kastybiy.db")
app = Flask(__name__)
app.config["SECRET_KEY"] = "dvrQYr4v62d"

#Api initialization
api = Api(app)
api.add_resource(cuisine_resource.CuisineListResource, "/api/get/cuisine")
api.add_resource(cuisine_resource.CuisineResource, "/api/get/cuisine/<id>")
api.add_resource(cuisine_resource.CuisineCategoryResource, "/api/get/cuisine/<category>")

api.add_resource(culture_resource.CultureResource, "/api/get/culture/<id>")
api.add_resource(culture_resource.CultureListResource, "/api/get/culture")

api.add_resource(places_resource.PlaceResource, "/api/get/place/<id>")
api.add_resource(places_resource.PlaceListResource, "/api/get/places")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/cuisine")
def cuisine():
    return render_template("cuisine.html")


@app.route("/culture")
def culture():
    return render_template("culture.html")


@app.route("/places")
def places():
    return render_template("places.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

