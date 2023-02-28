import feedparser


def handle_rss(link):
    feed = feedparser.parse(link)
    entries = []
    for entry in feed.entries:
        entry_dict = {}
        entry_dict["title"] = entry.title
        entry_dict["link"] = entry.link
        entry_dict["summary"] = entry.summary
        entries.append(entry_dict)
    return {"entries": entries}


# def handle_youtube(link):
#     return title, content

# def handle_twitch(link):
#     return title, content
