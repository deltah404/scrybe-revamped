import json

def get_config(key: str):
    with open('resources/config.json') as fp:
        try:
            return json.load(fp)[key]
        except KeyError:
            return None
