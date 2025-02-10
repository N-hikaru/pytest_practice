import traceback
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

class Api:

    def fetch_data():
        """API からデータを取得する関数"""
        try:
            response = requests.get(url, timeout=5)
            print(response)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.ConnectionError as e:
            print(f"API エラー: {e}")
            return type(e)
        # requests のすべてのエラーを捕まえる
        except requests.exceptions.RequestException as e:
            print(f"API エラー: {e}")
            return type(e)
        
    def fetch_data_with_id_change(id):
        try:
            response = requests.get(url, timeout=5) # モック化
            response.raise_for_status()
            res = response.json()
            res["id"] = id
            return res
        except requests.exceptions.ConnectionError as e:
            print(f"API エラー: {e}")
            return type(e)
        # requests のすべてのエラーを捕まえる
        except requests.exceptions.RequestException as e:
            print(f"API エラー: {e}")
            return type(e)
    

# if __name__ == "__main__":
#     # res = Api.fetch_data()
#     res = Api.fetch_data_with_id_change(100)
#     print(res)