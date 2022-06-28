import os
import json 


def where_json(file_name):
    return os.path.exists(file_name)

def check_database_avaiable():
    if where_json('database_file/data.json'):
        with open('database_file/data.json', 'r',encoding='utf-8') as outfile:
            try:  
                data = json.loads(outfile.read())
            except:
                with open('database_file/data.json', 'w', encoding='utf-8') as outfile:  
                    json.dump(list(), outfile)      
        pass 
    
    else:   
        with open('database_file/data.json', 'w') as outfile:  
            json.dump(list(), outfile)  

def local_img_storage():
    try:
        os.mkdir('local_image_url')
    except:
        pass
    