import pytest
from beetsstatistics import BeetsStatistics


@pytest.fixture
def beets_statistics():
    return BeetsStatistics("test.db")


def test_map_format_to_lossy_lossless_lossless(beets_statistics: BeetsStatistics):
    formats = [
        ("mp3", 1),
        ("mp3", 1),
        ("mp3", 1),
        ("ogg", 1),
        ("flac", 1),
        ("wav", 1),
        ("hurz", 1),
    ]
    lossless, _, _ = beets_statistics.map_file_format_to_lossy(formats)
    assert lossless == 2


def test_map_format_to_lossy_lossless_lossy(beets_statistics: BeetsStatistics):
    formats = [
        ("mp3", 1),
        ("mp3", 1),
        ("mp3", 1),
        ("ogg", 1),
        ("flac", 1),
        ("wav", 1),
        ("hurz", 1),
    ]
    _, lossy, _ = beets_statistics.map_file_format_to_lossy(formats)
    assert lossy


def test_map_format_to_lossy_lossless_unknown(beets_statistics: BeetsStatistics):
    formats = [
        ("mp3", 1),
        ("mp3", 1),
        ("mp3", 1),
        ("ogg", 1),
        ("flac", 1),
        ("wav", 1),
        ("hurz", 1),
    ]
    _, _, unknown = beets_statistics.map_file_format_to_lossy(formats)
    assert unknown == 1
