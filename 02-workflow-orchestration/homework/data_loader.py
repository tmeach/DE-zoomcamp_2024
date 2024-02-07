import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/'

    months = [10, 11, 12]

    dataframes = []

    for month in months:
        filename = f"{url}green_tripdata_2020-{month}.csv.gz"
        
        #print(filename)

        parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
        data = pd.read_csv(filename, sep=",", compression="gzip", parse_dates=parse_dates)
        dataframes.append(data)

    final_quarter_data = pd.concat(dataframes, ignore_index=True)

    return final_quarter_data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
