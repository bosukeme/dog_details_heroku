"""
Static Variables From Leather
"""
from ast import literal_eval

def generate_leather_water_and_co2_savings_tables(lea_lea_sold, lea_col_sold, leather_water_used_static_dict, co2_static_dict):
    """
    Water Savings Table
    """

    # Build function that creates the leather_water_dict
    trad_l_collar = leather_water_used_static_dict['traditional_leather_collar']
    rec_l_collar = leather_water_used_static_dict['recycled_leather_collar']
    trad_l_leash = leather_water_used_static_dict['traditional_leather_leash']
    rec_l_leash = leather_water_used_static_dict['recycled_leather_leash']

    # For the collar
    leather_water_collar_dict = {
        'traditional_leather_collar' : {'litres_of_water_used': trad_l_collar, 'Total': lea_col_sold*trad_l_collar, 'Bath Tubs' : lea_col_sold*trad_l_collar*0.013},
        'recycled_leather_collar' : {'litres_of_water_used': rec_l_collar, 'Total': lea_col_sold*rec_l_collar, 'Bath Tubs' : lea_col_sold*rec_l_collar*0.013}
    }
    leather_water_collar_dict['Leather Collar Savings'] = {'litres_of_water_used': round(trad_l_collar-rec_l_collar,15), 'Total': lea_col_sold*(trad_l_collar-rec_l_collar), 'Bath Tubs' : (lea_col_sold*(trad_l_collar-rec_l_collar))*0.013}


    # For the leash
    leather_water_leash_dict = {
        'traditional_leather_leash' : {'litres_of_water_used': trad_l_leash, 'Total': lea_lea_sold*trad_l_leash, 'Bath Tubs' : lea_lea_sold*trad_l_leash*0.013},
        'recycled_leather_leash' : {'litres_of_water_used': rec_l_leash, 'Total': lea_lea_sold*rec_l_leash, 'Bath Tubs' : lea_lea_sold*rec_l_leash*0.013}
    }
    leather_water_leash_dict['leather_leash_savings'] = {'litres_of_water_used': round(trad_l_leash-rec_l_leash,15), 'Total': lea_lea_sold*round(trad_l_leash-rec_l_leash,15), 'Bath Tubs' : (lea_lea_sold*(trad_l_leash-rec_l_leash))*0.013}

    # Combine leather and leash to create the leather_water_dict
    leather_water_dict = leather_water_collar_dict.copy()
    leather_water_dict.update(leather_water_leash_dict)


    """
    co2 Savings Table
    """


    # Create the co2 dict
    co2_collar = co2_static_dict['collar_average']
    co2_leash = co2_static_dict['Leash']

    co2_dict = {
        'collar_average' : {'litres_of_water_used': co2_collar, 'Total': lea_col_sold*co2_collar, 'Tonnes Saved' : lea_col_sold*co2_collar/1000},
        'recycled_leather_leash' : {'litres_of_water_used': co2_leash, 'Total': lea_lea_sold*co2_leash, 'Tonnes Saved' : lea_lea_sold*co2_leash/1000}
    }

    return leather_water_dict, co2_dict


