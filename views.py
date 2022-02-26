# from flask import Blueprint, jsonify
# from flask_restful import Api, Resource
# from scopezero.resources.dog_resources import DogDetails, DogDetailsCSV
# from scopezero.resources.dog_resources import (
#             GenerateLeatherCollar, GenerateLeatherLeach, GeneratePolyester, CleanUpNumber)


# class Home(Resource):
#     def get(self):
#         return jsonify({
#             "message": "Welcome to the DOG Details  pipeline!"
#         })


# dog_details = Blueprint(
#     "dog_details", __name__
# )

# api = Api(dog_details)

# api.add_resource(Home, '/')
# api.add_resource(DogDetails, "/dog_details")
# api.add_resource(DogDetailsCSV, "/dog_details_csv")
# api.add_resource(GenerateLeatherCollar, "/generate_collar")
# api.add_resource(GenerateLeatherLeach, "/generate_leash")
# api.add_resource(GeneratePolyester, "/generate_polyester")
# api.add_resource(CleanUpNumber, "/clean_up_number")