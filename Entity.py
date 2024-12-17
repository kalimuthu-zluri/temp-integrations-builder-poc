
class Entity:
    def __init__(self):
        self.static_request_config = {
            "Headers": [{ "Headerkey": 'added Header Value' }],
            "Params": [{ "queryKey": 'added query Value' }],
            "URL": {
                "protocol": 'https',
                "method": 'GET',
                "domain": 'pokeapi.co',
                "endpoint": 'api/v2/pokemon'
            },
            "Auth": {
                "type": 'Bearer',
                "token": '123'
            },
            "Body": {
                "type": 'JSON',
                "data": {}
            }
        }

        self.pagination_config = {
            "type": 'LIMIT_OFFSET',
            "limit": 100,
            "limitKey": 'limit',
            "offsetKey": 'offset',
            "breakCondition": ''
        }

        self.depenpencies = [
            {
                "entity": 'User',
                "fields": ['name']
            }
        ]

        self.responseContext = {
            "entity_locator": 'response.data.results',
            "save_path": 'pokemon_details'
        }
