from __future__ import annotations
from typing import List, Optional, Tuple, TYPE_CHECKING
import os

from models.img import Img

if TYPE_CHECKING:
    from PIL import Image


def split_image_and_save(
    img: Img,
    subimage_size: Tuple[int, int],
    save_path: str = "",
    ext: Optional[str] = None,
    skip_partial: bool = False,
) -> None:
    if not ext:
        ext = img.extension

    if save_path and not os.path.exists(save_path):
        os.makedirs(save_path, exist_ok=True)

    images = split_image(img.image, subimage_size, skip_partial)
    for sub_img in images:
        sub_img.image.save(f"{save_path}/{sub_img.name}.{ext}")


def split_image(
    img: Image.Image, subimage_size: Tuple[int, int], skip_partial: bool = False
) -> List[Img]:
    images: List[Img] = []
    w, h = img.size
    sub_w, sub_h = subimage_size

    for y1 in range(0, h, sub_h):
        curr_row = y1 // sub_h
        for x1 in range(0, w, sub_w):
            x2 = min(x1 + sub_w, w)
            y2 = min(y1 + sub_h, h)

            if skip_partial and (x2 - x1 < sub_w or y2 - y1 < sub_h):
                continue

            sub_img = img.crop((x1, y1, x2, y2))
            sub_img = Img.from_image(sub_img, f"{curr_row}_{x1//sub_w}")
            images.append(sub_img)

    return images
