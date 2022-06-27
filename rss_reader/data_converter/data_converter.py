

from typing import Optional
from pandas import DataFrame

from rss_reader.interfaces.idataconverter.idataconverter import IDataConverter


class DataConverter(IDataConverter):

    def concat_data(self, data, local_data) -> Optional[DataFrame]:
        norm_data = json_normalize(data, record_path=['items'],
                                   meta=['title_web_resource', 'link'],
                                   record_prefix="item.")

        norm_data = self._convert_date(norm_data, 'item.pubDate')
