import feedparser
import time
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

default_date = time.strptime("1970-01-01", "%Y-%m-%d")


def handle_feed(tag, url):
    if url.endswith(".xml"):
        return handle_rss(tag, url)
    elif url.startswith("https://www.youtube.com/"):
        return handle_youtube(tag, url)
    elif url.startswith("https://www.twitch.tv/"):
        # return handle_twitch(tag, feed_url)
        pass
    else:
        print(f"Not sure what kind of feed {url} is, skipping...")


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


def handle_youtube(tag, base_url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")
    channel_id = soup.find("meta", {"itemprop": "channelId"})["content"]
    feed_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"

    feed = feedparser.parse(feed_url)
    entries = []
    for entry in feed.entries:
        date = time.strftime("%Y-%m-%d", entry.get("published_parsed", default_date))
        entry_dict = {}
        entry_dict["base_url"] = base_url
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


def handle_twitch(tag, base_url):
    # print(f"{feed_url} is a twitch feed")
    # return {"entries": entries}
    pass


# Fix later
# Atom content tags work differently than rss content tags
# Make another handler for atom feeds or handle it on the frontends
