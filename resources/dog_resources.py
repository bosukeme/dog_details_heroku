from flask_restful import Resource, reqparse
from flask import request

from get_dogs import get_dog_details, get_dog_details_csv
from functions import single_calculations


class DogDetails(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('num_dog_beds_sold', type=int, help="The number of dogs to be sold")
            parser.add_argument('avg_bed_weight', type=float, help="The average weight of the dogs")
            parser.add_argument('lea_lea_sold', type=int, help="The lea lea sold")
            parser.add_argument('lea_col_sold', type=int, help="The lea col sold")
            

            args = parser.parse_args()


            result = get_dog_details(args['num_dog_beds_sold'], args['avg_bed_weight'], args['lea_lea_sold'], args['lea_col_sold'])
            return {
                'status': 'success',
                'data': result, 
                'message': 'Dog Details successful.'
            }, 200

        except Exception as e:
            return {
                'status': 'failed',
                'data': None,
                'message': str(e)
            }, 500




class DogDetailsCSV(Resource):

    def post(self):
        try:
            csv_file = request.files["csv_file"]
            if not csv_file:
                return "No CSV file attached"

            result = get_dog_details_csv(csv_file)
            return {
                'status': 'success',
                'data': result, 
                'message': 'Dog Details successful.'
            }, 200

        except Exception as e:
            return {
                'status': 'failed',
                'data': None,
                'message': str(e)
            }, 500



class GenerateLeatherCollar(Resource):
    def post(self):
        try:
            json_data = request.get_json()
            
            req_fields = ['collars_sold']

            for field in req_fields:
                if field not in json_data:
                    return {
                       'status': 'failed',
                       'data': None,
                       'message': field + ' is required'
                    }, 400
                elif json_data[field] == '':
                    return {
                       'status': 'failed',
                       'data': None,
                       'message': field + ' cannot be empty'
                    }, 400
                else:
                    pass
            
            collars_sold = json_data['collars_sold']
            result = single_calculations.generate_leather_dog_collar_water_and_co2_savings_tables(collars_sold)
            result = {
                "litres_of_water_used" : result[0],
                "excess_co2": result[1] 
                }
    
            return {
                'status': 'success',  
                'data': result, 
                'message': 'Generate Leather Dog Collar successful.'
            }, 200

        except Exception as e:
            return {
                'status': 'failed',
                'data': None,
                'message': str(e)
            }, 500


class GenerateLeatherLeach(Resource):
    def post(self):
        try:
            json_data = request.get_json()
            
            req_fields = ['leashes_sold']

            for field in req_fields:
                if field not in json_data:
                    return {
                       'status': 'failed',
                       'data': None,
                       'message': field + ' is required'
                    }, 400
                elif json_data[field] == '':
                    return {
                       'status': 'failed',
                       'data': None,
                       'message': field + ' cannot be empty'
                    }, 400
                else:
                    pass
            
            leashes_sold = json_data['leashes_sold']
        
            result = single_calculations.generate_leather_dog_leash_water_and_co2_savings_tables(leashes_sold)
            result = {
                "litres_of_water_used" : result[0],
                "excess_co2": result[1] 
                }
    
            return {
                'status': 'success',  
                'data': result, 
                'message': 'Generate Leather Dog Leaches successful.'
            }, 200

        except Exception as e:
            return {
                'status': 'failed',
                'data': None,
                'message': str(e)
            }, 500


class GeneratePolyester(Resource):
    def post(self):
        try:
            json_data = request.get_json()
            
            req_fields = ['num_dog_beds_sold', 'avg_bed_weight']

            for field in req_fields:
                if field not in json_data:
                    return {
                       'status': 'failed',
                       'data': None,
                       'message': field + ' is required'
                    }, 400
                elif json_data[field] == '':
                    return {
                       'status': 'failed',
                       'data': None,
                       'message': field + ' cannot be empty'
                    }, 400
                else:
                    pass
            
            num_dog_beds_sold = json_data['num_dog_beds_sold']
            avg_bed_weight = json_data['avg_bed_weight']
            result = single_calculations.generate_polyester_water_and_co2_savings_tables(num_dog_beds_sold, avg_bed_weight)
            
            result = {
                "litres_of_water_used" : result[0],
                "excess_co2": result[1] 
                }

            return {
                'status': 'success',  
                'data': result, 
                'message': 'Generate Polyester Data successful.'
            }, 200

        except Exception as e:
            return {
                'status': 'failed',
                'data': None,
                'message': str(e)
            }, 500



class CleanUpNumber(Resource):
    def post(self):
        try:
            json_data = request.get_json()
            
            req_fields = ['input_float']

            for field in req_fields:
                if field not in json_data:
                    return {
                       'status': 'failed',
                       'data': None,
                       'message': field + ' is required'
                    }, 400
                elif json_data[field] == '':
                    return {
                       'status': 'failed',
                       'data': None,
                       'message': field + ' cannot be empty'
                    }, 400
                else:
                    pass
            
            input_float = json_data['input_float']
            result = single_calculations.clean_up_number(input_float)

            return {
                'status': 'success',  
                'data': result, 
                'message': 'Clean Up Number successful.'
            }, 200

        except Exception as e:
            return {
                'status': 'failed',
                'data': None,
                'message': str(e)
            }, 500
