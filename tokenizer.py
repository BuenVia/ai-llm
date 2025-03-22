import re
from importlib.metadata import version
import tiktoken
print(f"tiktoken version: {version('tiktoken')}")

# 1 TOKENIZE THE SOURCE TEXT 
# Get the text and assign it to a variable
with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
# Split the words and punctuation, and remove whitespace
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
# Sort words by alphabetical order and remove duplicates, then add in text separator and unknown handler
all_tokens = sorted(set(preprocessed))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])
# Create a dictionary of vocabulary and an id value, which is an integer
vocab = {token:integer for integer,token in enumerate(all_tokens)}

# 2 TOKENIZE AND ENCODE/DECODE GIVEN TEXT
# Create the tokenizer class
class SimpleTokenizerv2:
    def __init__(self, vocab):
        self.str_to_int = vocab # Vocab:ID as attribute for encode and decode methods
        self.int_to_str = {i:s for s,i in vocab.items()} # Inverted ID:Vocab 

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [item if item in self.str_to_int else "<|unk|>" for item in preprocessed]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text
    
# tokenizer = SimpleTokenizerv2(vocab=vocab)
# text = """"It's the last he painted, you know," Mrs. Gisburn said with pardonable pride."""
# ids = tokenizer.encode(text)
# print(ids)
# print(tokenizer.decode(ids))

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = " <|endoftext|> ".join((text1, text2))

# tokenizer = SimpleTokenizerv2(vocab=vocab)
# print(tokenizer.encode(text))
# print(tokenizer.decode(tokenizer.encode(text)))

tokenizer = tiktoken.get_encoding("gpt2")
text = (
    "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
    "of someunknownPlace"
)
integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
print(integers)
strings = tokenizer.decode(integers)
print(strings)

