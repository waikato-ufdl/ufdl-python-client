from typing import List, Iterator, Union, IO

from ..._UFDLServerContext import UFDLServerContext

# ========================= #
# SegmentationLayersViewSet #
# ========================= #


def get_layer(
        context: UFDLServerContext,
        url: str,
        pk: int,
        filename: str,
        label: str
) -> Iterator[bytes]:
    return context.download(
        f"{url}/{pk}/layers/{filename}/{label}"
    ).iter_content(chunk_size=None)


def set_layer(
        context: UFDLServerContext,
        url: str,
        pk: int,
        filename: str,
        label: str,
        mask: Union[bytes, IO[bytes]]
) -> str:
    return context.upload(
        f"{url}/{pk}/layers/{filename}/{label}",
        filename,
        mask
    ).json()


def get_labels(
        context: UFDLServerContext,
        url: str,
        pk: int
) -> List[str]:
    return context.get(
        f"{url}/{pk}/labels"
    ).json()


def set_labels(
        context: UFDLServerContext,
        url: str,
        pk: int,
        labels: List[str]
) -> List[str]:
    return context.post(
        f"{url}/{pk}/labels",
        {
            "labels": labels
        }
    ).json()
