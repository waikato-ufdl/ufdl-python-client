from typing import List

from ufdl.json.object_detection import Annotation

from wai.json.raw import RawJSONObject

from ...core import get, post, delete
from .._util import detail_url

# ================== #
# AnnotationsViewSet #
# ================== #


def get_annotations(url: str, pk: int) -> RawJSONObject:
    return get(detail_url(url, pk) + "annotations").json()


def get_annotations_for_image(url: str, pk: int, image: str) -> RawJSONObject:
    return get(detail_url(url, pk) + f"annotations/{image}").json()


def set_annotations_for_image(url: str, pk: int, image: str, annotations: List[Annotation]):
    raw_annotations = [annotation.to_raw_json() for annotation in annotations]
    post(detail_url(url, pk) + f"annotations/{image}", {"annotations": raw_annotations})


def delete_annotations_for_image(url: str, pk: int, image: str):
    delete(detail_url(url, pk) + f"annotations/{image}")
