"""Checagem de anonimato (H4 / §8.4).

ADR-04: a denylist NUNCA entra no repo. Vem de RCA_DENYLIST (CSV inline) ou
RCA_DENYLIST_FILE (caminho). Sem nenhuma das duas, o teste faz skip com mensagem
clara; o CI injeta via secret RCA_DENYLIST.
"""

import os
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
EXT_TEXTO = {".py", ".md", ".ipynb", ".txt", ".toml", ".cfg", ".yml", ".yaml", ".csv"}
IGNORAR = {".git", "__pycache__", ".pytest_cache", ".ipynb_checkpoints", ".venv"}


def _denylist():
    nomes = [n.strip() for n in os.environ.get("RCA_DENYLIST", "").split(",") if n.strip()]
    arq = os.environ.get("RCA_DENYLIST_FILE")
    if arq and Path(arq).exists():
        nomes += [
            ln.strip() for ln in Path(arq).read_text(encoding="utf-8").splitlines() if ln.strip()
        ]
    return nomes


def test_anonimato():
    nomes = _denylist()
    if not nomes:
        pytest.skip("Sem denylist (RCA_DENYLIST/RCA_DENYLIST_FILE). CI injeta via secret.")
    achados = []
    for p in REPO.rglob("*"):
        if any(parte in IGNORAR for parte in p.parts):
            continue
        if not p.is_file() or p.suffix.lower() not in EXT_TEXTO or p.name == "test_anonymity.py":
            continue
        texto = p.read_text(encoding="utf-8", errors="ignore").lower()
        for nome in nomes:
            if nome.lower() in texto:
                achados.append(f"{p.relative_to(REPO)}: nome proibido encontrado")
    assert not achados, "Anonimato violado:\n" + "\n".join(sorted(set(achados)))
