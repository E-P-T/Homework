"""This module contains a class that works with data stored in local storage."""

from locale import normalize
from typing import List, Optional
from pandas import DataFrame, json_normalize, concat, to_datetime

from rss_reader.interfaces.idataconverter.idataconverter import IDataConverter


class DataConverter(IDataConverter):

    def concat_data(self, data: List[dict],
                    local_data: DataFrame,
                    ignore_index: bool) -> Optional[DataFrame]:
        """Concat two DataFrames.

        :param data: Data to be merged with data from local storage.
        :type data: List[dict]
        :param local_data: DataFrame which is obtained from local storage.
        :type local_data: DataFrame
        :param ignore_index: Returns True when the argument x is true,
        False otherwise. The builtins True and False are the only two
        instances of the class bool. The class bool is a subclass of the
        class int, and cannot be subclassed.
        :type ignore_index: bool
        :return: Merged DataFrame.
        :rtype: Optional[DataFrame]
        """

        data_concat = concat([local_data, data],
                             ignore_index=ignore_index)
        return data_concat

    def drop_duplicates_(self, data: DataFrame,
                         keep: str = "first",
                         ignore_index: bool = False) -> Optional[DataFrame]:
        """Return DataFrame with duplicate rows removed.

        :param data: The DataFrame in which duplicates should be removed.
        :type data: DataFrame
        :param keep: {'first', 'last', False}, default 'first'
            Determines which duplicates (if any) to keep.
            - ``first`` : Drop duplicates except for the first occurrence.
            - ``last`` : Drop duplicates except for the last occurrence.
            - False : Drop all duplicates.
        :type keep: str
        :param inplace: bool, default False
            Whether to drop duplicates in place or to return a copy.
        :type inplace: bool
        :param ignore_index: bool, default False
            If True, the resulting axis will be labeled 0, 1, …, n - 1.
        :type ignore_index: bool
        :return: DataFrame without duplicates.
        :rtype: Optional[DataFrame]
        """
        return data.drop_duplicates(keep=keep,
                                    ignore_index=ignore_index)

    def normalize_(self, data: List[dict], record_path: List[str],
                   meta: List[str], record_prefix: str) -> DataFrame:
        """Normalize semi-structured JSON data into a flat table.

        :param data: Data for normalize.
        :type data: List[dict]
        :param record_path: Path in each object to list of records. If not
        passed, data will be assumed to be an array of records.
        :type record_path: List[str]
        :param meta: Fields to use as metadata for each record in resulting
        table.
        :type meta: List[str]
        :param record_prefix: If True, prefix records with dotted (?) path,
        e.g. foo.bar.field if
        path to records is ['foo', 'bar'].
        :type record_prefix: str
        :return: Normalize semi-structured JSON data into a flat table.
        :rtype: DataFrame
        """
        return json_normalize(data, record_path=record_path,
                              meta=meta,
                              record_prefix=record_prefix)

    def convert_date(self, df: DataFrame, column_name:
                     str, format: str = '%Y-%m-%d',
                     utc: bool = True) -> DataFrame:
        """Convert the date to the desired format.

        :param df: The DataFrame in which to replace.
        :type df: DataFrame
        :param column_name: The name of the column in which you want to change.
        :type column_name: str
        :param format: Return a string representing the date, controlled by an
        explicit format string. Format codes referring to hours, minutes or
        seconds will see 0 values., defaults to '%Y-%m-%d'
        :type format: str, optional
        :param utc: Control timezone-related parsing, localization and
        conversion.

        If True, the function always returns a timezone-aware UTC-localized
        Timestamp, Series or DatetimeIndex. To do this, timezone-naive inputs
        are localized as UTC, while timezone-aware inputs are converted to UTC.

        If False (default), inputs will not be coerced to UTC. Timezone-naive
        inputs will remain naive, while timezone-aware ones will keep their
        time offsets. Limitations exist for mixed offsets (typically, daylight
        savings), see Examples section for details., defaults to True

        :type utc: bool
        :return: DataFrame with the converted date.
        :rtype: DataFrame
        """

        df[column_name] = to_datetime(df.get(column_name), utc=utc)
        df[column_name] = df.get(column_name).dt.date.apply(
            lambda x: x.strftime(format))
        return df
