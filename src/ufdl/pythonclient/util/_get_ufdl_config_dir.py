import os

from wai.common.config import get_config_dir


def get_ufdl_config_dir() -> str:
    """
    Gets the directory in which to store app configuration.

    :return:    The directory string.
    """
    # Get the system app configuration standard location
    config_dir = get_config_dir()

    # Define a folder for our configuration in the standard location
    ufdl_config_dir = os.path.join(config_dir, 'ufdl')

    # Make sure the location exists
    if not os.path.exists(ufdl_config_dir):
        os.makedirs(ufdl_config_dir, exist_ok=True)

    return ufdl_config_dir
