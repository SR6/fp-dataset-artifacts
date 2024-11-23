import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json

# Load your dataset
df = pd.read_json("./eval_output/incorrect_eval_predictions.jsonl", lines=True)

# Example: Analyze label distribution
print(df['label'].value_counts())
print(df['predicted_label'].value_counts())

# Example: Analyze length of premises and hypotheses
df['premise_length'] = df['premise'].apply(len)
df['hypothesis_length'] = df['hypothesis'].apply(len)

# Visualize length distributions
df[['premise_length', 'hypothesis_length']].hist(bins=30)
plt.xlabel('Number of Tokens distribution')
plt.ylabel('Length of text')
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