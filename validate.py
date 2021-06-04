#!/usr/bin/env python3

import os
import json

with open('config.json', encoding='utf8') as config_json:
    config = json.load(config_json)

results = {"errors": [], "warnings": []}

#symlink the input in - no change to the data
if not os.path.exists("output"):
    os.mkdir("output")

if not os.path.exists(config["parc-stats"]):
    results["errors"].append("Can't find parc-stats directory");
else:
    if not os.path.exists("output/parc-stats"):
        os.symlink("../"+config["parc-stats"], "output/parc-stats")

#we don't have anything for secondary but app-secondary-archive requires it
if not os.path.exists("secondary"):
    os.mkdir("secondary")

with open("product.json", "w") as fp:
    json.dump(results, fp)

print("done");
