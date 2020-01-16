def detail_url(base_url: str, object_pk: int) -> str:
    """
    Combines a base model URL with the primary key of a
    particular instance of the model into an instance-
    specific URL.

    :param base_url:    The base URL of the model.
    :param object_pk:   The primary key of the instance.
    :return:            The instance-specific URL.
    """
    return base_url + str(object_pk) + "/"