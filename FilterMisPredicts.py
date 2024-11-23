import json

# Define the input and output file paths
input_file = "./eval_output/eval_predictions_with_confidence.jsonl"  # Replace with your file path
output_file = "./eval_output/filtered_mispredictions.jsonl"
output_file_2 = "./eval_output/filtered_mispredictions_2.jsonl"

# Define the confidence range for filtering (e.g., intermediate confidence)
confidence_min = 0.2
confidence_max = 0.3

# Open the input file, filter examples, and write to the output file
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        example = json.loads(line)

        # Extract confidence
        confidence = example["confidence"]

        # Filter out examples that fall within the specified confidence range
        if confidence_min <= confidence <= confidence_max and example['label'] == 0:
            outfile.write(json.dumps(example) + "\n")

with open(input_file, "r") as infile, open(output_file_2, "w") as outfile:
    for line in infile:
        example = json.loads(line)
        if (example['label'] == 2):
            outfile.write(json.dumps(example) + "\n")

print(f"Filtered examples written to {output_file}")
