import json
from apis.api_caller import ApiCaller
from helpers.date_converter import convert_unix_dateformat_to_utc
import pandas as pd


class ForecastApi(ApiCaller):
    BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast??'

    def __init__(self, city, uri=BASE_URL):
        super().__init__(city, uri)

    def get_city_name(self):
        return self.location

    def get_forecast_data_from_api(self):
        return self.get_data_from_api()

    def forecast_data_to_string(self):
        return json.dumps(self.get_forecast_data_from_api(), indent=2)

    def json_to_pandas_dataframe(self):
        data = self.get_forecast_data_from_api()
        normalized_pandas_data_frame = pd.json_normalize(data, record_path=['list'])
        normalized_pandas_data_frame['dt'] = normalized_pandas_data_frame['dt'].apply(
            lambda x: convert_unix_dateformat_to_utc(x))
        normalized_pandas_data_frame = normalized_pandas_data_frame.rename(
            columns={'dt': 'date', 'main.pressure': 'pressure', 'main.humidity': 'humidity', 'main.temp': 'temp'})
        cropped_pd_dataframe = normalized_pandas_data_frame.filter(['date', 'pressure', 'humidity', 'temp'], axis=1)
        dataframe_crouped_by_date = cropped_pd_dataframe.groupby('date').mean().round(0)
        return dataframe_crouped_by_date