def generate_polyester_water_and_co2_savings_tables(num_dog_beds_sold, avg_bed_weight):
    """
    Now work on generating all the tables required from the Polyester table
    """
    polyester_co2_tonne_static_dict = {
        'Virgin Polyester' : 5357,
        'Recycled Polyester' : 1339
    }

    ## For the polyester co2 tonne dict
    # Get the static variables
    vir_pol = polyester_co2_tonne_static_dict['Virgin Polyester']
    rec_pol = polyester_co2_tonne_static_dict['Recycled Polyester']

    polyester_co2_tonne_dict = {
        'Virgin Polyester' : {'Tonne': vir_pol, 'KG': round(vir_pol/1000,10)},
        'Recycled Polyester' : {'Tonne': rec_pol, 'KG': round(rec_pol/1000,10)}
    }

    ## For the polyester co2 savings dict - it takes in the polyester_co2_tonne_dict as well as avg_bed_weight and num_dog_beds_sold
    # Create the polyester co2 savings dict
    vir_kg = polyester_co2_tonne_dict['Virgin Polyester']['KG']
    rec_kg = polyester_co2_tonne_dict['Recycled Polyester']['KG']

    polyester_co2_savings_dict = {
        'Virgin Polyester' : {'CO2': round(vir_kg*avg_bed_weight,15), 'Total CO2 - KG': round(vir_kg*avg_bed_weight,15)*num_dog_beds_sold, 'Total CO2 - Tonne' : (round(vir_kg*avg_bed_weight,15)*num_dog_beds_sold)/1000},
        'Recycled Polyester' : {'CO2': round(rec_kg*avg_bed_weight,15), 'Total CO2 - KG': round(rec_kg*avg_bed_weight,15)*num_dog_beds_sold, 'Total CO2 - Tonne' : (round(rec_kg*avg_bed_weight,15)*num_dog_beds_sold)/1000}
    }

    polyester_co2_savings_dict['Polyester CO2 Savings'] = {'CO2': round((vir_kg-rec_kg)*avg_bed_weight,15), 'Total CO2 - KG': round((vir_kg-rec_kg)*avg_bed_weight,6)*num_dog_beds_sold, 'Total CO2 - Tonne' : (round((vir_kg-rec_kg)*avg_bed_weight,15)*num_dog_beds_sold)/1000}


    # Now for the polyester co2 miles dict
    polyester_co2_miles_dict = {
        'Average Co2 per mile - KG' : 0.41,  
    }
    polyester_co2_miles_dict['Miles Saved'] = polyester_co2_savings_dict['Polyester CO2 Savings']['Total CO2 - KG'] * polyester_co2_miles_dict['Average Co2 per mile - KG']
    polyester_co2_miles_dict['Miles Around World'] = 24901
    polyester_co2_miles_dict['Equivalent Saving'] = polyester_co2_miles_dict['Miles Saved']/polyester_co2_miles_dict['Miles Around World']

    # Now for the water usage static dict - note that CBM stands for cubic meters
    polyester_water_usage_static_dict = {
        'Water Usage Per Tonne (CBM)': 71000,
        'Water Saving For Recycled (%)': 86,
        'Average Bath Size (CBM)': 0.13,
        'Water In Olympic Pool': 2500
    }
    polyester_water_usage_static_dict['Water Usage Per KG (CBM)'] = polyester_water_usage_static_dict['Water Usage Per Tonne (CBM)']/1000


    ## For the polyester water savings dict - it takes in the polyester_water_usage_static_dict as well as avg_bed_weight and num_dog_beds_sold
    # Create the polyester water savings dict
    wp_kg = polyester_water_usage_static_dict['Water Usage Per KG (CBM)'] # water used per kg cbm
    avg_bath_cbm = polyester_water_usage_static_dict['Average Bath Size (CBM)']
    water_olymp = polyester_water_usage_static_dict['Water In Olympic Pool']
    water_sv_perc = polyester_water_usage_static_dict['Water Saving For Recycled (%)']
    # print(wp_kg)

    polyester_water_savings_dict = {
        'Virgin Polyester' : {'Water Used (CBM)': wp_kg*avg_bed_weight, 'Total Water': round(wp_kg*avg_bed_weight,15)*num_dog_beds_sold, 'Bath Tubs' : round(wp_kg*avg_bed_weight,15)*avg_bath_cbm, 'Total Bath' : round(wp_kg*avg_bed_weight,15)*avg_bath_cbm*num_dog_beds_sold, 'Olympic Pools': (round(wp_kg*avg_bed_weight,15)*num_dog_beds_sold)/water_olymp},
        'Recycled Polyester' : {'Water Used (CBM)': (wp_kg*avg_bed_weight) * (1-(water_sv_perc/100)), 'Total Water': round((wp_kg*avg_bed_weight) * (1-(water_sv_perc/100)),15)*num_dog_beds_sold, 'Bath Tubs' : round((wp_kg*avg_bed_weight) * (1-(water_sv_perc/100)),15)*avg_bath_cbm, 'Total Bath' : round((wp_kg*avg_bed_weight) * (1-(water_sv_perc/100)),15)*avg_bath_cbm*num_dog_beds_sold, 'Olympic Pools': (round((wp_kg*avg_bed_weight) * (1-(water_sv_perc/100)),15)*num_dog_beds_sold)/water_olymp}
    }

    # Get all the variables from the current calculations
    wat_sav_kg = polyester_water_savings_dict['Virgin Polyester']['Water Used (CBM)'] - polyester_water_savings_dict['Recycled Polyester']['Water Used (CBM)']
    polyester_water_savings_dict['Polyester Water Savings'] = {'Water Used (CBM)': wat_sav_kg, 'Total Water': round(wat_sav_kg,15)*num_dog_beds_sold, 'Bath Tubs' : round(wat_sav_kg,15)*avg_bath_cbm, 'Total Bath' : round(wat_sav_kg,6)*avg_bath_cbm*num_dog_beds_sold, 'Olympic Pools': (round(wat_sav_kg,15)*num_dog_beds_sold)/water_olymp}

    ## Now generate the oil savings dict
    oil_savings_dict = {
        '1 Tonne Of Recycled PET Saves': 0.7,
        '1 KG Of Recycled PET Save': 86,
        'Total Weight Polyester (Tonne)': 0.13,
    }
    oil_savings_dict['1 KG Of Recycled PET Save'] = oil_savings_dict['1 Tonne Of Recycled PET Saves']/1000
    oil_savings_dict['Total Weight Polyester (Tonne)'] = round(avg_bed_weight*num_dog_beds_sold/1000,10)
    oil_savings_dict['Total Barrels Of Oil'] = round(avg_bed_weight*num_dog_beds_sold/1000,10)
    oil_savings_dict['Barrels Of Oil Saved'] = (round((avg_bed_weight*num_dog_beds_sold/1000),10) * 0.3)
    oil_savings_dict['Barrels Saved'] = round(oil_savings_dict['1 Tonne Of Recycled PET Saves'] * oil_savings_dict['Total Weight Polyester (Tonne)'],10)

    return polyester_co2_tonne_dict, polyester_co2_savings_dict, polyester_co2_miles_dict, polyester_water_usage_static_dict, polyester_water_savings_dict, oil_savings_dict

