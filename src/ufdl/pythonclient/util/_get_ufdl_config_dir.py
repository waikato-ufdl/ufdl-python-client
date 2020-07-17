import os


def get_ufdl_config_dir() -> str:
    """
    Gets the directory in which to store app configuration. Based on
    code from https://stackoverflow.com/a/3250952.

    On Windows, %APPDATA%\\ufdl\
    On Linux, $XDG_CONFIG_HOME/ufdl/

    If the relevant environment variable for the platform is not set,
    defaults to ~/.config/ufdl/

    :return:    The directory string.
    """
    # Get the system app configuration standard location
    config_dir = os.environ['APPDATA'] if 'APPDATA' in os.environ \
        else os.environ['XDG_CONFIG_HOME'] if 'XDG_CONFIG_HOME' in os.environ \
        else os.path.join(os.environ['HOME'], '.config')

    # Define a folder for our configuration in the standard location
    ufdl_config_dir = os.path.join(config_dir, 'ufdl')

    # Make sure the location exists
    if not os.path.exists(ufdl_config_dir):
        os.mkdir(ufdl_config_dir)

    return ufdl_config_dir
