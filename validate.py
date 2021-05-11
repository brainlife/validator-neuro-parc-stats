#!/usr/bin/env python3

import os
import json

with open('config.json', encoding='utf8') as config_json:
    config = json.load(config_json)

results = {"errors": [], "warnings": []}

if not os.path.exists("secondary"):
    os.mkdir("secondary")

if not os.path.exists("output"):
    os.mkdir("output")

#TODO - validate and create vis using reference data

with open("product.json", "w") as fp:
    json.dump(results, fp, cls=NumpyEncoder)

print("done");
