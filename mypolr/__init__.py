import requests

DEFAULT_API_KEY = '0652a12da6eed57acba65898252fef'


class UrlShorter:
    def __init__(self, api_server='https://7z.fi', api_key=DEFAULT_API_KEY, api_root='/api/v2/', ):
        """

        :param api_server:
        :type api_server: str
        :param api_root:
        :type api_root: str
        :param api_key:
        :type api_key: str
        """
        self.api_root = api_server + api_root
        self.api_shorten_endpoint = self.api_root + 'action/shorten'
        self.api_lookup_endpoint = self.api_root + 'action/lookup'
        self.api_link_data_endpoint = self.api_root + 'data/link'
        self.api_key = api_key
        self._base_header = {
            'key': self.api_key,
            'response_type': 'json'
        }

    def get_shorturl(self, long_url, custom=None, is_secret=False):
        """

        :param long_url:
        :type long_url: str
        :param custom:
        :type custom: str
        :param is_secret:
        :type is_secret: bool
        :return:
        :rtype: str
        """
        params = {
            **self._base_header,
            'url': long_url,
            'is_secret': is_secret,
            'custom_encoding': custom
        }
        try:
            r = requests.get(self.api_shorten_endpoint, params)
            data = r.json()
            if data.get('action') == 'shorten' and data.get('result') is not None:
                return data.get('result')
        except ValueError:
            pass
        except requests.ConnectionError:
            pass
        finally:
            return None