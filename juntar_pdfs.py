from typing import Callable
from pdfrw import PdfReader, PdfWriter
from pathlib import Path
from logging import error


def main(func: Callable) -> Callable:
    def wrapper():
        while True:
            caminho = Path(rf'{input("Digite o diretorio de input: ")}')
            func(caminho)

    return wrapper


@main
def join_pdf(caminho: Path):
    writer: PdfWriter = PdfWriter()

    pdfs: list = [
        pdf for pdf in caminho.iterdir()
        if pdf.is_file() and not pdf.name.startswith('.') and not pdf.name.startswith('~$')
    ]

    for pdf in pdfs:
        try:
            writer.addpages(PdfReader(str(pdf)).pages)
        except Exception as e:
            error(f'\n>> [ERRO]: {e}\n Relativo ao arquivo: {str(pdf)}\n')
    writer.write(str(caminho) + '.pdf')


if __name__ == '__main__':
    join_pdf()
