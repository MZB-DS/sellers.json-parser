# sellers.json-parser
sellers.json provides a mechanism to enable buyers to discover who the entities are that are either direct sellers of or intermediaries in the selling of digital advertising. This repository contains python code to parse sellers.json of any number for adtech companies and import the required parameters in an excel format. 

## How to use this code
1. Insert all the sellers.json link you want to fetch in the python list: urls.
2. Rename the output file.
3. Execute the python ```sellers_json_parser.py```.

## Future features
To accept input in a text file instead of entering them in the python list.

## Dependencies
- Python3 any version
- Python package:  pandas==1.0.3, requests==2.22.0

```pip3 install pandas==1.0.3 requests==2.22.0```
