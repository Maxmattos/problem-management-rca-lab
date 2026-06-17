"""Material do aluno não pode conter gabarito (DoD / §9).

Os notebooks dos três encontros são entregues ao aluno SEM resposta pronta: o
gabarito mora exclusivamente nos guias do instrutor (docs/0X_guia_instrutor.md).
Este teste trava isso como invariante.
"""

from pathlib import Path

import nbformat
import pytest

NB_DIR = Path(__file__).resolve().parents[1] / "notebooks"

# Marcadores que denunciam um gabarito embutido no material do aluno.
MARCADORES = ["gabarito", "answer key"]


@pytest.mark.parametrize("nb_path", sorted(NB_DIR.glob("*.ipynb")), ids=lambda p: p.name)
def test_notebook_aluno_sem_gabarito(nb_path):
    nb = nbformat.read(nb_path, as_version=4)
    ofensas = []
    for i, cell in enumerate(nb.cells):
        texto = (cell.source or "").lower()
        for marcador in MARCADORES:
            if marcador in texto:
                ofensas.append(f"célula {i}: contém '{marcador}'")
    assert not ofensas, f"{nb_path.name} parece conter gabarito:\n" + "\n".join(ofensas)
