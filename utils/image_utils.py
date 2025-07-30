from __future__ import annotations
from typing import List, Optional, Tuple, TYPE_CHECKING
import os

if TYPE_CHECKING:
    from models.img import Img

    from PIL import Image


def split_image_and_save(
    img: Img,
    subimage_size: Tuple[int, int],
    save_path: str = "",
    ext: Optional[str] = None,
) -> None:
    if not ext:
        ext = img.extension

    if save_path and not os.path.exists(save_path):
        os.makedirs(save_path, exist_ok=True)

    images = split_image(img.image, subimage_size)
    for i, sub_img in enumerate(images):
        sub_img.save(f"{save_path}/{i}.{ext}")


def split_image(img: Image.Image, subimage_size: Tuple[int, int]) -> List[Image.Image]:
    images = []
    w, h = img.size
    sub_w, sub_h = subimage_size

    for y1 in range(0, h, sub_h):
        for x1 in range(0, w, sub_w):
            x2 = min(x1 + sub_w, w)
            y2 = min(y1 + sub_h, h)

            sub_img = img.crop((x1, y1, x2, y2))
            images.append(sub_img)

    return images
