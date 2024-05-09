
import requests
import pandas as pd
from urllib.parse import urlencode

class GetStravaData:

    post_auth_redirected_url = 'http://localhost:8081'
    authorisation_uri = 'https://www.strava.com/oauth/authorize'
    token_url = 'https://www.strava.com/oauth/token'
    activities_url = 'https://www.strava.com/api/v3/athlete/activities'

    def __init__(self, client_id, client_secret, athlete_id):
        self.client_id = client_id
        self.client_secret = client_secret
        self.athlete_id = athlete_id

    def authorise_user_request(self):
        params = {
            'client_id': self.client_id,
            'redirect_uri': self.post_auth_redirected_url,
            'response_type': 'code',
            'scope': 'activity:read_all',  # Adjust scope as needed
        }
        auth_url = f"{self.authorisation_uri}?{urlencode(params)}"
        print("Grant authorise access:")
        print(auth_url)
        authorisation_code = input("Enter the post authorisation code: ")
        return authorisation_code

    def get_access_token(self, authorisation_code):
        try:
            data = {
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'code': authorisation_code,
                'grant_type': 'authorization_code',
            }
            response = requests.post(self.token_url, data=data)
            response.raise_for_status()  # Raise an exception for HTTP errors
            access_token = response.json()['access_token']
            return access_token
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def fetch_strava_activities(self, access_token):
        headers = {'Authorization': f'Bearer {access_token}'}
        params = {'athlete_id': self.athlete_id}
        response = requests.get(self.activities_url, headers=headers, params=params)
        status_code = response.status_code
        if status_code == 200:
            activities = response.json()
            return activities
        else:
            return response

    def fetch_activities_df(self):
        authorisation_code = self.authorise_user_request()
        access_token = self.get_access_token(authorisation_code)
        athlete_activities = self.fetch_strava_activities(access_token)
        df = pd.DataFrame(athlete_activities)
        return df
