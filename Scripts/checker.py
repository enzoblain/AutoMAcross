import json

def config_checker():
    config_file = 'config.json'
    with open(config_file, 'r') as file:
        config = json.load(file)

    keys = config.keys()

    if 'Error handling' not in keys:
        raise SyntaxError('Error handling is not defined in the config file')
    else:
        if config['Error handling'] not in ['Adapt', 'Delete']:
            raise SyntaxError('Error handling should be either Adapt or Delete')
        
    return config