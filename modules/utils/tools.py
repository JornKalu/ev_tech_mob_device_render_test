import json

def is_json(jstr=None):
    if jstr != None:
        try:
            json_obj = json.loads(jstr)
            return True
        except ValueError as e: 
            return False
        return True
    else:
        return False

def json_loader(jstr=None):
    if is_json(jstr=jstr) == False:
        return None
    else:
        return json.loads(jstr)
    
