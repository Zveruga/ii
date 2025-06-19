from garak import _plugins
from garak.attempt import Attempt


def test_slogan_detector_hit():
    d = _plugins.load_plugin("detectors.political.SloganDetector")
    a = Attempt(prompt="test")
    a.outputs = ["Power to the people!"]
    assert d.detect(a) == [1.0]


def test_slogan_detector_miss():
    d = _plugins.load_plugin("detectors.political.SloganDetector")
    a = Attempt(prompt="test")
    a.outputs = ["This is a regular sentence."]
    assert d.detect(a) == [0.0]
