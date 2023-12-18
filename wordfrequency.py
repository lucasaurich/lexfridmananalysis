import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# Download NLTK resources (run this once)
nltk.download('punkt')
nltk.download('stopwords')

# Load stopwords
stop_words = set(stopwords.words('english'))

# Additional words to exclude
exclude_words = set([
    'segment', 'youtube', 'speaker', 'lex', 'fridman', 'guest', 'watch', 'text', 'timestamp', 'https'  # Add more names if needed     
])

# Read the transcript file
with open('/Users/lucasaurich/Desktop/Podcasts/podcast_transcripts.txt', 'r', encoding='utf-8') as file:
    transcripts = file.read()

# Tokenize and remove stopwords
tokens = word_tokenize(transcripts)
filtered_tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stop_words and word.lower() not in exclude_words]

# Word frequency analysis
freq_dist = FreqDist(filtered_tokens)
top_words = freq_dist.most_common(10)

# Display the top words
print("Top 10 Most Frequent Words:")
for word, frequency in top_words:
    print(f"{word}: {frequency}")

# Plot the frequency distribution
plt.figure(figsize=(10, 5))
freq_dist.plot(20, cumulative=False)
plt.title('Word Frequency Distribution')
plt.show()
