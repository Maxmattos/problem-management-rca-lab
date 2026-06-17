# ADRs — decisões de design do harness

Registro curto das decisões tomadas ao implementar o harness e o conteúdo. Uma decisão
por seção.

## ADR-00 — Cenário e idioma: fábrica de móveis, em português

O laboratório foi (re)construído no cenário **fábrica de móveis planejados**, com todo o
conteúdo de ensino e os dados em **português**; o `README.md` permanece em **inglês**. Uma
variante anterior em inglês (plataforma de pagamentos) foi substituída. A estrutura
pedagógica (3 padrões plantados, 4 lentes, 3 encontros) é idêntica entre cenários — muda só
o vocabulário.

## ADR-01 — Gerador como função pura

`data/gerar_ocorrencias.py` expõe `gerar(seed=42, n_dias=90) -> DataFrame`; o bloco
`__main__` grava `ocorrencias.csv`. Toda a aleatoriedade vem de um `rng` local, então
chamadas repetidas não acumulam estado. Motivo: os invariantes rodam sobre dados
**regenerados do zero** (fixture `df_fresh`), não só sobre o CSV comitado.

## ADR-02 — Invariantes são fonte de verdade

Os thresholds de `tests/test_data_invariants.py` não se ajustam para "passar". Quando o
viés noturno ficou perto do teto da faixa, ajustou-se a **distribuição do gerador**
(`p=[0.25,0.25,0.50]`), não o teste.

## ADR-03 — Task runner: Makefile

Escolhido sobre `justfile` por ser zero-install no CI Ubuntu e universalmente reconhecível.

## ADR-04 — Anonimato com denylist externa + skip

A denylist nunca entra no repo. Vem de `RCA_DENYLIST` (CSV inline) ou `RCA_DENYLIST_FILE`.
Sem nenhuma das duas, o teste faz `pytest.skip`; o CI injeta via secret `RCA_DENYLIST`.

## ADR-05 — Métrica antes/depois do Encontro 3

"Antes" usa a série semanal **real** da Serra-02 (crescente). "Depois" é uma série
**ilustrativa, determinística e rotulada como tal** (projeção da redução esperada). Motivo:
honestidade pedagógica — a correção não ocorreu no log de 90 dias; apresentar projeção como
medição ensina o hábito errado. O notebook traz um markdown explicando a escolha.

## ADR-06 — Contagem de PNG por notebook é invariante versionado

`PNG_ESPERADO` em `tests/test_notebooks.py` trava a contagem real: Encontro 1 = 5,
Encontro 2 = 4, Encontro 3 = 3. O teste reexecuta o notebook e confere a contagem.

## ADR-07 — Ruff ignora `notebooks/`

Os notebooks são material didático (quebras de linha e imports de demonstração
intencionais); `extend-exclude = ["notebooks/"]` evita churn de formatação. A corretude do
código dos notebooks é garantida por `test_notebooks.py`, que os executa do zero.

## ADR-08 — `SETOR_ALVO` parametriza só a camada de tradução

Uma constante `SETOR_ALVO` parametriza **apenas** a camada plugável de exemplos: o
mapeamento de tradução fábrica→setor (Encontro 2), o enquadramento do mock (Encontro 3) e a
coluna **"→ Laboratório de ensaios"** da tabela *Da fábrica para a TI*. Trocar o setor é
mudar só essa constante (e, se quiser, adicionar uma entrada em `TRADUCAO_SETOR`) — **sem
rebuild de dados nem alteração da análise de fábrica** (Serra-02/Coladeira-01) dos notebooks.

**Default atual:** `"laboratorios-de-ensaios"` (rótulo "laboratório de ensaios analíticos /
life sciences"); o `"generico"` (service desk de TI) fica como fallback. O mapeamento de
vocabulário do setor: defeito sistemático da Serra-02 → método/instrumento/LIMS com
reanálise sistemática; viés de turno → concentração num turno/lote/laboratório da rede;
recorrência sutil da Coladeira-01 → integração de equipamento que perde dados ~semanal;
refugo/retrabalho → reanálise de amostras; métrica antes/depois → **TAT** e taxa de
reanálise (≙ MTTR/SLA); distrator Crítico isolado → incidente único (ex.: queda de energia
num laboratório). Nenhum nome de empresa real aparece no material.
