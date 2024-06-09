def commandWithOutputFile(f):
    
    def wrapper(*args, **kwargs):
        
        data = f(*args, **kwargs)
        for i in data:
            file_data = {
                "file" : i["name"],
                "mode" : i.get("mode", "w"),
            }
            
            if file_data["mode"] == "w":
                file_data["encoding"] = 'utf-8'
            
            with open(**file_data) as file:
                file.write(i["data"])

    return wrapper