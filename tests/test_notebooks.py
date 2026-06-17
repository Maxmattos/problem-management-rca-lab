"""Execução automatizada dos notebooks (H3 / §8.3).

Cada notebook é reexecutado do zero e a contagem de PNGs embutidos é travada como
invariante (ADR-06). Os PNGs Plotly são renderizados via kaleido (Chromium embutido).
"""

from pathlib import Path

import nbformat
import pytest
from nbclient import NotebookClient

NB_DIR = Path(__file__).resolve().parents[1] / "notebooks"

# ADR-06: contagem real de PNGs por notebook, travada como invariante.
PNG_ESPERADO = {
    "01_aluno_sinal_vs_ruido.ipynb": 5,
    "02_aluno_registro_e_rca.ipynb": 4,
    "03_aluno_validar_comunicar.ipynb": 3,
}


@pytest.mark.parametrize("nome", sorted(PNG_ESPERADO))
def test_notebook_executa_e_embute_imagens(nome):
    nb = nbformat.read(NB_DIR / nome, as_version=4)
    # cwd = notebooks/ para resolver "../data/ocorrencias.csv"
    NotebookClient(
        nb,
        timeout=300,
        kernel_name="python3",
        resources={"metadata": {"path": str(NB_DIR)}},
    ).execute()
    pngs = sum(
        1
        for cell in nb.cells
        for out in cell.get("outputs", [])
        if "image/png" in out.get("data", {})
    )
    assert pngs == PNG_ESPERADO[nome], f"{nome}: {pngs} PNGs, esperado {PNG_ESPERADO[nome]}"
