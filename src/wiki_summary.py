!pip install wikipedia
import wikipedia
import random
import warnings
# to cleanly suppress a BeautifulSoup internal warning that happens inside the wikipedia package.
warnings.filterwarnings("ignore", category=UserWarning, module='wikipedia')
# Set language to English
wikipedia.set_lang("en")

# Number of articles to fetch
ARTICLE_COUNT = 3

# File to store summary history
history_file = "history.txt"

print("📚 Fetching random Wikipedia articles...\n")

for i in range(ARTICLE_COUNT):
    random_topic = random.choice(wikipedia.random(pages=10))

    try:
        summary = wikipedia.summary(random_topic, sentences=3)

        # Display
        print(f"📘 {i+1}. Random Article: {random_topic}")
        print(f"📝 Summary:\n{summary}\n")

        # Save to file
        with open(history_file, "a", encoding="utf-8") as f:
            f.write(f"\n=== {random_topic} ===\n{summary}\n")

    except wikipedia.exceptions.DisambiguationError as e:
        print(f"⚠️ Disambiguation error for topic: {random_topic}")
        print(f"Suggested options: {e.options[:5]}\n")

    except wikipedia.exceptions.PageError:
        print(f"❌ Page not found: {random_topic}\n")

print(f"✅ Done! Summaries saved to {history_file}")
