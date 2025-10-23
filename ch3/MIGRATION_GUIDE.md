# Migration Guide: From Polyglot to NLTK Stemmers

## Quick Fix for Existing Code

If you have code using polyglot for stemming, here's how to migrate to NLTK:

### Before (Broken - Polyglot)

```python
from polyglot.text import Word

word = "happiness"
w = Word(word, language="en")
print(w.morphemes)
```

### After (Working - NLTK)

```python
from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer("english")
word = "happiness"
print(stemmer.stem(word))
```

## Common Migration Patterns

### Pattern 1: Simple Stemming

**Polyglot:**
```python
from polyglot.text import Word

words = ["running", "flies", "happiness"]
for w in words:
    word_obj = Word(w, language="en")
    print(f"{w} -> {word_obj.morphemes}")
```

**NLTK:**
```python
from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer("english")
words = ["running", "flies", "happiness"]
for w in words:
    print(f"{w} -> {stemmer.stem(w)}")
```

### Pattern 2: Batch Processing

**Polyglot:**
```python
from polyglot.text import Text

text = Text("The runners were running quickly")
for word in text.words:
    print(f"{word} -> {word.morphemes}")
```

**NLTK:**
```python
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

stemmer = SnowballStemmer("english")
text = "The runners were running quickly"
words = word_tokenize(text)
for word in words:
    print(f"{word} -> {stemmer.stem(word)}")
```

### Pattern 3: Multiple Languages

**Polyglot:**
```python
from polyglot.text import Word

word_en = Word("running", language="en")
word_es = Word("corriendo", language="es")
```

**NLTK:**
```python
from nltk.stem import SnowballStemmer

stemmer_en = SnowballStemmer("english")
stemmer_es = SnowballStemmer("spanish")

print(stemmer_en.stem("running"))
print(stemmer_es.stem("corriendo"))
```

## Supported Languages in NLTK Snowball Stemmer

NLTK's SnowballStemmer supports the following languages:

- Arabic
- Danish
- Dutch
- English
- Finnish
- French
- German
- Hungarian
- Italian
- Norwegian
- Portuguese
- Romanian
- Russian
- Spanish
- Swedish
- Turkish

## When to Use Each Stemmer

### Porter Stemmer
- **Use when**: You need the most widely-used stemming algorithm
- **Pros**: Well-documented, predictable behavior
- **Cons**: Older algorithm, some edge cases

### Snowball Stemmer
- **Use when**: You need improved accuracy over Porter
- **Pros**: Better handling of edge cases, multi-language support
- **Cons**: Slightly slower than Porter

### Lancaster Stemmer
- **Use when**: You need aggressive stemming
- **Pros**: Very fast, reduces words to minimal stems
- **Cons**: Can over-stem, reducing accuracy

## Complete Example: Chapter 3 Code

Here's the complete updated code for Chapter 3:

```python
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer

def demonstrate_stemmers():
    words = ["happiness", "unkind", "dogs", "expected", "running", "flies"]
    
    porter = PorterStemmer()
    snowball = SnowballStemmer("english")
    lancaster = LancasterStemmer()
    
    print("{:<15} {:<15} {:<15} {:<15}".format(
        "Word", "Porter", "Snowball", "Lancaster"
    ))
    print("-" * 60)
    
    for word in words:
        print("{:<15} {:<15} {:<15} {:<15}".format(
            word,
            porter.stem(word),
            snowball.stem(word),
            lancaster.stem(word)
        ))

if __name__ == "__main__":
    demonstrate_stemmers()
```

## Troubleshooting

### Issue: ModuleNotFoundError: No module named 'nltk'

**Solution:**
```bash
pip install nltk
```

### Issue: Resource 'tokenizers/punkt' not found

**Solution:**
```python
import nltk
nltk.download('punkt')
```

### Issue: Need morphological analysis, not just stemming

**Solution:** Use spaCy for lemmatization:
```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("The runners were running quickly")
for token in doc:
    print(f"{token.text} -> {token.lemma_}")
```

## Additional Resources

- [NLTK Stemming Documentation](https://www.nltk.org/howto/stem.html)
- [Difference between Stemming and Lemmatization](https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html)
- [spaCy Lemmatization Guide](https://spacy.io/usage/linguistic-features#lemmatization)

## Need Help?

If you encounter issues with this migration:
1. Check that NLTK is installed: `pip list | grep nltk`
2. Verify Python version: `python --version` (Python 3.6+ recommended)
3. Review the NLTK documentation for your specific use case
4. Consider using spaCy for more advanced NLP tasks
