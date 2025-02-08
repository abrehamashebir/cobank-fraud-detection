import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, 
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename='load_data.log')

def load_data(file_path):
    try:
        logging.info(f'Loading data from {file_path}')
        data = pd.read_csv(file_path)
        logging.info('Data loaded successfully')
        return data
    except Exception as e:
        logging.error(f'Error loading data: {e}')