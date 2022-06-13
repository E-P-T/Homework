import json
import bs4


class RSS:
    def __init__(self, feed):
        self.__get_title(feed)

    def __get_title(self, feed):
        self.title = feed.title.string

    def to_json(self):
        return json.dumps(self, default=lambda x: x.__dict__, indent=4, ensure_ascii=False)


class RssFeed(RSS):
    def __init__(self, feed, limit):
        super().__init__(feed)
        self.items = [RssFeedItem(item) for item in feed.findAll("item", limit=limit)]

    def __str__(self):
        if not self.items:
            return "NO DATA"
        result = f"\nFeed: {self.title}\n"
        for item in self.items:
            result += str(item)
        return result


class RssFeedItem(RSS):
    def __init__(self, item):
        if isinstance(item, dict):
            for key in item.keys():
                setattr(self, key, item[key])
        else:
            super().__init__(item)
            self.__parse_item(item)

    def __parse_item(self, item):
        self.date = item.pubdate.string
        self.link = item.link.next_sibling.strip()
        self.urls = []
        self.images = []
        self.__parse_description(item)

    def __parse_description(self, item):
        """
        Takes an BeautifulSoup object and clean up it for self-description

        :param item: BeautifulSoup object
        :return None:
        """
        if not item.description:
            self.description = "Empty"
        else:
            replaceable_tags_list = ["img", "figure", "a"]
            temp_description = bs4.BeautifulSoup(item.description.text.strip(), "html.parser")
            for tag in replaceable_tags_list:
                while temp_description.find(tag):
                    curr_elem = temp_description.find(tag)
                    if tag == replaceable_tags_list[0]:
                        self.images.append(curr_elem["src"])
                        curr_elem.replace_with(f"[Image_{len(self.images)}]")
                    elif tag == replaceable_tags_list[1]:
                        curr_elem.unwrap()
                    elif tag == replaceable_tags_list[2]:
                        self.urls.append(curr_elem["href"])
                        curr_elem.replace_with(f"[Link_{len(self.urls)}]{curr_elem.text}[]")
            self.description = temp_description.text.replace("\xa0", " ")

    def __str__(self):
        """
        Returns a string representation of RssItem object

        :return result: str
        """
        result = f"\nTitle: {self.title}\n" \
                 f"Date: {self.date}\n" \
                 f"Link: {self.link}\n" \
                 f"Description: {self.description}\n"
        if self.urls:
            result += "Links:\n"
            for index, url in enumerate(self.urls):
                result += f"[{index + 1}]\t{url}\n"

        if self.images:
            result += "Images:\n"
            for index, url in enumerate(self.images):
                result += f"[{index + 1}]\t{url}\n"

        return result
