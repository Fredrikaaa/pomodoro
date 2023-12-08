import json

work_time = 25
break_time = 5
long_break_time = 20
long_break_after = 4

def json_print(data, tooltip):
    output = {
        "text": data,
        "tooltip": tooltip,
        "class": "custom"
    }
    print(json.dumps(output))

