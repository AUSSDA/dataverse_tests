import json
import os

import pytest

from ..conftest import INSTANCE
from ..conftest import ROOT_DIR


with open(
    os.path.join(
        ROOT_DIR,
        "src/dvtests/testing/data",
        INSTANCE,
        "default/unit/testdata_oaipmh.json",
    )
) as json_file:
    testdata = json.load(json_file)


class TestEndpoint:
    @pytest.mark.v4_18_1
    @pytest.mark.v4_20
    @pytest.mark.parametrize("test_input,expected", testdata["endpoint"]["valid"])
    def test_valid(self, session, test_input, expected):
        """Test OAI-PMH endpoints."""
        # Arrange
        # Act
        resp = session.get(test_input["url"])

        # Assert
        assert resp.text
        assert resp.url == test_input["url"]
        assert resp.status_code == 200
        assert resp.encoding == expected["encoding"]
        assert resp.headers["Content-Type"] == expected["content-type"]
        # Cleanup
