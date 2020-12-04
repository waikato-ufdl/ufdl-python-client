from io import BytesIO
from typing import Iterator, IO


def download_all(iterator: Iterator[bytes]) -> bytes:
    """
    Downloads an entire data-stream into a bytes object.

    :param iterator:
                The iterator of chunks from the data-stream.
    :return:
                The concatenated contents of the stream.
    """
    # Create a buffer for the data
    buffer = BytesIO()

    # Consume each chunk of data
    download_all_into(iterator, buffer)

    # Reset the buffer's cursor to the beginning
    buffer.seek(0)

    # Return the contents of the buffer
    return buffer.read()


def download_all_into(iterator: Iterator[bytes], into: IO[bytes]):
    """
    Downloads the entire stream into a given file-like object.

    :param iterator:
                The iterator of chunks from the data-stream.
    :param into:
                The file-like object to write the data-stream into.
    """
    assert into.writable(), "File-like object 'into' must be writable"

    for chunk in iterator:
        into.write(chunk)
