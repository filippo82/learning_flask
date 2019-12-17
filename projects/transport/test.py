import requests

from pprint import pprint

url = 'http://transport.opendata.ch/v1/'

def _get(resource: str, payload: dict, verbose: bool):
    url_resource = f"{url}{resource}"
    r = requests.get(url_resource, params=payload)
    if verbose:
        print(f"The status code is {r.status_code}")
    return r.json()

def get_locations(payload: dict, verbose: bool):
    return _get('locations', payload, verbose)['stations']

def get_stationboard(payload: dict, verbose: bool):
    return _get('stationboard', payload, verbose)


if __name__ == '__main__':
    # Locations
    payload = {'query': ''}
    payload['query'] = 'stauff'

    verbose = True

    stations = get_locations(payload, verbose)

    for station in stations:
        if station['id'] is not None:
            print(f"{station['id']}: {station['name']}")

    # Stationboard
    payload = dict()
    payload['id'] = 8591381
    payload['limit'] = 10
    payload['type'] = 'departure'

    verbose = True

    departures = get_stationboard(payload, verbose)

    for d in departures['stationboard']:
        # pprint(d.keys()) # ['stop', 'name', 'category', 'subcategory', 'categoryCode', 'number', 'operator', 'to', 'passList', 'capacity1st', 'capacity2nd']
        pprint(f"{d['category']}{d['number']} at {d['stop']['departure']}")
        # print(f"{d['name']}{d['']}{}"")
        print('')
        # if station['id'] is not None:
        #     print(f"{station['name']}")
