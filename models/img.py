from __future__ import annotations
from pathlib import Path
from typing import final, Optional, Union
from PIL import Image


@final
class Img:
    __image: Image.Image
    __fp: Optional[Path]
    name: str
    __ext: Optional[str]

    @classmethod
    def from_image(cls, image: Image.Image, name: str = "") -> Img:
        return cls(image, name=name)

    @classmethod
    def from_file(cls, fp: Union[Path, str]) -> Img:
        fp = Path(fp) if isinstance(fp, str) else fp
        image = cls.__open_and_prepare_image(fp)

        return cls(image, fp=fp, name=fp.name)

    def __init__(
        self, image: Image.Image, name: str = "", fp: Optional[Path] = None
    ) -> None:
        self.__image = image
        self.__fp = fp
        self.name = name

        self.__init_ext()

    @staticmethod
    def __open_and_prepare_image(fp: Path) -> Image.Image:
        with Image.open(fp) as img:
            if img.mode != "RGB":
                image = img.convert("RGB")
            else:
                image = img.copy()
            image.format = img.format

        return image

    def __init_ext(self) -> None:
        if self.__fp:
            ext = self.__fp.suffix
            self.__ext = ext[1:] if ext else ""
            return

        if self.__image.format is None:
            self.__ext = None
            return

        self.__ext = str(self.__image.format).lower()

    @property
    def image(self) -> Image.Image:
        return self.__image

    @property
    def extension(self) -> Optional[str]:
        return self.__ext
