from requests import Response, HTTPError


def raise_for_response(response: Response) -> Response:
    """
    Calls raise_for_status on the given response object, or returns the
    same object if it doesn't raise.

    :param response:    The response object.
    :return:            The same response object.
    """
    # Call raise for status
    try:
        response.raise_for_status()
    except HTTPError as e:
        # Attach the detail message to the error if there is one
        e.detail = response.content.decode()
        raise

    return response
