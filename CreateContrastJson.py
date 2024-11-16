import json

data = [
    {"premise": "This is the first sentence.","hypothesis":"", "label": 0},
    {"premise": "Another sentence.", "hypothesis": "","label": 1},

]

with open('contrast_data.jsonl', 'w') as f:
    for item in data:
        json.dump(item, f)
        f.write('\n')