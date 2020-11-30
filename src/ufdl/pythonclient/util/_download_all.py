from io import BytesIO
from typing import Iterator


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
    for chunk in iterator:
        buffer.write(chunk)

    # Reset the buffer's cursor to the beginning
    buffer.seek(0)

    # Return the contents of the buffer
    return buffer.read()