"""
Main function
"""
def generate_sustainability_tables(num_dog_beds_sold, avg_bed_weight, lea_lea_sold, lea_col_sold):
    
    """
    Static Dicts for Leather
    """
    co2_static_dict = {
        'collar_average' : 0.5584,
        'Leash' : 1.5356
    }

    ## Static variables for leather_water_used
    leather_water_used_static_dict = {
        'traditional_leather_collar': 5.296,
        'recycled_leather_collar': 0.5296,
        'traditional_leather_leash': 16.0204,
        'recycled_leather_leash': 1.4564
    } 

    """
    Static Variables From Leather Tab
    """
    """
    ELeather per m² (SLi2) Table
    """
    eleather_pm2_SLi2_dict = {
        'Climate Change (Kg Of CO₂ Saved)' : 34.9,
        'Water Consuption (m³ Saved)' : 0.331,
        'Water Consuption (Liters Saved)' : 331,
        'Land Use (% Saved)' : 77,
        '10,000m² Eleather (Liters Saved)' : 3310000,
    }

    # create the olympic swimming pool variable from the 10km2 eleather variable 
    eleather_pm2_SLi2_dict['10,000m² Eleather (Olympic Swimming Pools)'] = round(eleather_pm2_SLi2_dict['10,000m² Eleather (Liters Saved)']/2500000,15)

    """
    Generate the preliminary tables
    """
    ## Generate the tables for leather analysis
    leather_water_dict, co2_dict = generate_leather_water_and_co2_savings_tables(lea_lea_sold, lea_col_sold, leather_water_used_static_dict, co2_static_dict)

    ## Generate the tables for polyester analysis
    polyester_co2_tonne_dict, polyester_co2_savings_dict, polyester_co2_miles_dict, polyester_water_usage_static_dict, polyester_water_savings_dict, oil_savings_dict = generate_polyester_water_and_co2_savings_tables(num_dog_beds_sold, avg_bed_weight)

    """
    Now to structure out the final output as we expect it
    """
    dog_bed_analysis_input_table = {
        'num_of_dog_beds_sold_per_year' : num_dog_beds_sold,
        'average_weight_of_dog_bed_kg' : avg_bed_weight
    }

    #* For this table, note that the column name for the table keys is 'Raw Material'
    carbon_footprint_analysis_table = {
        'dog_beds_made_from_virgin_polyester' : {'co2_per_ton': polyester_co2_savings_dict['Virgin Polyester']['Total CO2 - Tonne'], 'water_used_bath_tubs': polyester_water_savings_dict['Virgin Polyester']['Total Bath'], 'barrels_of_oil': oil_savings_dict['Total Barrels Of Oil']},
        'dog_beds_made_from_recycled_polyester' : {'co2_per_ton': polyester_co2_savings_dict['Recycled Polyester']['Total CO2 - Tonne'], 'water_used_bath_tubs': polyester_water_savings_dict['Recycled Polyester']['Total Bath'], 'barrels_of_oil': oil_savings_dict['Barrels Of Oil Saved']},
        'total_saving' : {'co2_per_ton': polyester_co2_savings_dict['Polyester CO2 Savings']['Total CO2 - Tonne'], 'water_used_bath_tubs': polyester_water_savings_dict['Polyester Water Savings']['Total Bath'], 'barrels_of_oil': oil_savings_dict['Barrels Saved']}
    }

    leather_collar_and_leash_analysis_input_table = {
        'num_of_leather_collars_sold' : lea_lea_sold,
        'num_of_leather_leashes_sold' : lea_col_sold
    }

    leather_collar_and_leash_analysis_table = {
        'traditional_leather_collar' : {'litres_of_water_used': leather_water_dict['traditional_leather_collar']['Total'], 'water_used_bath_tubs': leather_water_dict['traditional_leather_collar']['Bath Tubs']},
        'recycled_leather_collar' : {'litres_of_water_used': leather_water_dict['recycled_leather_collar']['Total'], 'water_used_bath_tubs': leather_water_dict['recycled_leather_collar']['Bath Tubs']},
        'collar_water_saving' : {'litres_of_water_used': leather_water_dict['Leather Collar Savings']['Total'], 'water_used_bath_tubs': leather_water_dict['Leather Collar Savings']['Bath Tubs']},
        'traditional_leather_leash' : {'litres_of_water_used': leather_water_dict['traditional_leather_leash']['Total'], 'water_used_bath_tubs': leather_water_dict['traditional_leather_leash']['Bath Tubs']},
        'recycled_leather_leash' : {'litres_of_water_used': leather_water_dict['recycled_leather_leash']['Total'], 'water_used_bath_tubs': leather_water_dict['recycled_leather_leash']['Bath Tubs']},
        'leash_water_saving' : {'litres_of_water_used': leather_water_dict['leather_leash_savings']['Total'], 'water_used_bath_tubs': leather_water_dict['leather_leash_savings']['Bath Tubs']},
    }

    co2_saving_per_item_table = {
        'recycled_leather_collar' : co2_dict['collar_average']['Tonnes Saved'],
        'recycled_leather_leash' : co2_dict['recycled_leather_leash']['Tonnes Saved']
    }

    return dog_bed_analysis_input_table, carbon_footprint_analysis_table, leather_collar_and_leash_analysis_input_table, leather_collar_and_leash_analysis_table, co2_saving_per_item_table


