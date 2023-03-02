import feedparser


def handle_rss(link):
    feed = feedparser.parse(link)
    entries = []
    for entry in feed.entries:
        entry_dict = {}
        entry_dict["title"] = entry.title
        entry_dict["link"] = entry.link
        entry_dict["date"] = entry.published_parsed
        entry_dict["content"] = getattr(entry, "content", entry.summary)
        entries.append(entry_dict)
    return {"entries": entries}


# def handle_youtube(link):
#     return entries

# def handle_twitch(link):
#     return entries
