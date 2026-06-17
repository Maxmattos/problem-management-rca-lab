"""
Gerador sintético de ocorrências para uma fábrica de móveis planejados.

Produz um log realista de 90 dias para treinar Problem Management: distinguir
incidentes isolados de problemas de verdade (tendência, recorrência, Pareto) e
conduzir análise de causa-raiz (RCA) sobre a evidência.

Três padrões são plantados de propósito para que o dataset tenha uma "resposta certa":

  1. PROBLEMA PRINCIPAL  -> máquina `Serra-02`, defeito `corte-fora-medida`.
     O volume cresce semana a semana (TENDÊNCIA sustentada de subida) e domina o
     Pareto. Além disso concentra-se no turno da NOITE (~55%) -- pista de método/
     treino/iluminação no terceiro turno. É o candidato óbvio a problema.

  2. PROBLEMA SUTIL      -> máquina `Coladeira-01`, defeito `falha-colagem`.
     Volume baixo, mas REINCIDE em cadência regular com a mesma assinatura
     ("Falha de colagem na fita de borda"). O Pareto não o destaca; só a
     recorrência o denuncia.

  3. DISTRATOR (NÃO é problema) -> um único "Incêndio no painel elétrico" (Crítico).
     Severidade máxima, assustador, mas acontece UMA vez e nunca se repete.
     Severidade alta NÃO transforma um evento em problema.

Todo o resto é ruído de fundo: ocorrências avulsas espalhadas pelo chão de fábrica.

Uso:   python gerar_ocorrencias.py
Saída: ocorrencias.csv  (uma linha por ocorrência)

ADR-01: `gerar()` é função pura -- mesmo seed produz o mesmo DataFrame, e os
invariantes pedagógicos (tests/) rodam sobre dados regenerados do zero, não só
sobre o CSV comitado.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

# --- Janela da simulação -----------------------------------------------------
INICIO = pd.Timestamp("2025-03-01")

# Máquinas do parque fabril (corte -> furação -> colagem -> acabamento -> embalagem).
MAQUINAS = [
    "Serra-01",
    "Serra-02",  # problema principal
    "Seccionadora-01",
    "Furadeira-01",
    "Coladeira-01",  # problema sutil
    "Coladeira-02",
    "Lixadeira-01",
    "Prensa-01",
    "CNC-01",
    "Embaladora-01",
]

PRODUTOS = [
    "Guarda-roupa",
    "Cômoda",
    "Mesa de jantar",
    "Estante",
    "Cabeceira",
    "Painel de TV",
    "Gaveteiro",
    "Criado-mudo",
]

TURNOS = ["Manhã", "Tarde", "Noite"]

# Biblioteca de assinaturas (tipo_defeito, descricao) por máquina.
# A mesma (máquina, descricao) repetida é o que torna a recorrência detectável.
ASSINATURAS = {
    "Serra-01": [
        ("corte-fora-esquadro", "Corte fora de esquadro no painel"),
        ("parada-nao-programada", "Parada não programada do disco de corte"),
    ],
    "Serra-02": [
        ("corte-fora-medida", "Corte fora de medida na Serra-02"),  # assinatura principal
    ],
    "Seccionadora-01": [
        ("corte-fora-medida", "Divergência de medida no plano de corte"),
        ("lascamento", "Lascamento na borda do painel"),
    ],
    "Furadeira-01": [
        ("furo-descentralizado", "Furo descentralizado no painel"),
        ("broca-quebrada", "Quebra de broca durante a furação"),
    ],
    "Coladeira-01": [
        ("falha-colagem", "Falha de colagem na fita de borda"),  # assinatura sutil
    ],
    "Coladeira-02": [
        ("bolha-fita", "Bolhas na fita de borda"),
        ("cola-temperatura", "Cola fora da temperatura de trabalho"),
    ],
    "Lixadeira-01": [
        ("acabamento-irregular", "Acabamento irregular na superfície"),
        ("lixa-desgastada", "Lixa desgastada antes do previsto"),
    ],
    "Prensa-01": [
        ("delaminacao", "Delaminação do painel prensado"),
        ("pressao-fora-padrao", "Pressão fora do padrão na prensagem"),
    ],
    "CNC-01": [
        ("erro-programa", "Erro de programa no usinado CNC"),
        ("desgaste-ferramenta", "Desgaste de ferramenta no usinado"),
    ],
    "Embaladora-01": [
        ("falha-embalagem", "Falha no filme de embalagem"),
        ("etiqueta-ilegivel", "Etiqueta ilegível na expedição"),
    ],
}

GRAVIDADES = ["Crítico", "Alto", "Médio", "Baixo"]

# Tempo mediano de resolução (horas) por gravidade -> dá realismo ao MTTR.
TRH_MEDIANA = {"Crítico": 4.0, "Alto": 8.0, "Médio": 24.0, "Baixo": 72.0}


def gerar(seed: int = 42, n_dias: int = 90) -> pd.DataFrame:
    """Gera o log de ocorrências de forma determinística.

    Função pura: `gerar(42)` sempre retorna um DataFrame idêntico. Toda a
    aleatoriedade vem do `rng` local, então chamadas repetidas não acumulam
    estado (ADR-01).
    """
    rng = np.random.default_rng(seed)
    linhas: list[dict] = []
    contador = {"n": 0}

    def ts(dia_baixo: int, dia_alto: int) -> pd.Timestamp:
        """Timestamp uniforme dentro de uma janela de dias (operação 24x7)."""
        dia = int(rng.integers(dia_baixo, dia_alto))
        segundos = int(rng.integers(0, 24 * 3600))
        return INICIO + pd.Timedelta(days=dia, seconds=segundos)

    def resolucao(aberto: pd.Timestamp, gravidade: str) -> pd.Timestamp:
        """Tempo de resolução lognormal ancorado na mediana da gravidade."""
        mediana = TRH_MEDIANA[gravidade]
        horas = float(rng.lognormal(mean=np.log(mediana), sigma=0.6))
        horas = max(0.25, horas)
        return aberto + pd.Timedelta(hours=horas)

    def add(maquina, tipo_defeito, descricao, gravidade, aberto, turno=None, produto=None):
        contador["n"] += 1
        turno = turno or str(rng.choice(TURNOS))
        produto = produto or str(rng.choice(PRODUTOS))
        aberto = pd.Timestamp(aberto)
        linhas.append(
            {
                "ocorrencia_id": f"OC{contador['n']:05d}",
                "aberto_em": aberto,
                "resolvido_em": resolucao(aberto, gravidade),
                "maquina": maquina,
                "produto": produto,
                "tipo_defeito": tipo_defeito,
                "gravidade": gravidade,
                "turno": turno,
                "descricao": descricao,
            }
        )

    # --- 1) PROBLEMA PRINCIPAL: Serra-02, tendência crescente + viés noturno ---
    # Contagem semanal sobe de ~3/sem para ~12/sem ao longo da janela.
    # Turno enviesado para a Noite (~55%) -- a pista de causa-raiz do Encontro 2.
    for semana in range(n_dias // 7 + 1):
        base = 3 + semana * 0.75  # rampa de subida
        n = int(rng.poisson(base))
        for _ in range(n):
            dia = min(n_dias - 1, semana * 7 + int(rng.integers(0, 7)))
            gravidade = str(rng.choice(["Alto", "Médio", "Médio", "Baixo"]))
            turno = str(rng.choice(TURNOS, p=[0.25, 0.25, 0.50]))  # viés noturno (~55%)
            add(
                "Serra-02",
                "corte-fora-medida",
                "Corte fora de medida na Serra-02",
                gravidade,
                ts(dia, dia + 1),
                turno=turno,
            )

    # --- 2) PROBLEMA SUTIL: Coladeira-01 reincide ~semanalmente, volume baixo ---
    # Mesma assinatura, cadência regular, nunca em alto volume.
    dia = 4
    while dia < n_dias:
        add(
            "Coladeira-01",
            "falha-colagem",
            "Falha de colagem na fita de borda",
            str(rng.choice(["Alto", "Médio"])),
            ts(dia, dia + 1),
        )
        dia += int(rng.integers(6, 9))  # cadência ~semanal

    # --- 3) DISTRATOR: um único incêndio, severíssimo, isolado ------------------
    add(
        "Prensa-01",
        "incendio",
        "Incêndio no painel elétrico",
        "Crítico",
        ts(40, 41),
    )

    # --- 4) RUÍDO DE FUNDO: ocorrências avulsas pelo resto do parque ------------
    # Exclui as máquinas plantadas para que suas contagens reflitam só os padrões.
    maquinas_ruido = [m for m in MAQUINAS if m not in ("Serra-02", "Coladeira-01")]
    n_ruido = 230
    for _ in range(n_ruido):
        maq = str(rng.choice(maquinas_ruido))
        assinaturas = ASSINATURAS[maq]
        tipo_defeito, descricao = assinaturas[int(rng.integers(0, len(assinaturas)))]
        gravidade = str(rng.choice(GRAVIDADES, p=[0.03, 0.20, 0.50, 0.27]))
        add(maq, tipo_defeito, descricao, gravidade, ts(0, n_dias))

    # --- Montagem final ---------------------------------------------------------
    df = pd.DataFrame(linhas)
    df = df.sort_values("aberto_em").reset_index(drop=True)
    # Reatribui ids em ordem cronológica para o log se ler naturalmente.
    df["ocorrencia_id"] = [f"OC{i:05d}" for i in range(1, len(df) + 1)]
    df["tempo_resolucao_h"] = (
        (df["resolvido_em"] - df["aberto_em"]).dt.total_seconds() / 3600
    ).round(2)
    # Ordem de colunas estável (invariante de schema).
    df = df[
        [
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
    ]
    return df


if __name__ == "__main__":
    from pathlib import Path

    df = gerar()
    out = Path(__file__).resolve().parent / "ocorrencias.csv"
    df.to_csv(out, index=False)
    print(f"gerado: {out} ({len(df)} linhas)")
    print(f"janela: {df['aberto_em'].min()} .. {df['aberto_em'].max()}")
    print("\nMáquinas por volume:")
    print(df["maquina"].value_counts().head(6).to_string())
