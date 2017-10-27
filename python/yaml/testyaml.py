#!/usr/bin/env python
import yaml
from jsonschema import validate as js_v, exceptions as js_e
with open("midescriptor.yaml", 'r') as stream:
    try:
        data = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

print data
print yaml.dump(data)
#js_v(data, used_schema)

