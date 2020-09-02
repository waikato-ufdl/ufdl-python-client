from typing import List

from ufdl.json.object_detection import Annotation

from wai.json.raw import RawJSONObject

from ..._UFDLServerContext import UFDLServerContext

# ================== #
# AnnotationsViewSet #
# ================== #


def get_annotations(context: UFDLServerContext, url: str, pk: int) -> RawJSONObject:
    return context.get(f"{url}/{pk}/annotations").json()


def get_annotations_for_image(context: UFDLServerContext, url: str, pk: int, image: str) -> RawJSONObject:
    return context.get(f"{url}/{pk}/annotations/{image}").json()


def set_annotations_for_image(context: UFDLServerContext, url: str, pk: int, image: str, annotations: List[Annotation]):
    raw_annotations = [annotation.to_raw_json() for annotation in annotations]
    context.post(f"{url}/{pk}/annotations/{image}", {"annotations": raw_annotations})


def delete_annotations_for_image(context: UFDLServerContext, url: str, pk: int, image: str):
    context.delete(f"{url}/{pk}/annotations/{image}")
