"""
Core package for the UFDL client library. Provides the ability to set
the communication context (host/port to communicate with) and functions
for performing the communication.
"""
from ._context import set_context, get_host, get_port
from ._methods import get, post, put, patch, delete, upload, download
