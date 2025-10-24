# Fixes for Chapter 3 wordsteam.py Issues

## Problem Summary

The original `3_1_wordsteam.py` script has two main issues:

1. **Python 2 to Python 3 Syntax**: The script uses Python 2 `print` statements without parentheses
2. **Polyglot Library HTTP 403 Error**: The polyglot library fails to download morpheme models due to server access issues

## Solutions Provided

### Solution 1: Fixed Original Script (Recommended for Learning)

**File**: `3_1_wordsteam.py` (updated)

**Changes Made**:
- Fixed all `print` statements to use Python 3 syntax with parentheses
- Script now runs without syntax errors

**Limitations**:
- Still requires polyglot library and its dependencies
- Polyglot morpheme functionality may fail due to server issues (HTTP 403)
- The polyglot project is deprecated and not actively maintained

**Dependencies Required**:
```bash
# System dependencies
sudo apt-get install libicu-dev pkg-config

# Python dependencies
pip install nltk polyglot PyICU pycld2 morfessor numpy six
```

### Solution 2: Polyglot Downloader Patch (Advanced)

**File**: `polyglot_downloader_patch.py`

**Purpose**: Patches the polyglot library to add User-Agent headers to HTTP requests

**Usage**:
```bash
python3 polyglot_downloader_patch.py
```

**What it does**:
- Locates the installed polyglot library
- Adds User-Agent header to urllib requests
- Helps bypass some server restrictions

**Note**: Even with this patch, polyglot's morpheme download may still fail because:
- The polyglot resource server (polyglot.readthedocs.io) has access restrictions
- The project is no longer actively maintained
- Server infrastructure may be unreliable

### Solution 3: NLTK-Only Alternative (Best for Production)

**File**: `3_1_wordsteam_nltk_only.py`

**Advantages**:
- ✅ Works reliably without external server dependencies
- ✅ Uses only NLTK library (well-maintained and stable)
- ✅ Demonstrates multiple stemming algorithms
- ✅ Provides comparison between different stemmers
- ✅ No complex dependency installation required

**Features**:
- Porter Stemmer (original algorithm from the book)
- Lancaster Stemmer (more aggressive)
- Snowball Stemmer (improved Porter algorithm)
- Side-by-side comparison of all three stemmers

**Dependencies**:
```bash
pip install nltk
```

**Usage**:
```bash
python3 3_1_wordsteam_nltk_only.py
```

## Detailed Error Analysis

### Root Cause

The error occurs at:
```
File "polyglot/downloader.py", line 831, in _update_index
    data = urlopen(index_url).read()
urllib.error.HTTPError: HTTP Error 403: Forbidden
```

**Why it happens**:
1. Polyglot tries to auto-download morpheme models from remote servers
2. The server (polyglot.readthedocs.io) returns HTTP 403 Forbidden
3. This happens because:
   - The server blocks requests without proper User-Agent headers
   - The polyglot infrastructure is deprecated and may have access restrictions
   - The project hasn't been updated since 2016

### Why Polyglot is Problematic

1. **Deprecated**: Last updated in 2016 (version 16.7.4)
2. **Complex Dependencies**: Requires PyICU, pycld2, morfessor, and system libraries
3. **Server Issues**: Resource download servers are unreliable
4. **Python 3 Compatibility**: Has various compatibility issues with modern Python

## Recommendations

### For Learning (Following the Book)

1. Use `3_1_wordsteam_nltk_only.py` - it demonstrates the same concepts without polyglot issues
2. The NLTK stemmers provide the same educational value
3. You'll learn about multiple stemming algorithms instead of just one

### For Production Code

1. **Use spaCy**: Modern, well-maintained, excellent morphological analysis
   ```bash
   pip install spacy
   python -m spacy download en_core_web_sm
   ```

2. **Use stanza**: Stanford NLP's modern Python library
   ```bash
   pip install stanza
   ```

3. **Use NLTK**: Reliable for basic stemming and lemmatization
   ```bash
   pip install nltk
   ```

## Installation Guide

### Quick Start (NLTK-Only Solution)

```bash
# Install NLTK
pip install nltk

# Run the alternative script
python3 3_1_wordsteam_nltk_only.py
```

### Full Installation (If you want to try polyglot)

```bash
# System dependencies (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install -y libicu-dev pkg-config

# Python dependencies
pip install nltk polyglot PyICU pycld2 morfessor numpy six

# Apply the patch
python3 polyglot_downloader_patch.py

# Run the fixed script
python3 3_1_wordsteam.py
```

**Warning**: Even with all dependencies installed and the patch applied, polyglot's morpheme functionality may still fail due to server issues.

## Comparison of Outputs

### Original Script (with polyglot working)
```
Derivational Morphemes
happi
unkind

Derivational Morphemes using polyglot library
happiness           ['happiness']
unkind              ['un', 'kind']
```

### NLTK-Only Alternative
```
Derivational Morphemes (Porter Stemmer)
happi
unkind

Lancaster Stemmer (More Aggressive)
happiness           happy
unkind              unkind

Snowball Stemmer (Improved Porter)
happiness           happi
unkind              unkind
```

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'icu'"
**Solution**: Install PyICU
```bash
sudo apt-get install libicu-dev pkg-config
pip install PyICU
```

### Error: "HTTP Error 403: Forbidden"
**Solutions**:
1. Use the NLTK-only alternative script (recommended)
2. Apply the polyglot_downloader_patch.py (may not fully resolve)
3. Switch to modern alternatives (spaCy, stanza)

### Error: "SyntaxError: invalid syntax" on print statements
**Solution**: The script has been updated to Python 3 syntax. Make sure you're using the updated version.

## Additional Resources

- [NLTK Documentation](https://www.nltk.org/)
- [spaCy Documentation](https://spacy.io/)
- [Stanza Documentation](https://stanfordnlp.github.io/stanza/)
- [Polyglot GitHub Issues](https://github.com/aboSamoor/polyglot/issues) - See known issues

## Summary

The polyglot library issue is a known problem affecting many users. The best solution is to use the NLTK-only alternative (`3_1_wordsteam_nltk_only.py`) which provides the same educational value without the dependency and server issues. For production code, consider using modern alternatives like spaCy or stanza.
