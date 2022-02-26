import numpy as np
import pandas as pd
import math
from ast import literal_eval

"""
Static Dicts for Leather
"""

co2_static_dict = {
    'collar_average' : 0.5584,
    'leash' : 1.5356
}

## Static variables for leather_water_used
leather_water_used_static_dict = {
    'traditional_leather_collar': 5.296,
    'recycled_leather_collar': 0.5296,
    'traditional_leather_leash': 16.0204,
    'recycled_leather_leash': 1.4564
}

"""
Static Dicts for Polyester
"""
polyester_co2_tonne_static_dict = {
    'virgin_polyester' : 5357,
    'recycled_polyester' : 1339
}

## For the polyester co2 tonne dict
# Get the static variables
vir_pol = polyester_co2_tonne_static_dict['virgin_polyester']
rec_pol = polyester_co2_tonne_static_dict['recycled_polyester']

polyester_co2_tonne_dict = {
    'virgin_polyester' : {'tonne': vir_pol, 'kg': round(vir_pol/1000,10)},
    'recycled_polyester' : {'tonne': rec_pol, 'kg': round(rec_pol/1000,10)}
}


# Now for the water usage static dict - note that CBM stands for cubic meters
polyester_water_usage_static_dict = {
    'water_usage_per_tonne_cbm': 71000,
    'water_saving_for_recycled': 86,
    'average_bath_size': 0.13,
    'water_in_olympic_pool': 2500
}
polyester_water_usage_static_dict['water_usage_per_kg_cbm'] = polyester_water_usage_static_dict['water_usage_per_tonne_cbm']/1000

"""
Functions
"""
def clean_up_number(input_float):
    """
    This function takes an input float and then cleans it up into a format that can easily be 
    """
    num_len = len(str(int(input_float)))

    if num_len > 9:
        output_num = input_float/1000000000
        output_num = round(output_num,1)
        output_num = '%sb' % output_num

    elif num_len > 6:
        output_num = input_float/1000000
        output_num = round(output_num,1)
        output_num = '%sm' % output_num

    elif num_len > 3:
        output_num = input_float/1000
        output_num = round(output_num,1)
        output_num = '%sk' % output_num
    else:
        output_num = round(input_float,1)
        output_num = str(output_num)
    
    return output_num


def generate_leather_dog_collar_water_and_co2_savings_tables(collars_sold):
    """
    Water Savings Table
    """
    # Build function that creates the leather_water_dict
    trad_l_collar = leather_water_used_static_dict['traditional_leather_collar']
    rec_l_collar = leather_water_used_static_dict['recycled_leather_collar']

    # For the collar
    collar_water_dict = {
        'traditional_leather_collar' : {'litres_of_water_used': trad_l_collar, 'total': collars_sold*trad_l_collar, 'bath_tubs' : collars_sold*trad_l_collar*0.013},
        'recycled_leather_collar' : {'litres_of_water_used': rec_l_collar, 'total': collars_sold*rec_l_collar, 'bath_tubs' : collars_sold*rec_l_collar*0.013}
    }
    collar_water_dict['leather_collar_savings'] = {'litres_of_water_used': round(trad_l_collar-rec_l_collar,15), 'total': collars_sold*(trad_l_collar-rec_l_collar), 'bath_tubs' : (collars_sold*(trad_l_collar-rec_l_collar))*0.013}

    
    """
    co2 Savings Table
    """
    # Create the co2 dict
    co2_collar = co2_static_dict['collar_average']

    collar_co2_dict = {
        'collar_average' : {'co2_kg_saved': co2_collar, 'total': collars_sold*co2_collar, 'tonnes_saved' : collars_sold*co2_collar/1000},
    }

    litres_of_water_used = collar_water_dict['traditional_leather_collar']['total']
    excess_co2 = collar_co2_dict['collar_average']['total']

    return litres_of_water_used, excess_co2


def generate_leather_dog_leash_water_and_co2_savings_tables(leashes_sold):
    """
    Water Savings Table
    """
    # Build function that creates the leather_water_dict
    trad_l_leash = leather_water_used_static_dict['traditional_leather_leash']
    rec_l_leash = leather_water_used_static_dict['recycled_leather_leash']

    # For the collar
    collar_water_dict = {
        'traditional_leather_leash' : {'litres_of_water_used': trad_l_leash, 'total': leashes_sold*trad_l_leash, 'bath_tubs' : leashes_sold*trad_l_leash*0.013},
        'recycled_leather_leash' : {'litres_of_water_used': rec_l_leash, 'total': leashes_sold*rec_l_leash, 'bath_tubs' : leashes_sold*rec_l_leash*0.013}
    }
    collar_water_dict['leather_leash_savings'] = {'litres_of_water_used': round(trad_l_leash-rec_l_leash,15), 'total': leashes_sold*(trad_l_leash-rec_l_leash), 'bath_tubs' : (leashes_sold*(trad_l_leash-rec_l_leash))*0.013}

    
    """
    co2 Savings Table
    """
    # Create the co2 dict
    co2_leash = co2_static_dict['leash']

    collar_co2_dict = {
        'leash' : {'co2_kg_saved': co2_leash, 'total': leashes_sold*co2_leash, 'tonnes_saved' : leashes_sold*co2_leash/1000},
    }

    litres_of_water_used = collar_water_dict['traditional_leather_leash']['total']
    excess_co2 = collar_co2_dict['leash']['total']


    return litres_of_water_used, excess_co2


