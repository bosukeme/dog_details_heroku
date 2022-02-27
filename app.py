# from flask import Flask
# from flask_cors import CORS
# # from config.settings import CORS_ORIGINS

# #views
# from scopezero.views import dog_details



# def create_app(settings_override=None):
#     """
#     Create a Flask application using the app factory pattern.

#     :param settings_override: Override settings
#     :return: Flask app
#     """
#     app = Flask(__name__, instance_relative_config=True)

#     app.config.from_object('config.settings')
#     app.config.from_pyfile('settings.py', silent=True)

#     if settings_override:
#         app.config.update(settings_override)


#     app.register_blueprint(dog_details)

#     CORS(app, supports_credentials=True, origins=CORS_ORIGINS)

#     return app



from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.dog_resources import (
            DogDetails, DogDetailsCSV, GenerateLeatherCollar, 
            GenerateLeatherLeach, GeneratePolyester, CleanUpNumber)


from config.settings import CORS_ORIGINS


app=Flask(__name__)

CORS(app, supports_credentials=True, origins=CORS_ORIGINS)

api=Api(app)


@app.route("/")
def home():
    return "<h1 style='color:blue'>This is the DOG Details  pipeline!</h1>"


api.add_resource(DogDetails, '/dog_details')
api.add_resource(DogDetailsCSV, '/dog_details_csv')
api.add_resource(GenerateLeatherCollar, "/generate_collar")
api.add_resource(GenerateLeatherLeach, "/generate_leash")
api.add_resource(GeneratePolyester, "/generate_polyester")
api.add_resource(CleanUpNumber, "/clean_up_number")

if __name__=='__main__':
    app.run(port= 5000, debug=True)
