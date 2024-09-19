import pytest
from beetsstatistics import BeetsStatistics


@pytest.fixture
def beets_statistics():
    return BeetsStatistics("test.db")


def test_map_format_to_lossy_lossless_lossless(beets_statistics: BeetsStatistics):
    formats = [
        ("mp3", 5),
        ("ogg", 3),
        ("flac", 7),
        ("wav", 11),
        ("hurz", 2),
    ]
    lossless, _, _ = beets_statistics.map_file_format_to_lossy(formats)
    assert lossless == 18


def test_map_format_to_lossy_lossless_lossy(beets_statistics: BeetsStatistics):
    formats = [
        ("mp3", 5),
        ("ogg", 3),
        ("flac", 7),
        ("wav", 11),
        ("hurz", 2),
    ]
    _, lossy, _ = beets_statistics.map_file_format_to_lossy(formats)
    assert lossy == 8


def test_map_format_to_lossy_lossless_unknown(beets_statistics: BeetsStatistics):
    formats = [
        ("mp3", 5),
        ("ogg", 3),
        ("flac", 7),
        ("wav", 11),
        ("hurz", 2),
    ]
    _, _, unknown = beets_statistics.map_file_format_to_lossy(formats)
    assert unknown == 2
