#!/bin/bash

#     command = [script, json.dumps(config)] is the python line that calls this script. Now get stuff form the config

config="$1"
# use jq to parse the json
input_file=$(echo $config | jq -r '.input_file')
output_file=$(echo $config | jq -r '.output_file')
Zoteropath=$(echo $config | jq -r '.Zoteropath')
Presspath=$(echo $config | jq -r '.Presspath')