"""
Functions for single product calculations
"""

def generate_sustainability_calculations_for_single_dog_bed(num_dog_beds_sold, bed_weight):
    """
    This function takes a single dog bed and then runs the calculations needed to get the sustainability figures for just that bed
    """
    """
    Static Variables From Leather Tab
    """
    """
    ELeather per m² (SLi2) Table
    """
    eleather_pm2_SLi2_dict = {
        'Climate Change (Kg Of CO₂ Saved)' : 34.9,
        'Water Consuption (m³ Saved)' : 0.331,
        'Water Consuption (Liters Saved)' : 331,
        'Land Use (% Saved)' : 77,
        '10,000m² Eleather (Liters Saved)' : 3310000,
    }

    # create the olympic swimming pool variable from the 10km2 eleather variable 
    eleather_pm2_SLi2_dict['10,000m² Eleather (Olympic Swimming Pools)'] = round(eleather_pm2_SLi2_dict['10,000m² Eleather (Liters Saved)']/2500000,3)

    ## Generate the tables for polyester analysis
    polyester_co2_tonne_dict, polyester_co2_savings_dict, polyester_co2_miles_dict, polyester_water_usage_static_dict, polyester_water_savings_dict, oil_savings_dict = generate_polyester_water_and_co2_savings_tables(num_dog_beds_sold, bed_weight)

    """
    Now to structure out the final output as we expect it
    """
    dog_bed_analysis_input_table = {
        'num_of_dog_beds_sold_per_year' : num_dog_beds_sold,
        'average_weight_of_dog_bed_kg' : bed_weight
    }

    #* For this table, note that the column name for the table keys is 'Raw Material'
    carbon_footprint_analysis_table = {
        'dog_beds_made_from_virgin_polyester' : {'co2_per_ton': polyester_co2_savings_dict['Virgin Polyester']['Total CO2 - Tonne'], 'water_used_bath_tubs': polyester_water_savings_dict['Virgin Polyester']['Total Bath'], 'barrels_of_oil': oil_savings_dict['Total Barrels Of Oil']},
        'dog_beds_made_from_recycled_polyester' : {'co2_per_ton': polyester_co2_savings_dict['Recycled Polyester']['Total CO2 - Tonne'], 'water_used_bath_tubs': polyester_water_savings_dict['Recycled Polyester']['Total Bath'], 'barrels_of_oil': oil_savings_dict['Barrels Of Oil Saved']},
        'total_saving' : {'co2_per_ton': polyester_co2_savings_dict['Polyester CO2 Savings']['Total CO2 - Tonne'], 'water_used_bath_tubs': polyester_water_savings_dict['Polyester Water Savings']['Total Bath'], 'barrels_of_oil': oil_savings_dict['Barrels Saved']}
    }

    leather_collar_and_leash_analysis_input_table = {
        'num_of_leather_collars_sold' : 0,
        'num_of_leather_leashes_sold' : 0
    }

    
    leather_collar_and_leash_analysis_table = {
        'traditional_leather_collar' : {'litres_of_water_used': 0, 'water_used_bath_tubs': 0},
        'recycled_leather_collar' : {'litres_of_water_used': 0, 'water_used_bath_tubs': 0},
        'collar_water_saving' : {'litres_of_water_used': 0, 'water_used_bath_tubs': 0},
        'traditional_leather_leash' : {'litres_of_water_used': 0, 'water_used_bath_tubs': 0},
        'recycled_leather_leash' : {'litres_of_water_used': 0, 'water_used_bath_tubs': 0},
        'leash_water_saving' : {'litres_of_water_used': 0, 'water_used_bath_tubs': 0},
    }

    co2_saving_per_item_table = {
        'recycled_leather_collar' : 0,
        'recycled_leather_leash' : 0
    }

    single_product_dict = {
        'dog_bed_analysis_input_table' : dog_bed_analysis_input_table,
        'carbon_footprint_analysis_table' : carbon_footprint_analysis_table,
        'leather_collar_and_leash_analysis_input_table' : leather_collar_and_leash_analysis_input_table,
        'leather_collar_and_leash_analysis_table' : leather_collar_and_leash_analysis_table,
        'co2_saving_per_item_table' : co2_saving_per_item_table,
    }

    return single_product_dict


