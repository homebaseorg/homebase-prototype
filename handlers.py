import feedparser
import time
from urllib.parse import urlparse

default_date = time.strptime("1970-01-01", "%Y-%m-%d")


def handle_feed(tag, feed_url):
    if feed_url.endswith(".xml"):
        return handle_rss(tag, feed_url)
    elif feed_url.startswith("https://www.youtube.com/"):
        # return handle_youtube(tag, feed_url)
        pass
    elif feed_url.startswith("https://www.twitch.tv/"):
        # return handle_twitch(tag, feed_url)
        pass
    else:
        print(f"Not sure what kind of feed {feed_url} is, skipping...")


def handle_rss(tag, feed_url):
    feed = feedparser.parse(feed_url)
    entries = []
    for entry in feed.entries:
        date = time.strftime("%Y-%m-%d", entry.get("published_parsed", default_date))
        entry_dict = {}
        entry_dict["base_url"] = urlparse(entry.link).netloc
        entry_dict["feed_url"] = feed_url
        entry_dict["title"] = entry.get("title", "No title")
        entry_dict["author"] = entry.get("author", "No author")
        entry_dict["date"] = date
        entry_dict["link"] = entry.link
        entry_dict["tag"] = tag
        entry_dict["content"] = getattr(
            entry, "content", entry.get("summary", "No summary")
        )
        entry_dict["language"] = tag
        entry_dict["unread"] = 1
        entry_dict["rtl"] = 0
        entries.append(entry_dict)
    return entries


def handle_youtube(tag, feed_url):
    # print(f"{feed_url} is a youtube feed")
    # return {"entries": entries}
    pass


def handle_twitch(tag, feed_url):
    # print(f"{feed_url} is a twitch feed")
    # return {"entries": entries}
    pass


# Fix later
# Atom content tags work differently than rss content tags
# Make another handler for atom feeds or handle it on the frontends
