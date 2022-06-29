from rss_parse.preprocessor.rss_preprocessor import RssSortPreprocessor, RssCachePreprocessor, RssLimitPreprocessor
from rss_parse.utils.messaging_utils import MESSAGE_CONSUMER_NOOP


def get_preprocessors(params, mc=MESSAGE_CONSUMER_NOOP):
    """
    Fetch correct implementation of RssPreprocessor based on input parameters
    """
    preprocessors = [RssSortPreprocessor(mc)]
    if not params.pub_date:
        preprocessors.append(RssCachePreprocessor(mc))
    if params.limit:
        preprocessors.append(RssLimitPreprocessor(params.limit, mc))
    return preprocessors
