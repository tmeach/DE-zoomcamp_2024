import io
import pandas as pd
import requests
# if 'data_loader' not in globals():
#     from mage_ai.data_preparation.decorators import data_loader
# if 'test' not in globals():
#     from mage_ai.data_preparation.decorators import test

def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    combined_df = pd.DataFrame()

    urls = [
    "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2019-01.parquet"
    ]
    for url in urls:
        df = pd.read_parquet(url)
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


# Вызываем функцию и сохраняем результат в переменной
data_frame = load_data_from_api()

# Выводим на печать датафрейм
print(data_frame)

# @test
# def test_output(output, *args) -> None:
#     """
#     Template code for testing the output of the block.
#     """
#     assert output is not None, 'The output is undefined'
