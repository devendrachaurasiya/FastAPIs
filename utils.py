from multiprocessing import Pool
import logging
from datetime import datetime


logging.basicConfig(level=logging.INFO)

def to_add_numbers(input_data):
    try:
        return input_data
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return None

def process_data(inputs):
    with Pool() as pool:
        results = pool.map(to_add_numbers, inputs)
    return results