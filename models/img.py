import os
from PIL import Image


class Img:
    __fp: str
    __image: Image.Image
    __ext: str

    def __init__(self, fp: str) -> None:
        self.__fp = fp

        self.__init_image()
        self.__init_ext()

    def __init_image(self) -> None:
        with Image.open(self.__fp) as img:
            self.__image = img.copy()
            self.__image.format = img.format

    def __init_ext(self) -> None:
        base = os.path.basename(self.__fp)
        _, ext = os.path.splitext(base)
        self.__ext = ext[1:] if ext else ""

    @property
    def path(self) -> str:
        return self.__fp

    @property
    def image(self) -> Image.Image:
        return self.__image

    @property
    def extension(self) -> str:
        return self.__ext
