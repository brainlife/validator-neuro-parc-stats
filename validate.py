#!/usr/bin/env python3

import os
import json

with open('config.json', encoding='utf8') as config_json:
    config = json.load(config_json)

results = {"errors": [], "warnings": []}

#symlink the input in - no change to the data
if not os.path.exists("secondary"):
    os.symlink(config["parc-stats"], "secondary")

if not os.path.exists("output"):
    os.symlink(config["parc-stats"], "output")

with open("product.json", "w") as fp:
    json.dump(results, fp)

print("done");