def generate_sustainability_calculations_for_single_dog_collar(lea_col_sold):
    """
    Static Dicts for Leather
    """
    lea_lea_sold = 0

    co2_static_dict = {
        'collar_average' : 0.5584,
        'Leash' : 1.5356
    }

    ## Static variables for leather_water_used
    leather_water_used_static_dict = {
        'traditional_leather_collar': 5.296,
        'recycled_leather_collar': 0.5296,
        'traditional_leather_leash': 16.0204,
        'recycled_leather_leash': 1.4564
        
    }

    """
    Static Variables From Leather Tab
    """
    """
    ELeather per m² (SLi2) Table
    """
    eleather_pm2_SLi2_dict = {
        'Climate Change (Kg Of CO₂ Saved)' : 34.9,
        'Water Consuption (m³ Saved)' : 0.331,
        'Water Consuption (Liters Saved)' : 331,
        'Land Use (% Saved)' : 77,
        '10,000m² Eleather (Liters Saved)' : 3310000,
    }

    # create the olympic swimming pool variable from the 10km2 eleather variable 
    eleather_pm2_SLi2_dict['10,000m² Eleather (Olympic Swimming Pools)'] = round(eleather_pm2_SLi2_dict['10,000m² Eleather (Liters Saved)']/2500000,15)

    """
    Generate the preliminary tables
    """
    ## Generate the tables for leather analysis
    leather_water_dict, co2_dict = generate_leather_water_and_co2_savings_tables(lea_lea_sold, lea_col_sold, leather_water_used_static_dict, co2_static_dict)

    """
    Now to structure out the final output as we expect it
    """
    dog_bed_analysis_input_table = {
        'num_of_dog_beds_sold_per_year' : 0,
        'average_weight_of_dog_bed_kg' : 0
    }

    #* For this table, note that the column name for the table keys is 'Raw Material'
    carbon_footprint_analysis_table = {
        'dog_beds_made_from_virgin_polyester' : {'co2_per_ton': 0, 'water_used_bath_tubs': 0, 'barrels_of_oil': 0},
        'dog_beds_made_from_recycled_polyester' : {'co2_per_ton': 0, 'water_used_bath_tubs': 0, 'barrels_of_oil': 0},
        'total_saving' : {'co2_per_ton': 0, 'water_used_bath_tubs': 0, 'barrels_of_oil': 0}
    }

    leather_collar_and_leash_analysis_input_table = {
        'num_of_leather_collars_sold' : 0,
        'num_of_leather_leashes_sold' : lea_col_sold
    }


    leather_collar_and_leash_analysis_table = {
        'traditional_leather_collar' : {'litres_of_water_used': leather_water_dict['traditional_leather_collar']['Total'], 'water_used_bath_tubs': leather_water_dict['traditional_leather_collar']['Bath Tubs']},
        'recycled_leather_collar' : {'litres_of_water_used': leather_water_dict['recycled_leather_collar']['Total'], 'water_used_bath_tubs': leather_water_dict['recycled_leather_collar']['Bath Tubs']},
        'collar_water_saving' : {'litres_of_water_used': leather_water_dict['Leather Collar Savings']['Total'], 'water_used_bath_tubs': leather_water_dict['Leather Collar Savings']['Bath Tubs']},
        'traditional_leather_leash' : {'litres_of_water_used': 0, 'water_used_bath_tubs': 0},
        'recycled_leather_leash' : {'litres_of_water_used': 0, 'water_used_bath_tubs': 0},
        'leash_water_saving' : {'litres_of_water_used': 0, 'water_used_bath_tubs': 0},
    }

    co2_saving_per_item_table = {
        'recycled_leather_collar' : co2_dict['collar_average']['Tonnes Saved'],
        'recycled_leather_leash' : 0
    }

    single_product_dict = {
        'dog_bed_analysis_input_table' : dog_bed_analysis_input_table,
        'carbon_footprint_analysis_table' : carbon_footprint_analysis_table,
        'leather_collar_and_leash_analysis_input_table' : leather_collar_and_leash_analysis_input_table,
        'leather_collar_and_leash_analysis_table' : leather_collar_and_leash_analysis_table,
        'co2_saving_per_item_table' : co2_saving_per_item_table,
    }

    return single_product_dict


