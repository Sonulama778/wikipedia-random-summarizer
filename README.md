## Project Title: Wikipedia Random Article Summarizer

### Overview:
This Python project fetches and summarizes random Wikipedia articles using the `wikipedia` Python package. It demonstrates the use of web-based data retrieval, error handling, and file writing in Python. Summaries are saved to a local history file, and the project is structured to be extended easily into a web app or GUI application.

### Folder Structure:
```
Wikipedia-Random-Summary/
- data/
   └── history.txt
- src/
   └── wiki_summary.py
- README.md
- requirements.txt

```

### README.md
```markdown
# Wikipedia Random Article Summarizer

This Python project fetches and summarizes random Wikipedia articles using the `wikipedia` library. It displays a summary of 3 random topics each time it's run and saves the output in a local file for history tracking.

## Features
- Fetches 3 random Wikipedia articles per run
- Displays a 3-sentence summary for each topic
- Handles disambiguation and missing page errors gracefully
- Saves results to a local file (`history.txt`)
- Easily extendable for custom topic search, web apps, or GUI

## How It Works
- Uses `wikipedia.random()` to get article titles
- Uses `wikipedia.summary()` to retrieve clean summaries
- Handles exceptions like `DisambiguationError` and `PageError`

## Technologies
- Python 3
- [wikipedia](https://pypi.org/project/wikipedia/)

## Getting Started
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python src/wiki_summary.py
   ```

## Output Example
```
📘 1. Random Article: Danny Dereck Prince
📝 Summary:
Danny Dereck Prince (born 14 March 1986) is an Indian cricketer...

📘 2. Random Article: Wake Island
⚠️ Disambiguation error for topic: Wake Island
Suggested options: ['Wake Island (film)', ...]
```

## Optional Enhancements
- Add CLI flag to fetch specific topic
- Convert to GUI with Tkinter or web app using Streamlit
- Schedule to run daily and email summary

## License
MIT
```

### requirements.txt
```
wikipedia
```

### wiki_summary.py (in src/)
```python
import wikipedia
import random
import warnings

# Suppress parser warnings
warnings.filterwarnings("ignore", category=UserWarning, module='wikipedia')

wikipedia.set_lang("en")
ARTICLE_COUNT = 3
history_file = "../data/history.txt"

print("📚 Fetching random Wikipedia articles...\n")

for i in range(ARTICLE_COUNT):
    random_topic = random.choice(wikipedia.random(pages=10))

    try:
        summary = wikipedia.summary(random_topic, sentences=3)

        print(f"📘 {i+1}. Random Article: {random_topic}")
        print(f"📝 Summary:\n{summary}\n")

        with open(history_file, "a", encoding="utf-8") as f:
            f.write(f"\n=== {random_topic} ===\n{summary}\n")

    except wikipedia.exceptions.DisambiguationError as e:
        print(f"⚠️ Disambiguation error for topic: {random_topic}")
        print(f"Suggested options: {e.options[:5]}\n")

    except wikipedia.exceptions.PageError:
        print(f"❌ Page not found: {random_topic}\n")

print(f"✅ Done! Summaries saved to {history_file}")
```
