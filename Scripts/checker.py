import json

def config_checker() -> dict:
    config_file = 'config.json'
    with open(config_file, 'r') as file:
        config = json.load(file)

    if 'Api' not in config:
        raise KeyError("Missing 'Api' configuration")
    if 'Key' not in config['Api'] or not config['Api']['Key']:
        raise ValueError("Missing or empty 'Api Key'")
    if 'Url' not in config['Api'] or not config['Api']['Url']:
        raise ValueError("Missing or empty 'Api Url'")

    if 'Error handling' not in config:
        raise KeyError("Missing 'Error handling' configuration")
    if config['Error handling'] not in ['Adapt', 'Delete']:
        raise SyntaxError("Error handling should be either 'Adapt' or 'Delete'")

    if 'Time zone' not in config or not config['Time zone']:
        raise ValueError("Missing or empty 'Time zone'")

    if 'Symbol' not in config or not config['Symbol']:
        raise ValueError("Missing or empty 'Symbol'")

    if 'Time range' not in config or not config['Time range']:
        raise ValueError("Missing or empty 'Time range'")
    
    if 'Average 1' not in config or not isinstance(config['Average 1'], int):
        raise ValueError("Missing or invalid 'Average 1'")

    if 'Average 2' not in config or not isinstance(config['Average 2'], int):
        raise ValueError("Missing or invalid 'Average 2'")

    if 'Average type' not in config or config['Average type'] not in ['Global', 'Local']:
        raise ValueError("Missing or invalid 'Average type'")

    if 'Balance' not in config or not isinstance(config['Balance'], (int, float)):
        raise ValueError("Missing or invalid 'Balance'")

    return config

    return config