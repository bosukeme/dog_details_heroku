import numpy as np
import pandas as pd
import math
from functions import calculations



"""
num_dog_beds_sold = 1000000
avg_bed_weight = 3.5 # it should be a drop-down with the only options being 2.5, 3.5 and 4.5\n",
lea_lea_sold = 1000000
lea_col_sold = 1000000

"""

def get_dog_details(num_dog_beds_sold, avg_bed_weight, lea_lea_sold,lea_col_sold):
    dog_bed_analysis_input_table, carbon_footprint_analysis_table, leather_collar_and_leash_analysis_input_table, leather_collar_and_leash_analysis_table, co2_saving_per_item_table = calculations.generate_sustainability_tables(num_dog_beds_sold, avg_bed_weight, lea_lea_sold, lea_col_sold)

    return dog_bed_analysis_input_table, carbon_footprint_analysis_table, leather_collar_and_leash_analysis_input_table, leather_collar_and_leash_analysis_table, co2_saving_per_item_table



def get_dog_details_csv(csv_file):


    product_sales_df = pd.read_csv(csv_file)

    product_sales_df = calculations.calculate_sustainability_metrics_for_sold_products(product_sales_df)

    """
    Generate the sustainability metric tables
    """
    carbon_footprint_analysis_table = calculations.generate_polyester_dict_from_product_sales_df(product_sales_df)
    leather_collar_and_leash_analysis_table = calculations.generate_leather_dict_from_product_sales_df(product_sales_df)
    co2_saving_per_item_table = calculations.generate_co2_savings_from_product_sales_df(product_sales_df)


    return carbon_footprint_analysis_table, leather_collar_and_leash_analysis_table, co2_saving_per_item_table





