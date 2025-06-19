"""Political slogan detector

Detects common political slogans or calls to action in text by matching
against a list of known phrases."""

from garak import _config
from garak.data import path as data_path
from garak.detectors.base import StringDetector


class SloganDetector(StringDetector):
    """Detect political slogans and calls to action"""

    lang_spec = "*"
    doc_uri = ""
    tags = ["quality:Behavioral:ContentSafety:Political"]
    DEFAULT_PARAMS = StringDetector.DEFAULT_PARAMS | {"matchtype": "word"}

    def __init__(self, config_root=_config):
        with open(
            data_path / "political" / "slogans.txt",
            "r",
            encoding="utf-8",
        ) as f:
            slogans = [line.strip() for line in f if line.strip()]
        super().__init__(slogans, config_root=config_root)
