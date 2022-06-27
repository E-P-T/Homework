

from typing import Optional

from rss_reader.interfaces.idataconverter.idataconverter import IDataConverter


class DataConverter(IDataConverter):

    def concat_data(self, data, local_data) -> Optional[DataFrame]:
        pass
