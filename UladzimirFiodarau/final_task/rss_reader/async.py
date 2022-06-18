import asyncio
import aiohttp
import platform
import json
import base64
import tqdm


class AsyncImageCacher:
    """
    Class is used to download images from urls for later caching.
    For faster computing and better user experience getting URL data is made in async mode.
    """
    def __init__(self, news_dict):
        """
        Method is used for saving the news dictionary that is going to be updated and a list of URLs to download from

        :param news_dict: news dictionary
        """
        self.news_dict = news_dict
        self.image_urls = AsyncImageCacher.find_urls(self.news_dict)

    @staticmethod
    def find_urls(news_dict):
        """
        Method is used to parse a dictionary of standard known structure and getting a list of URLs from it

        :param news_dict: news dictionary
        :return: a list of found URLs
        """
        found_urls = []
        if 'feed_media' in news_dict:
            if 'type' not in news_dict['feed_media'] or news_dict['feed_media']['type'].startswith('image'):
                found_urls.append(news_dict['feed_media']['url'])
        for item in news_dict['feed_items']:
            if 'media' in news_dict["feed_items"][item] and 'url' in news_dict["feed_items"][item]['media']:
                media = news_dict["feed_items"][item]['media']
                if 'type' not in media or media['type'].startswith('image'):
                    found_urls.append(media['url'])
        return found_urls

    @staticmethod
    async def get_image(url):
        """
        Method is used for async requesting URL and downloading image from it. Image is returned in tuple with URL, that
        it was downloaded from, in form of base64 encoded string  (for later processing).
        Read buffer size is set approximately to 4 Mb in case of heavy weighted image files.

        :param url: image URL
        :return: tuple (image URL, encoded image data) if download successful,  None if request fails
        """
        try:
            async with aiohttp.ClientSession(read_bufsize=2 ** 22) as session:
                async with session.get(url=url, read_bufsize=2 ** 22) as response:
                    resp = await response.read()
        except Exception as e:
            print(f"Unable to get url {url} due to {e.__class__} {e}.")
        else:
            return url, base64.b64encode(resp).decode('utf-8')

    @staticmethod
    async def get_all_images(urls):
        """
        Method is used to combine all async requests of URLs into a dictionary URL: encoded image data while also
        discarding failed requests results. Uses tqdm to show user progress bar of async processes

        :param urls:
        :return:
        """
        print('Getting images for cache. This may take some time, please wait.\n Download progress:')
        getlist = [(AsyncImageCacher.get_image(url)) for url in urls]
        returns = [await f for f in tqdm.tqdm(asyncio.as_completed(getlist), total=len(getlist))]
        print(f"Finished downloading image(s)")
        image_dict = {}
        for tup in returns:
            if isinstance(tup, tuple):
                image_dict[tup[0]] = tup[1]
        return image_dict

    @staticmethod
    def update_dict(news, media_dict):
        """
        Method updates given news dictionary with known structure with requested image data
        :param news: news dictionary
        :param media_dict: dictionary with requested image data
        :return: news dictionary with requested image data
        """
        if 'feed_media' in news:
            if 'type' not in news['feed_media'] or news['feed_media']['type'].startswith('image'):
                if news['feed_media']['url'] in media_dict:
                    news['feed_media']['contains'] = media_dict[news['feed_media']['url']]
        for item in news['feed_items']:
            if 'media' in news["feed_items"][item] and 'url' in news["feed_items"][item]['media']:
                media = news["feed_items"][item]['media']
                if 'type' not in media or media['type'].startswith('image'):
                    if media['url'] in media_dict:
                        media['contains'] = media_dict[media['url']]
        return news

    def run(self):
        """
        Method combines other methods of AsyncImageCacher class into a single script
        :return:
        """
        if platform.system() == "Windows":
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        media_dict = asyncio.run(AsyncImageCacher.get_all_images(self.image_urls))
        new_dict = AsyncImageCacher.update_dict(self.news_dict, media_dict)
        return new_dict


if __name__ == '__main__':
    with open('rss_json_test.json', 'r') as rss_cache:
        dictionary = json.load(rss_cache)
    AsyncImageCacher(dictionary).run()


# from PIL import Image
# from io import BytesIO
# for i in media_dict.values():
#     name = str(random.randint(1, 500))
#     im = Image.open(BytesIO(base64.b64decode(i)))
#     rgb_im = im.convert('RGB')
#     rgb_im.save('temp/image' + name + '.jpg', 'JPEG')
