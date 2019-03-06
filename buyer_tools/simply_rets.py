import requests
from requests.auth import HTTPBasicAuth

from buyer_tools.constants import (RETS_KEY_MAP, BAD_REQUEST_MESSAGE, LOGIN_REQUIRED_MESSAGE,
                                   ERRORED_KEY, FORBIDDEN_MESSAGE, API_RATE_LIMIT_HIT_MESSAGE,
                                   SERVER_ERROR_MESSAGE, UNKNOWN_ERROR_MESSAGE)
from gwenn_demo.settings.prod import (SIMPLY_RETS_API_KEY, SIMPLY_RETS_API_SECRET, SIMPLY_REST_DOMAIN)


class SimplyRets:

    def __init__(self):
        self.api_key = SIMPLY_RETS_API_KEY
        self.api_secret = SIMPLY_RETS_API_SECRET
        self.domain = SIMPLY_REST_DOMAIN

    def create_parameters(self, data):
        parameters = {}

        for next_key, next_rets_key in RETS_KEY_MAP.items():

            if next_key in data:

                # do not include empty lists
                if isinstance(data[next_key], list) and len(data[next_key]) == 0:
                    continue
                else:
                    parameters[next_rets_key] = data[next_key]

        return parameters

    def make_rets_call(self, url, parameters):
        results = {ERRORED_KEY: UNKNOWN_ERROR_MESSAGE}
        response = requests.get(url=url,
                                params=parameters,
                                auth=HTTPBasicAuth(self.api_key, self.api_secret))

        if response.ok:
            results = response.json()
        elif response.status_code == 400:
            results = {ERRORED_KEY: BAD_REQUEST_MESSAGE}
        elif response.status_code == 401:
            results = {ERRORED_KEY: LOGIN_REQUIRED_MESSAGE}
        elif response.status_code == 403:
            results = {ERRORED_KEY: FORBIDDEN_MESSAGE}
        elif response.status_code == 429:
            results = {ERRORED_KEY: API_RATE_LIMIT_HIT_MESSAGE}
        elif response.status_code == 500:
            results = {ERRORED_KEY: SERVER_ERROR_MESSAGE}

        return results

    def get_properties(self, data, limit=50, offset=0):
        url = f"{self.domain}/properties"
        parameters = self.create_parameters(data)
        parameters["limit"] = limit
        parameters["lastId"] = offset

        property_results = self.make_rets_call(url=url, parameters=parameters)

        return property_results