def generate_polyester_water_and_co2_savings_tables(num_dog_beds_sold, avg_bed_weight):


    ## For the polyester co2 savings dict - it takes in the polyester_co2_tonne_dict as well as avg_bed_weight and num_dog_beds_sold
    # Create the polyester co2 savings dict
    vir_kg = polyester_co2_tonne_dict['virgin_polyester']['kg']
    rec_kg = polyester_co2_tonne_dict['recycled_polyester']['kg']

    polyester_co2_savings_dict = {
        'virgin_polyester' : {'co2': round(vir_kg*avg_bed_weight,15), 'total_co2_kg': round(vir_kg*avg_bed_weight,15)*num_dog_beds_sold, 'total_co2_tonne' : (round(vir_kg*avg_bed_weight,15)*num_dog_beds_sold)/1000},
        'recycled_polyester' : {'co2': round(rec_kg*avg_bed_weight,15), 'total_co2_kg': round(rec_kg*avg_bed_weight,15)*num_dog_beds_sold, 'total_co2_tonne' : (round(rec_kg*avg_bed_weight,15)*num_dog_beds_sold)/1000}
    }

    polyester_co2_savings_dict['polyester_co2_savings'] = {'co2': round((vir_kg-rec_kg)*avg_bed_weight,15), 'total_co2_kg': round((vir_kg-rec_kg)*avg_bed_weight,6)*num_dog_beds_sold, 'total_co2_tonne' : (round((vir_kg-rec_kg)*avg_bed_weight,15)*num_dog_beds_sold)/1000}


    # Now for the polyester co2 miles dict
    polyester_co2_miles_dict = {
        'average_co2_per_mile_kg' : 0.41,  
    }
    polyester_co2_miles_dict['miles_saved'] = polyester_co2_savings_dict['polyester_co2_savings']['total_co2_kg'] * polyester_co2_miles_dict['average_co2_per_mile_kg']
    polyester_co2_miles_dict['miles_around_world'] = 24901
    polyester_co2_miles_dict['equivalent_saving'] = polyester_co2_miles_dict['miles_saved']/polyester_co2_miles_dict['miles_around_world']


    ## For the polyester water savings dict - it takes in the polyester_water_usage_static_dict as well as avg_bed_weight and num_dog_beds_sold
    # Create the polyester water savings dict
    wp_kg = polyester_water_usage_static_dict['water_usage_per_kg_cbm'] # water used per kg cbm
    avg_bath_cbm = polyester_water_usage_static_dict['average_bath_size']
    water_olymp = polyester_water_usage_static_dict['water_in_olympic_pool']
    water_sv_perc = polyester_water_usage_static_dict['water_saving_for_recycled']
    # print(wp_kg)

    polyester_water_savings_dict = {
        'virgin_polyester' : {'water_used_cbm': wp_kg*avg_bed_weight, 'total_water': round(wp_kg*avg_bed_weight,15)*num_dog_beds_sold, 'bath_tubs' : round(wp_kg*avg_bed_weight,15)*avg_bath_cbm, 'total_bath' : round(wp_kg*avg_bed_weight,15)*avg_bath_cbm*num_dog_beds_sold, 'olympic_pools': (round(wp_kg*avg_bed_weight,15)*num_dog_beds_sold)/water_olymp},
        'recycled_polyester' : {'water_used_cbm': (wp_kg*avg_bed_weight) * (1-(water_sv_perc/100)), 'total_water': round((wp_kg*avg_bed_weight) * (1-(water_sv_perc/100)),15)*num_dog_beds_sold, 'bath_tubs' : round((wp_kg*avg_bed_weight) * (1-(water_sv_perc/100)),15)*avg_bath_cbm, 'total_bath' : round((wp_kg*avg_bed_weight) * (1-(water_sv_perc/100)),15)*avg_bath_cbm*num_dog_beds_sold, 'olympic_pools': (round((wp_kg*avg_bed_weight) * (1-(water_sv_perc/100)),15)*num_dog_beds_sold)/water_olymp}
    }

    litres_of_water_used = polyester_water_savings_dict['virgin_polyester']['total_water']
    excess_co2 = polyester_co2_savings_dict['polyester_co2_savings']['total_co2_kg']

    
    return litres_of_water_used, excess_co2

