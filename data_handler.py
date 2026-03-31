import json
import os

def get_file_path(username):
    return f"data_{username}.json"  # since you're using data.json directly

def load_data(username):
    import os
    import json

    file_path = get_file_path(username)

    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as file:
        return json.load(file)


def save_data(username, data):
    import json

    file_path = get_file_path(username)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)