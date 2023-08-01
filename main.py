OUTPUT_FILE = "./merged.json" # Output file location
INPUT_FILES = [ # list of (FILE_LOCATION, TRACE_NAME)
    ("./trace-1.json", "trace-1"),
    ("./trace-2.json", "trace-2")
    ]



import json

merged_output = list()

for FILE_LOCATION, TRACE_NAME in INPUT_FILES:
    with open(FILE_LOCATION) as f:
        trace_obj = json.load(f)
        for event in trace_obj:
            event["pid"] = TRACE_NAME
        merged_output = merged_output + trace_obj


with open(OUTPUT_FILE, "w") as f:
    json.dump(merged_output, f)
