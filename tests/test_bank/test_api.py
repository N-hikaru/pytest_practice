import pytest
import requests
from unittest.mock import patch
from pytest_lazyfixture import lazy_fixture

from api import Api


@pytest.fixture
def fetch_api():
    """Lambdaを返すことで、テスト関数内で初めて `Api.fetch_data()` を実行(with patch内で実行)
    例外処理を起こしたいパターンもあるため、遅延評価したい
    """
    return lambda: Api.fetch_data()

@pytest.mark.parametrize("api", [lazy_fixture("fetch_api")])
def test_api_success(api):
    res = api()
    assert res["userId"] == 1, "userIdが違います"

@pytest.mark.parametrize("api", [lazy_fixture("fetch_api")])
def test_api_ConnectionError(api):
    """ネットワークエラー (ConnectionError) を発生させる"""
    with patch("requests.get", side_effect=requests.exceptions.ConnectionError("ネットワーク障害")):
        result = api()
        assert result is requests.exceptions.ConnectionError

@pytest.mark.parametrize("api", [lazy_fixture("fetch_api")])
def test_api_RequestException(api):
    """その他のエラー (RequestException) を発生させる(requests のすべてのエラーを捕まえる)"""
    with patch("requests.get", side_effect=requests.exceptions.RequestException("requestsのすべてのエラー")):
        result = api()
        assert result is requests.exceptions.RequestException


@pytest.fixture
def result_api_mock_response_success():
    response = requests.models.Response()
    response.status_code = 200
    response._content = b'{\n  "userId": 1,\n  "id": 1,\n  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",\n  "body": "quia et suscipit\\nsuscipit recusandae consequuntur expedita et cum\\nreprehenderit molestiae ut ut quas totam\\nnostrum rerum est autem sunt rem eveniet architecto"\n}'
    response.raise_for_status = lambda: None
    return response

def test_fetch_data_with_id_change_100_success(result_api_mock_response_success):
    with patch("requests.get") as mock_get:
        mock_get.return_value = result_api_mock_response_success
        result = Api.fetch_data_with_id_change(100)
        assert result["id"] == 100

def test_fetch_data_with_id_change_200_success(result_api_mock_response_success):
    with patch("requests.get") as mock_get:
        mock_get.return_value = result_api_mock_response_success
        result = Api.fetch_data_with_id_change(200)
        assert result["id"] == 200

# TODO: Api.fetch_data_with_id_change()の例外処理での失敗パターンも書く
# @pytest.fixture
# def result_api_mock_response_connectionError():
#     """
#     requests.exceptions.ConnectionError は response の属性として取得できません！
#     requests.get() が ConnectionError を発生させた場合、response オブジェクトは生成されず、直接 ConnectionError の例外が発生 します
#     """
#     return requests.exceptions.ConnectionError