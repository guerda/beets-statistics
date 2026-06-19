from pydantic_settings import BaseSettings


class BeetsStatisticsSettings(BaseSettings):
    """
    This settings object reads out all members via environment variables, if they are not specified in the constructor.

    musiclibrary_db is a string defining the location of the beets library.
    log_level can be set to "debug" if you want debug output.
    """

    musiclibrary_db: str
    log_level: str
    media_path: str
