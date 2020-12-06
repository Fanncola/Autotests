import requests
import cerberus
def test_get_locations():
    response = requests.get("http://api.zippopotam.us/RU/101000")
    assert response.status_code == 200
    schema = {
        "post code": {"type": "string","allowed" : ["00210","101000"]},
        "country": {"type": "string"},
        "country abbreviation": {"type": "string"},
        "places": {"type": "list", "schema":{"type": "dict","schema":{
            "place name": {"type": "string"},
            'longitude': {"type": "string"},
            'state': {"type": "string"},
            'state abbreviation': {"type": "string"},
            'latitude': {"type": "string"}
        }}}
    }
    v = cerberus.Validator()
    assert v.validate(response.json(), schema)

