# Guia do instrutor — Encontro 1: Ler o painel (ruído vs problema)

> **Notebook do aluno:** [`notebooks/01_aluno_sinal_vs_ruido.ipynb`](../notebooks/01_aluno_sinal_vs_ruido.ipynb)
> **Duração sugerida:** 90 min. **Material que a aluna leva:** só o `cheat_sheet_aluno.md`.

## Objetivo do encontro

Treinar a leitura de um painel de ocorrências e a **régua de decisão** que separa
incidente isolado de problema de verdade, com quatro lentes: **tendência, Pareto (80/20),
recorrência, severidade ≠ problema**. Nada de teoria de ITIL aqui — ela já domina; o foco
é a leitura do dado que sustenta a decisão.

## Roteiro e tempo

| Bloco | Tempo | O que fazer |
|---|---|---|
| Abertura + tabela fábrica→TI | 10 min | Ancorar o vocabulário. Deixar claro: a régua é idêntica em TI. |
| KPIs + painel cru | 10 min | "Uma tabela de 343 linhas não responde *existe problema?*". |
| Lente 1 — Tendência | 15 min | Volume semanal total e por máquina. Achar a rampa. |
| Lente 2 — Pareto | 15 min | Líder isolado + tamanho do degrau para a 2ª. |
| Lente 3 — Recorrência | 15 min | Volume baixo + assinatura repetida = problema. |
| Lente 4 — Severidade ≠ problema | 10 min | O distrator crítico de 1 ocorrência. |
| Exercício guiado | 15 min | A aluna usa `investigar()` e responde às 3 perguntas. |

## Gabarito do exercício

**1. Candidatas a problema:**

- **`Serra-02`** — **líder isolado do Pareto** (~99 ocorrências, ~3× a 2ª máquina) **e**
  **tendência de subida sustentada** (baseline ~3/sem → ~12/sem), sempre a mesma
  assinatura ("Corte fora de medida na Serra-02"). Tendência + Pareto + recorrência: é o
  problema principal. Pista extra para o Encontro 2: **~55% das ocorrências no turno da
  Noite**.
- **`Coladeira-01`** — volume **baixo** (~13 no período), então **não** aparece no topo do
  Pareto. Mas reincide em **cadência regular** (~semanal) com assinatura idêntica ("Falha
  de colagem na fita de borda") por mais de 60 dias. Sinal = **recorrência**, não volume.

**2. Parece problema mas não é:** o **"Incêndio no painel elétrico"** (Prensa-01,
gravidade **Crítico**) — severidade máxima, porém **1 única ocorrência** e sem tendência.
Incidente bem resolvido, não problema. É a armadilha da lente 4.

**3. Próxima ação para a candidata nº 1:** abrir um **registro de problema (proativo)**
para a Serra-02, ligando as ocorrências relacionadas, e iniciar a RCA sobre as evidências
— exatamente o Encontro 2.

**Régua de decisão (resumo):**

| Sinal | É problema? | Evidência no dado |
|---|---|---|
| Tendência sustentada de subida | Sim | rampa no volume semanal vs baseline |
| Concentração no Pareto | Sim | poucas máquinas = maioria das ocorrências |
| Recorrência da mesma assinatura | Sim | mesma `máquina+descrição` repetida/cadenciada |
| Crítico isolado, sem repetição | Não | contagem = 1, sem tendência |

## Se a aluna travar

- **"Tudo parece problema"** → volte à régua: peça a *evidência* de cada candidato. Sem
  tendência, Pareto ou recorrência, é incidente.
- **Fixou no incêndio** (porque é Crítico) → pergunte "quantas vezes aconteceu?". Severidade
  ≠ recorrência.
- **Ignorou a Coladeira-01** (porque é volume baixo) → mostre `investigar("Coladeira-01")`
  e a cadência regular. Pareto não é a única lente.

## Perguntas de entrevista para fechar o encontro

(Respostas-modelo no Encontro 3; aqui só provoque.)

- "Quando um conjunto de incidentes vira um **problema**?" *(interviewquestions.guru)*
- "Como decide se um incidente é **isolado** ou sinal de um problema sistêmico?" *(skilr)*
- "Com vários candidatos na fila, como **prioriza**?" *(Pareto/impacto)*
