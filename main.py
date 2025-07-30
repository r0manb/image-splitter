from models.img import Img
from utils import image_utils

from cli import parse_args


def main():
    args = parse_args()

    img = Img(args.fp)
    image_utils.split_image_and_save(
        img, (args.w, args.h), args.save_path, args.extension
    )


if __name__ == "__main__":
    main()
