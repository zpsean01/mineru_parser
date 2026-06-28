import json
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def _load_token() -> str:
    config_path = Path(__file__).resolve().parent.parent / "config.json"
    if config_path.exists():
        try:
            with open(config_path) as f:
                data = json.load(f)
                if data.get("token"):
                    return data["token"]
        except Exception:
            pass
    return os.getenv("MINERU_TOKEN", "")


class Config:
    TOKEN: str = _load_token()
    BASE_URL: str = os.getenv("MINERU_BASE_URL", "https://mineru.net")
    POLL_INTERVAL: int = int(os.getenv("MINERU_POLL_INTERVAL", "5"))
    POLL_TIMEOUT: int = int(os.getenv("MINERU_POLL_TIMEOUT", "1800"))
    DATA_DIR: Path = Path(os.getenv("MINERU_DATA_DIR", "./data"))

    @classmethod
    def validate(cls):
        if not cls.TOKEN:
            raise ValueError(
                "Token 未设置！请在 config.json 或 .env 中配置你的 Token。"
            )