def generate_sustainability_calculations_for_single_dog_leash(lea_lea_sold):
    """
    Static Dicts for Leather
    """
    lea_col_sold = 0

    co2_static_dict = {
        'collar_average' : 0.5584,
        'Leash' : 1.5356
    }

    ## Static variables for leather_water_used

    leather_water_used_static_dict = {
        'traditional_leather_collar': 5.296,
        'recycled_leather_collar': 0.5296,
        'traditional_leather_leash': 16.0204,
        'recycled_leather_leash': 1.4564
        
    }



    """
    Static Variables From Leather Tab
    """
    """
    ELeather per m² (SLi2) Table
    """
    eleather_pm2_SLi2_dict = {
        'Climate Change (Kg Of CO₂ Saved)' : 34.9,
        'Water Consuption (m³ Saved)' : 0.331,
        'Water Consuption (Liters Saved)' : 331,
        'Land Use (% Saved)' : 77,
        '10,000m² Eleather (Liters Saved)' : 3310000,
    }

    # create the olympic swimming pool variable from the 10km2 eleather variable 
    eleather_pm2_SLi2_dict['10,000m² Eleather (Olympic Swimming Pools)'] = round(eleather_pm2_SLi2_dict['10,000m² Eleather (Liters Saved)']/2500000,15)

    """
    Generate the preliminary tables
    """
    ## Generate the tables for leather analysis
    leather_water_dict, co2_dict = generate_leather_water_and_co2_savings_tables(lea_lea_sold, lea_col_sold, leather_water_used_static_dict, co2_static_dict)

    """
    Now to structure out the final output as we expect it
    """
    dog_bed_analysis_input_table = {
        'num_of_dog_beds_sold_per_year' : 0,
        'average_weight_of_dog_bed_kg' : 0
    }


    #* For this table, note that the column name for the table keys is 'Raw Material'
    carbon_footprint_analysis_table = {
        'dog_beds_made_from_virgin_polyester' : {'co2_per_ton': 0, 'water_used_bath_tubs': 0, 'barrels_of_oil': 0},
        'dog_beds_made_from_recycled_polyester' : {'co2_per_ton': 0, 'water_used_bath_tubs': 0, 'barrels_of_oil': 0},
        'total_saving' : {'co2_per_ton': 0, 'water_used_bath_tubs': 0, 'barrels_of_oil': 0}
    }

    leather_collar_and_leash_analysis_input_table = {
        'num_of_leather_collars_sold' : lea_lea_sold,
        'num_of_leather_leashes_sold' : 0
    }


    leather_collar_and_leash_analysis_table = {
        'traditional_leather_collar' : {'litres_of_water_used': 0, 'water_used_bath_tubs': 0},
        'recycled_leather_collar' : {'litres_of_water_used': 0, 'water_used_bath_tubs': 0},
        'collar_water_saving' : {'litres_of_water_used': 0, 'water_used_bath_tubs': 0},
        'traditional_leather_leash' : {'litres_of_water_used': leather_water_dict['traditional_leather_leash']['Total'], 'water_used_bath_tubs': leather_water_dict['traditional_leather_leash']['Bath Tubs']},
        'recycled_leather_leash' : {'litres_of_water_used': leather_water_dict['recycled_leather_leash']['Total'], 'water_used_bath_tubs': leather_water_dict['recycled_leather_leash']['Bath Tubs']},
        'leash_water_saving' : {'litres_of_water_used': leather_water_dict['leather_leash_savings']['Total'], 'water_used_bath_tubs': leather_water_dict['leather_leash_savings']['Bath Tubs']},
    }


    co2_saving_per_item_table = {
        'recycled_leather_collar' : 0,
        'recycled_leather_leash' : co2_dict['recycled_leather_leash']['Tonnes Saved']
    }





    single_product_dict = {
        'dog_bed_analysis_input_table' : dog_bed_analysis_input_table,
        'carbon_footprint_analysis_table' : carbon_footprint_analysis_table,
        'leather_collar_and_leash_analysis_input_table' : leather_collar_and_leash_analysis_input_table,
        'leather_collar_and_leash_analysis_table' : leather_collar_and_leash_analysis_table,
        'co2_saving_per_item_table' : co2_saving_per_item_table,
    }

    return single_product_dict

