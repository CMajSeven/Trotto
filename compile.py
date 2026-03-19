from pathlib import Path
import os
import sys
import traceback

from pypdf import PdfWriter
from pypdf.constants import PageLabelStyle


def wrap(f):
    def wrapped(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except BaseException as e:
            traceback.print_stack(file=sys.stderr)
            print(f"\033[91m{e}\033[0m", file=sys.stderr)
    return wrapped


@wrap
def writeFullScore():
    writer = PdfWriter()
    writer.append("01 - Full score - Trotto.pdf")
    writer.append("01 - Mensural - Trotto.pdf")
    writer.add_outline_item("Cover", 0)
    writer.add_outline_item("Full Score", 2)
    writer.set_page_layout("/TwoPageRight")
    writer.set_page_label(0, 0, prefix="Cover")
    writer.set_page_label(2, 3, style=PageLabelStyle.DECIMAL)
    writer.write("Trotto.pdf")

@wrap
def setPageLayout(filename: str, rightLayout: bool):
    writer = PdfWriter(Path(filename))
    writer.set_page_layout("/TwoPageRight" if rightLayout else "/TwoPageLeft")
    writer.write(filename)


def main():
    print("Processing Full Score")
    writeFullScore()


if __name__ == "__main__":
    main()
