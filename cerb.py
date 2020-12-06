import cerberus
# schema = {'name': {'type': 'string'}, 'age': {'type': 'integer', 'min': 10}}
# document = {'name': 'Little Joe', 'age': 1}

    # "post code": "90210",
    # "country": "United States",
    # "country abbreviation": "US",
schema = {'post code': {'type': 'string'},'country': {'type':'string'},'country abbreviation':{'type':'string'}}
crb = {'post code': '90210', 'country': 'United States','country abbreviation': 'US'}
print(type(schema))
v = cerberus.Validator()
# v.allow_unknown = True
if v.validate(crb, schema):
    print('valid')
else:
    print(v.errors)

# v.validate(document)
# assert v.validate(response.json(), schema)