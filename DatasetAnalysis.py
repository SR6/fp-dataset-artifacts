from datasets import load_dataset

# Load the SNLI dataset
snli_dataset = load_dataset("snli")
train_dataset = snli_dataset['train']
from transformers import AutoTokenizer

# Load a tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Tokenize and calculate the number of tokens for premise and hypothesis
def count_tokens(example):
    #premise_tokens = len(tokenizer.tokenize(example['premise']))
    hypothesis_tokens = len(tokenizer.tokenize(example['hypothesis']))
    return {
        'num_tokens': hypothesis_tokens,  # Total tokens
        'label': example['label']  # 0 = entailment, 1 = neutral, 2 = contradiction
    }

def count_classes(df):
    """
    Count the number of examples for each NLI class.
    """
    class_counts = df['label'].value_counts()
    return class_counts


# Apply the function to calculate token counts
token_counts = train_dataset.map(count_tokens)
import pandas as pd

# Filter out invalid labels (-1)
filtered_data = token_counts.filter(lambda x: x['label'] != -1)


# Create a DataFrame
df = pd.DataFrame({
    'num_tokens': filtered_data['num_tokens'],
    'label': filtered_data['label']
})

# Get class counts
class_counts = count_classes(df)
print("Class Counts:")
print(class_counts)

# Map labels to class names
label_mapping = {0: 'entailment', 1: 'neutral', 2: 'contradiction'}
df['label'] = df['label'].map(label_mapping)

# Calculate the probability mass function (PMF)
pmf_data = df.groupby(['label', 'num_tokens']).size().reset_index(name='count')
pmf_data['probability_mass'] = pmf_data['count'] / pmf_data.groupby('label')['count'].transform('sum')
import matplotlib.pyplot as plt
import seaborn as sns

# Create the plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=pmf_data, x='num_tokens', y='probability_mass', hue='label', marker='o')

# Add labels and legend
plt.title('Token Count Distribution by NLI Class', fontsize=16)
plt.xlabel('Number of Tokens (Hypothesis)', fontsize=14)
plt.ylabel('Probability Mass', fontsize=14)
plt.legend(title='Class', fontsize=12)
plt.grid(True)
plt.xlim(0,30)
# Show the plot
plt.show()


import matplotlib.pyplot as plt

# Load the SNLI dataset if not already loaded
# snli = load_dataset("snli", split="train")  # Uncomment if you need to load it

def compute_lengths_from_dataset(dataset):
    premise_lengths = dataset["premise"]
    hypothesis_lengths = dataset["hypothesis"]

    # Tokenize and compute lengths
    premise_lengths = [len(p.split()) for p in premise_lengths]
    hypothesis_lengths = [len(h.split()) for h in hypothesis_lengths]

    return premise_lengths, hypothesis_lengths

def plot_length_distribution(lengths, title, color):
    plt.figure(figsize=(10, 6))
    plt.hist(lengths, bins=range(0, max(lengths) + 5, 5), color=color, alpha=0.7, edgecolor='black')
    plt.title(title)
    plt.xlabel('Sentence Length (Number of Tokens)')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Compute lengths
premise_lengths, hypothesis_lengths = compute_lengths_from_dataset(train_dataset)

# Plot the distributions
plot_length_distribution(premise_lengths, "Premise Sentence Length Distribution", "blue")
plot_length_distribution(hypothesis_lengths, "Hypothesis Sentence Length Distribution", "green")