"""
Calculations for product sales df
"""
def calculate_sustainability_metrics_for_sold_products(product_sales_df):
    product_sustainability_dict_list = []
    for i in range(len(product_sales_df)):

        sku = product_sales_df.iloc[i]['_id']
        prod_type = product_sales_df.iloc[i]['product_type']
        num_sold = product_sales_df.iloc[i]['Number_of_items_sold']

        try:
            if prod_type == 'dog-bed':
                bed_weight = round(float(literal_eval(product_sales_df['Attributes_and_specifications'].iloc[i])['Weight'][:-3]),2)
                single_product_dict = generate_sustainability_calculations_for_single_dog_bed(num_sold, bed_weight)
            elif prod_type == 'dog-collar':
                single_product_dict = generate_sustainability_calculations_for_single_dog_collar(num_sold)
            elif prod_type == 'dog-leash':
                single_product_dict = generate_sustainability_calculations_for_single_dog_leash(num_sold)
        except:
            single_product_dict = 'NA'

        product_sustainability_dict_list.append(single_product_dict)

    product_sales_df['Product Sustainability Metrics'] = product_sustainability_dict_list

    return product_sales_df

def generate_co2_savings_from_product_sales_df(product_sales_df):
    ## Build functionality to calculate all metrics for the co2 table
    collar_co2_list = []
    leash_co2_list = []

    for i in range(len(product_sales_df)):

        single_product_dict = product_sales_df['Product Sustainability Metrics'].iloc[i]

        if single_product_dict != 'NA':

            co2_table = single_product_dict['co2_saving_per_item_table']
            collar = co2_table['recycled_leather_collar']
            leash = co2_table['recycled_leather_leash']
            collar_co2_list.append(collar)
            leash_co2_list.append(leash)

    collar_total = int(sum(collar_co2_list))
    leash_total = int(sum(leash_co2_list))

    co2_saving_per_item_table = {
        'recycled_leather_collar' : collar_total,
        'recycled_leather_leash' : leash_total
    }


    return co2_saving_per_item_table


def generate_polyester_dict_from_product_sales_df(product_sales_df):
    ## Build functionality to calculate all metrics for the polyester table
    v_pol_co2_list = []
    v_pol_wat_list = []
    v_pol_oil_list = []
    r_pol_co2_list = []
    r_pol_wat_list = []
    r_pol_oil_list = []
    for i in range(len(product_sales_df)):

        single_product_dict = product_sales_df['Product Sustainability Metrics'].iloc[i]
        if single_product_dict != 'NA':
            carbon_dict = single_product_dict['carbon_footprint_analysis_table']
            v_pol_co2 = carbon_dict['dog_beds_made_from_virgin_polyester']['co2_per_ton']
            v_pol_wat = carbon_dict['dog_beds_made_from_virgin_polyester']['water_used_bath_tubs']
            v_pol_oil = carbon_dict['dog_beds_made_from_virgin_polyester']['barrels_of_oil']
            v_pol_co2_list.append(v_pol_co2)
            v_pol_wat_list.append(v_pol_wat)
            v_pol_oil_list.append(v_pol_oil)

            r_pol_co2 = carbon_dict['dog_beds_made_from_recycled_polyester']['co2_per_ton']
            r_pol_wat = carbon_dict['dog_beds_made_from_recycled_polyester']['water_used_bath_tubs']
            r_pol_oil = carbon_dict['dog_beds_made_from_recycled_polyester']['barrels_of_oil']
            r_pol_co2_list.append(r_pol_co2)
            r_pol_wat_list.append(r_pol_wat)
            r_pol_oil_list.append(r_pol_oil)

    avg_v_pol_co2 = int(sum(v_pol_co2_list))
    avg_r_pol_co2 = int(sum(r_pol_co2_list))

    v_pol_wat_total = int(sum(v_pol_wat_list))
    v_pol_oil_total = int(sum(v_pol_oil_list))

    r_pol_wat_total = int(sum(r_pol_wat_list))
    r_pol_oil_total = int(sum(r_pol_oil_list))


    carbon_footprint_analysis_table = {
        'dog_beds_made_from_virgin_polyester' : {'co2_per_ton': avg_v_pol_co2, 'water_used_bath_tubs': v_pol_wat_total, 'barrels_of_oil': v_pol_oil_total},
        'dog_beds_made_from_recycled_polyester' : {'co2_per_ton': avg_r_pol_co2, 'water_used_bath_tubs': r_pol_wat_total, 'barrels_of_oil': r_pol_oil_total},
        'total_saving' : {'co2_per_ton': avg_v_pol_co2-avg_r_pol_co2, 'water_used_bath_tubs': v_pol_wat_total-r_pol_wat_total, 'barrels_of_oil': v_pol_oil_total-r_pol_oil_total}
    }

    return carbon_footprint_analysis_table


