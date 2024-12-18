import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json

# Load your dataset
df = pd.read_json("./eval_output/incorrect_eval_predictions.jsonl", lines=True)

# Example: Analyze label distribution
print(df['label'].value_counts())
print(df['predicted_label'].value_counts())

df_a = pd.read_json("./contrast_data.jsonl", lines=True)

# Example: Analyze label distribution
print('contrast set breakdown of classes')
print(df_a['label'].value_counts())

# Example: Analyze length of premises and hypotheses
# Correctly calculate the number of tokens
df['premise_length'] = df['premise'].apply(lambda x: len(x.split()))
df['hypothesis_length'] = df['hypothesis'].apply(lambda x: len(x.split()))

# Visualize length distributions
df[['premise_length', 'hypothesis_length']].hist(bins=30, alpha=0.7, figsize=(10, 6))
plt.xlabel('Number of Tokens')
plt.ylabel('Frequency')
plt.title('Sentence Length Distributions for Premises and Hypotheses')
plt.legend(['Premise Length', 'Hypothesis Length'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


#attempting dataset cartography
# Load the output file
output_file_path = "./eval_output/incorrect_eval_predictions.jsonl"

# Initialize a list to store the parsed examples
examples = []

with open(output_file_path, 'r') as f:
    for line in f:
        example = json.loads(line)
        examples.append(example)

# Check the structure of the loaded data (print the first few examples)
#print(examples[:2])  # Shows first two examples

def compute_confidence(predicted_scores, true_label):
    # Convert logits to probabilities using softmax
    probs = np.exp(predicted_scores) / np.sum(np.exp(predicted_scores))
    # Get the confidence for the true label
    confidence = probs[true_label]
    return confidence

# Add a 'confidence' field to each example
for example in examples:
    true_label = example['label']
    predicted_scores = example['predicted_scores']
    example['confidence'] = compute_confidence(predicted_scores, true_label)

# Check the updated examples with confidence values
#print(examples[:2])

def compute_variability(confidences):
    return np.std(confidences)

# For the example, if you have multiple confidence values from different epochs:
#for example in examples:
    # If you tracked multiple confidences over epochs:
    # example['variability'] = compute_variability(example['epoch_confidences'])
    # For now, using single confidence from a single evaluation phase:
#    example['variability'] = 0.0  # If you only have single confidence values

# Check the updated examples with variability
#print(examples[:2])

# Extract mean confidence and variability values
mean_confidences = [example['confidence'] for example in examples]
#variabilities = [example['variability'] for example in examples]

# Create the scatter plot
#plt.scatter(mean_confidences, variabilities, alpha=0.7)
#plt.xlabel("Mean Confidence")
#plt.ylabel("Variability")
#plt.title("Dataset Cartography")
#plt.show()

# Save the updated examples to a new file with confidence values
output_with_confidence_file_path = "./eval_output/eval_predictions_with_confidence.jsonl"

with open(output_with_confidence_file_path, 'w', encoding='utf-8') as f:
    for example in examples:
        f.write(json.dumps(example) + '\n')

import json
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# Load the mispredictions file
file_path = output_with_confidence_file_path  # Replace with your file path
data = []

# Read the data from the file
with open(file_path, "r") as f:
    for line in f:
        data.append(json.loads(line))

# Organize confidence scores by gold label
confidence_by_label = defaultdict(list)

# Map gold labels to their string representations for readability
label_map = {0: "entailment", 1: "neutral", 2: "contradiction"}

for entry in data:
    gold_label = entry["label"]
    confidence = entry["confidence"]
    confidence_by_label[label_map[gold_label]].append(confidence)

# Plot histograms
plt.figure(figsize=(12, 8))

for i, (label, confidences) in enumerate(confidence_by_label.items(), 1):
    plt.subplot(1, 3, i)  # Create subplots for each label
    plt.hist(confidences, bins=np.linspace(0, 1, 20), alpha=0.7, color='blue', edgecolor='black')
    plt.title(f"Confidence Scores: {label.capitalize()}")
    plt.xlabel("Confidence")
    plt.ylabel("Frequency")
    plt.grid(True)

# Adjust layout and display
plt.tight_layout()
plt.show()