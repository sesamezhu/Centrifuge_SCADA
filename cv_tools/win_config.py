import json

json_file_path = "configs/config.json"
json_sql_path = "configs/sql.json"


def read_json(file=json_file_path):
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_json(config):
    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)


def save_config(key, value):
    config = read_json()
    config[key] = value
    with open(json_file_path, 'w') as f:
        json.dump(config, f, indent=4)


def read_config(key):
    config = read_json()
    return config.get(key, None)


def save_video_item(index, key, value):
    config = read_json()
    videos = config.get("videos")
    videos[index][key] = value
    write_json(config)


def save_video_allitem(index, trandict):
    config = read_json()
    videos = config.get("videos")[index]
    for key in trandict:
        if key.startswith("angle-") or key.startswith("angle2-"):
            videos[key] = int(trandict[key])
        elif key.startswith("distance-"):
            videos[key] = float(trandict[key])
        else:
            videos[key] = trandict[key]
    write_json(config)


json_config = read_json()
json_grid = json_config["grid"]
