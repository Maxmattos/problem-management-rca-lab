"""Invariantes pedagógicos dos dados (H2 / §8.2).

ADR-02: estes thresholds são fonte de verdade. Se um invariante falhar com o seed
atual, ajusta-se a DISTRIBUIÇÃO do gerador até passar com margem -- o teste fica fixo.
"""

import pandas as pd

COLUNAS = [
    "ocorrencia_id",
    "aberto_em",
    "resolvido_em",
    "maquina",
    "produto",
    "tipo_defeito",
    "gravidade",
    "turno",
    "descricao",
    "tempo_resolucao_h",
]


def test_schema(df_fresh):
    df = df_fresh
    assert list(df.columns) == COLUNAS
    assert df[COLUNAS].notna().all().all(), "nulos em colunas-chave"
    assert pd.api.types.is_datetime64_any_dtype(df["aberto_em"])
    assert pd.api.types.is_datetime64_any_dtype(df["resolvido_em"])
    assert (df["resolvido_em"] >= df["aberto_em"]).all()
    assert set(df["gravidade"]) <= {"Crítico", "Alto", "Médio", "Baixo"}
    assert set(df["turno"]) <= {"Manhã", "Tarde", "Noite"}
    # ids sequenciais e cronológicos
    assert list(df["ocorrencia_id"]) == [f"OC{i:05d}" for i in range(1, len(df) + 1)]
    assert df["aberto_em"].is_monotonic_increasing


def test_pareto_serra02_lider_isolado(df_fresh):
    c = df_fresh["maquina"].value_counts()
    assert c.index[0] == "Serra-02", "Serra-02 deve liderar o Pareto"
    assert c.iloc[0] >= 2 * c.iloc[1], "líder deve ter >= 2x o segundo"


def test_serra02_tendencia_crescente(df_fresh):
    s = df_fresh[df_fresh["maquina"] == "Serra-02"].copy()
    inicio = s["aberto_em"].min().normalize()
    s["semana"] = (s["aberto_em"] - inicio).dt.days // 7
    por_semana = s.groupby("semana").size()
    n = int(por_semana.index.max())
    primeiras4 = por_semana.reindex(range(0, 4), fill_value=0).mean()
    ultimas4 = por_semana.reindex(range(n - 3, n + 1), fill_value=0).mean()
    assert ultimas4 >= 1.3 * primeiras4, "tendência crescente >= 30%"


def test_serra02_vies_noturno(df_fresh):
    s = df_fresh[df_fresh["maquina"] == "Serra-02"]
    frac = (s["turno"] == "Noite").mean()
    assert 0.45 <= frac <= 0.65, f"viés noturno fora da faixa: {frac:.2f}"


def test_coladeira_problema_sutil(df_fresh):
    c = df_fresh[df_fresh["maquina"] == "Coladeira-01"]
    assert 8 <= len(c) <= 20, "volume baixo da Coladeira-01"
    cola = c[c["descricao"].str.contains("colagem", case=False, na=False)]
    assert len(cola) >= 6, "recorrência da assinatura idêntica"
    span = (cola["aberto_em"].max() - cola["aberto_em"].min()).days
    assert span >= 60, "recorrência espaçada ao longo do período"


def test_distrator_incendio_evento_unico(df_fresh):
    inc = df_fresh[df_fresh["descricao"].str.contains("Incêndio no painel", case=False, na=False)]
    assert len(inc) == 1, "incêndio deve ser evento único"
    assert inc.iloc[0]["gravidade"] == "Crítico"
