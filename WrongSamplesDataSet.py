import json

def extract_and_save_data(input_file, output_file):
  with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
      data = json.loads(line)

      new_data = {
          "premise": data["premise"],
          "hypothesis": data["hypothesis"],
          "label": data["label"]
      }
      json.dump(new_data, outfile)
      outfile.write('\n')

# Replace 'your_input_file.jsonl' and 'new_data.jsonl' with the actual file paths
input_file = "./eval_output/incorrect_eval_predictions.jsonl"
output_file = "wrong_pred_dataset.jsonl"
extract_and_save_data(input_file, output_file)