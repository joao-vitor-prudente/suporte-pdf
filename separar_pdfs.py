from typing import Callable
from pathlib import Path
from logging import error
from PyPDF2 import PdfFileWriter, PdfFileReader


def main(func: Callable) -> Callable:
    def wrapper():
        while True:
            caminho = Path(rf'{input("Digite o diretorio de input: ")}')
            func(caminho)

    return wrapper


@main
def split_pdf(caminho: Path):
    pdfs: list = [
        pdf for pdf in caminho.iterdir()
        if pdf.is_file() and not pdf.name.startswith('.') and not pdf.name.startswith('~$')
    ]

    for pdf in pdfs:
        try:
            (caminho / pdf.stem).mkdir()

            with open(str(pdf), "rb") as f:
                inputpdf = PdfFileReader(f)

                for i in range(inputpdf.numPages):
                    output = PdfFileWriter()
                    output.addPage(inputpdf.getPage(i))
                    caminho / pdf.stem
                    with open(str(caminho / pdf.stem / Path(f'{i}.pdf')), "wb") as outputStream:
                        output.write(outputStream)

        except Exception as e:
            error(f'\n>> [ERRO]: {e}\n Relativo ao arquivo: {str(pdf)}\n')


if __name__ == '__main__':
    split_pdf()
