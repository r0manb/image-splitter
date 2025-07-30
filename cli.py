import argparse


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("fp", type=str, help="Путь к изображению")
    parser.add_argument("w", type=int, help="Ширина под-изображения")
    parser.add_argument("h", type=int, help="Высота под-изображения")
    parser.add_argument(
        "-sp",
        "--save_path",
        type=str,
        default="",
        help="Путь к папке для сохранения",
    )
    parser.add_argument(
        "-ext", "--extension", type=str, help="Расширение под-изображения"
    )

    return parser.parse_args()
