import pandas as pd
from io import StringIO
import requests


def looker_api_call(usr, pss, query):
    looker_url = "https://looker.clarityhs.com:19999/api/3.1"
    headers = {'Content-Type' : 'application/x-www-form-urlencoded'}
    body = {"client_id" : usr,
    "client_secret" : pss}
    login_url = f"{looker_url}/login"
    access_token = requests.post(login_url, headers = headers, data=body).json()['access_token']
    headers = {
    'Authorization' : 'token ' + access_token,
    'ContentType' : 'application/json'
    }
    df= requests.post(f"{looker_url}/queries/run/csv", json = query, headers = headers)
    return df

def looker_convert_to_df(df):
    df = pd.read_csv(StringIO(df.text))
    return df

