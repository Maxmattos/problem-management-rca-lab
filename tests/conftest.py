"""Fixtures de teste: dados regenerados do zero + determinismo (H1 / §8.1)."""

import importlib.util
from pathlib import Path

import pandas as pd
import pytest

REPO = Path(__file__).resolve().parents[1]


def _carregar_gerador():
    spec = importlib.util.spec_from_file_location(
        "gerar_ocorrencias", REPO / "data" / "gerar_ocorrencias.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="session")
def df_fresh() -> pd.DataFrame:
    """Dados regenerados do zero com seed fixo. Os invariantes rodam aqui (§9)."""
    return _carregar_gerador().gerar(seed=42)


def test_geracao_deterministica():
    """gerar(42) duas vezes produz DataFrames idênticos (função pura, ADR-01)."""
    gen = _carregar_gerador()
    pd.testing.assert_frame_equal(gen.gerar(seed=42), gen.gerar(seed=42))


def test_csv_comitado_bate_com_regeracao():
    """O CSV comitado é exatamente o que `gerar(42)` produz (§8.1, checagem de hash).

    Mantenha o CSV sempre regenerado (`make data`) antes de commitar; as versões
    fixadas em requirements*.txt estabilizam a serialização de float.
    """
    gen = _carregar_gerador()
    csv = REPO / "data" / "ocorrencias.csv"
    do_disco = pd.read_csv(csv, parse_dates=["aberto_em", "resolvido_em"])
    regerado = gen.gerar(seed=42)
    pd.testing.assert_frame_equal(
        do_disco.reset_index(drop=True),
        regerado.reset_index(drop=True),
        check_dtype=False,  # CSV round-trip pode reabrir datas/inteiros com dtype distinto
    )
