import json
import os

# Placeholder script for pushing JSON data to Google Business Profile
# TODO: integrate with GMB API using credentials.json

def load_json_files(path):
    data = []
    for file in os.listdir(path):
        if file.endswith(".json"):
            with open(os.path.join(path, file), "r", encoding="utf-8") as f:
                data.append(json.load(f))
    return data

if __name__ == "__main__":
    seo_path = "../seo-json-data"
    if os.path.exists(seo_path):
        all_data = load_json_files(seo_path)
        print(f"Loaded {len(all_data)} location files.")
    else:
        print("SEO JSON data folder not found.")
