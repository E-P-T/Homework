

from typing import Optional
from pandas import DataFrame, json_normalize, concat

from rss_reader.interfaces.idataconverter.idataconverter import IDataConverter


class DataConverter(IDataConverter):

    def concat_data(self, data, local_data) -> Optional[DataFrame]:
        norm_data = json_normalize(data, record_path=['items'],
                                   meta=['title_web_resource', 'link'],
                                   record_prefix="item.")

        norm_data = self._convert_date(norm_data, 'item.pubDate')
        data_concat = concat([local_data, norm_data],
                             ignore_index=True)
        data_concat.drop_duplicates(keep='first', inplace=True,
                                    ignore_index=True)

    def _convert_date(self, df: DataFrame, column_name:
                      str, format: str = '%Y-%m-%d',
                      utc: bool = True) -> DataFrame:
        df[column_name] = to_datetime(df.get(column_name), utc=utc)
        df[column_name] = df.get(column_name).dt.date.apply(
            lambda x: x.strftime(format))