def generate_leather_dict_from_product_sales_df(product_sales_df):  
    ## Build functionality to calculate all metrics for the polyester table

    l_col_wat_list = []
    l_col_bat_list = []
    r_col_wat_list = []
    r_col_bat_list = []

    l_lea_wat_list = []
    l_lea_bat_list = []
    r_lea_wat_list = []
    r_lea_bat_list = []
    for i in range(len(product_sales_df)):

        single_product_dict = product_sales_df['Product Sustainability Metrics'].iloc[i]
        if single_product_dict != 'NA':
            leather_dict = single_product_dict['leather_collar_and_leash_analysis_table']
            l_col_wat = leather_dict['traditional_leather_collar']['litres_of_water_used']
            l_col_bat = leather_dict['traditional_leather_collar']['water_used_bath_tubs']
            r_col_wat = leather_dict['recycled_leather_collar']['litres_of_water_used']
            r_col_bat = leather_dict['recycled_leather_collar']['water_used_bath_tubs']

            l_col_wat_list.append(l_col_wat)
            l_col_bat_list.append(l_col_bat)
            r_col_wat_list.append(r_col_wat)
            r_col_bat_list.append(r_col_bat)

            l_lea_wat = leather_dict['traditional_leather_leash']['litres_of_water_used']
            l_lea_bat = leather_dict['traditional_leather_leash']['water_used_bath_tubs']
            r_lea_wat = leather_dict['recycled_leather_leash']['litres_of_water_used']
            r_lea_bat = leather_dict['recycled_leather_leash']['water_used_bath_tubs']

            l_lea_wat_list.append(l_lea_wat)
            l_lea_bat_list.append(l_lea_bat)
            r_lea_wat_list.append(r_lea_wat)
            r_lea_bat_list.append(r_lea_bat)

    l_col_wat_total = int(sum(l_col_wat_list))
    l_col_bat_total = int(sum(l_col_bat_list))
    r_col_wat_total = int(sum(r_col_wat_list))
    r_col_bat_total = int(sum(r_col_bat_list))

    l_lea_wat_total = int(sum(l_lea_wat_list))
    l_lea_bat_total = int(sum(l_lea_bat_list))
    r_lea_wat_total = int(sum(r_lea_wat_list))
    r_lea_bat_total = int(sum(r_lea_bat_list))

    leather_collar_and_leash_analysis_table = {
        'traditional_leather_collar' : {'litres_of_water_used': l_col_wat_total, 'water_used_bath_tubs': l_col_bat_total},
        'recycled_leather_collar' : {'litres_of_water_used': r_col_wat_total, 'water_used_bath_tubs': r_col_bat_total},
        'collar_water_saving' : {'litres_of_water_used': l_col_wat_total-r_col_wat_total, 'water_used_bath_tubs': l_col_bat_total-r_col_bat_total},
        'traditional_leather_leash' : {'litres_of_water_used': l_lea_wat_total, 'water_used_bath_tubs': l_lea_bat_total},
        'recycled_leather_leash' : {'litres_of_water_used': r_lea_wat_total, 'water_used_bath_tubs': r_lea_bat_total},
        'leash_water_saving' : {'litres_of_water_used': l_lea_wat_total-r_lea_wat_total, 'water_used_bath_tubs': l_lea_bat_total-r_lea_bat_total},
    }

    return leather_collar_and_leash_analysis_table