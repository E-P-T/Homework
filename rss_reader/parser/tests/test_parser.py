

import pytest
from collections.abc import Generator


from ..parser import BeautifulParser
from ..exceptions import EmptyListError


class MockTags:

    @property
    def text(self):
        return ['mock_1_text', 'mock_2_text']
