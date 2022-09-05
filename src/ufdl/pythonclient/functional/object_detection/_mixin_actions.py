from typing import List, Optional, Union

from ufdl.json.object_detection import ImageAnnotation, VideoAnnotation, AnnotationsFile

from wai.json.raw import RawJSONObject, RawJSONArray

from ..._UFDLServerContext import UFDLServerContext

# ================== #
# AnnotationsViewSet #
# ================== #


def get_labels(
        context: UFDLServerContext,
        url: str,
        pk: int
) -> List[str]:
    return context.get(
        f"{url}/{pk}/labels"
    ).json()


def add_labels(
        context: UFDLServerContext,
        url: str,
        pk: int,
        *labels: str
):
    context.post(
        f"{url}/{pk}/labels",
        labels
    )


def delete_label(
        context: UFDLServerContext,
        url: str,
        pk: int,
        label: str
):
    context.delete(
        f"{url}/{pk}/labels/{label}"
    )


def get_prefixes(
        context: UFDLServerContext,
        url: str,
        pk: int
) -> List[str]:
    return context.get(
        f"{url}/{pk}/prefixes"
    ).json()


def add_prefixes(
        context: UFDLServerContext,
        url: str,
        pk: int,
        *prefixes: str
):
    context.post(
        f"{url}/{pk}/prefixes",
        prefixes
    )


def delete_prefix(
        context: UFDLServerContext,
        url: str,
        pk: int,
        prefix: str
):
    context.delete(
        f"{url}/{pk}/prefixes/{prefix}"
    )


def get_file_type(
        context: UFDLServerContext,
        url: str,
        pk: int,
        filename: str
) -> RawJSONObject:
    return context.get(
        f"{url}/{pk}/file-type/{filename}"
    ).json()


def set_file_type(
        context: UFDLServerContext,
        url: str,
        pk: int,
        filename: str,
        format: str,
        width: int,
        height: int,
        length: Optional[float]
):
    body = {
        "format": format,
        "dimensions": [width, height]
    }

    if length is not None:
        body['length'] = length

    context.post(
        f"{url}/{pk}/file-type/{filename}",
        body
    )


def get_file_types(
        context: UFDLServerContext,
        url: str,
        pk: int
) -> RawJSONObject:
    return context.get(
        f"{url}/{pk}/file-types"
    ).json()


def get_annotations(
        context: UFDLServerContext,
        url: str,
        pk: int
) -> RawJSONObject:
    return context.get(
        f"{url}/{pk}/annotations"
    ).json()


def set_annotations(
        context: UFDLServerContext,
        url: str,
        pk: int,
        annotations: AnnotationsFile
):
    context.post(
        f"{url}/{pk}/annotations",
        annotations.to_raw_json()
    )


def clear_annotations(
        context: UFDLServerContext,
        url: str,
        pk: int
):
    context.delete(
        f"{url}/{pk}/annotations"
    )


def get_annotations_for_file(
        context: UFDLServerContext,
        url: str,
        pk: int,
        filename: str
) -> RawJSONArray:
    return context.get(
        f"{url}/{pk}/annotations/{filename}"
    ).json()


def set_annotations_for_file(
        context: UFDLServerContext,
        url: str,
        pk: int,
        filename: str,
        annotations: Union[List[ImageAnnotation], List[VideoAnnotation]]
):
    raw_annotations = [
        annotation.to_raw_json()
        for annotation in annotations
    ]
    context.post(
        f"{url}/{pk}/annotations/{filename}",
        raw_annotations
    )


def add_annotations_to_file(
        context: UFDLServerContext,
        url: str,
        pk: int,
        filename: str,
        annotations: Union[List[ImageAnnotation], List[VideoAnnotation]]
):
    raw_annotations = [
        annotation.to_raw_json()
        for annotation in annotations
    ]
    context.patch(
        f"{url}/{pk}/annotations/{filename}",
        raw_annotations
    )


def delete_annotations_for_file(
        context: UFDLServerContext,
        url: str,
        pk: int,
        filename: str
):
    context.delete(
        f"{url}/{pk}/annotations/{filename}"
    )
