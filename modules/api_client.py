from typing import Optional
import requests

from modules.config import Config


class MineruClient:
    def __init__(self, token: Optional[str] = None):
        self.token = token or Config.TOKEN
        if not self.token:
            raise ValueError("MinerU Token 不能为空，请在 .env 中配置 MINERU_TOKEN")
        self.base_url = Config.BASE_URL
        self._session: Optional[requests.Session] = None

    @property
    def session(self) -> requests.Session:
        if self._session is None:
            self._session = requests.Session()
            self._session.headers.update({
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            })
        return self._session

    def _request(self, method: str, path: str, **kwargs) -> dict:
        url = f"{self.base_url}{path}"
        resp = self.session.request(method, url, **kwargs)
        resp.raise_for_status()
        body = resp.json()
        if body.get("code") != 0:
            raise RuntimeError(
                f"API 请求失败 [code={body.get('code')}]: {body.get('msg', 'unknown error')}"
            )
        return body["data"]
