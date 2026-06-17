# ITIL Problem Management — Hands-on RCA Lab

A practical, data-driven lab for **ITIL 4 Problem Management**: turning a raw occurrence
log into signal, telling *isolated incidents* apart from *real problems*, running
**root-cause analysis (RCA)** on the evidence, and proving that a fix actually worked.

The theory of Problem Management (Incident vs Problem, Known Error, workarounds) is well
covered elsewhere. What practitioners rarely get to rehearse is the **practical** part:
*looking at a dashboard and deciding whether a problem exists, then validating whether a
proposed solution makes sense.* That is the gap this lab fills.

> The teaching content and dataset are in **Portuguese**; this README is in English.

[![CI](https://github.com/Maxmattos/problem-management-rca-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/Maxmattos/problem-management-rca-lab/actions/workflows/ci.yml)
![python](https://img.shields.io/badge/python-3.11%2B-blue)
![pandas](https://img.shields.io/badge/pandas-3.x-150458)
![plotly](https://img.shields.io/badge/plotly-5.x-3f4f75)

## Scenario

A synthetic **90-day occurrence log** for a **planned-furniture factory** (24x7, three
shifts). The shop-floor system records *occurrences* (stoppages, scrap, rework) per
machine, shift and product. The data is fully synthetic and generated from a seeded
script — no real company, system, or personal data. Three patterns are deliberately
planted so each exercise has a defensible "right answer":

| Pattern | What it teaches |
|---|---|
| A high-volume, worsening signature (`Serra-02`, off-spec cuts, night-shift biased) | trend + Pareto → the obvious problem |
| A low-volume, regularly recurring failure (`Coladeira-01`, edge-banding glue failure) | recurrence ≠ volume |
| A single, severe, one-off event (panel fire on `Prensa-01`) | high severity ≠ problem |

## What you practise (three meetings)

1. **Reading a dashboard** — separating noise from problems with four lenses: trend,
   Pareto (80/20), recurrence, and severity.
2. **Opening a problem record & running RCA** — proactive vs reactive triggers, then
   5 Whys and Ishikawa (6 M) grounded in the data.
3. **Validating the fix & communicating** — root cause vs symptom, proving efficacy with
   an honest before/after metric, a PIR, and a mock interview for the Problem Analyst role.

## Repository structure

```
itil-problem-management-rca-lab/
├── data/
│   ├── gerar_ocorrencias.py        # seeded, pure generator: gerar(seed, n_dias)
│   └── ocorrencias.csv             # generated dataset (343 occurrences, 90 days)
├── notebooks/
│   ├── 01_aluno_sinal_vs_ruido.ipynb       # signal vs noise (4 lenses)
│   ├── 02_aluno_registro_e_rca.ipynb       # problem record + 5 Whys + Ishikawa
│   └── 03_aluno_validar_comunicar.ipynb    # validate fix + PIR + mock interview
├── docs/
│   ├── 01_guia_instrutor.md        # instructor guide + answer keys (per meeting)
│   ├── 02_guia_instrutor.md
│   ├── 03_guia_instrutor.md
│   ├── cheat_sheet_aluno.md        # the only handout the student keeps (~1 page)
│   └── ADRs.md                     # design decisions
├── tests/                          # the harness (see "How it's verified")
├── .github/workflows/ci.yml
├── Makefile
├── pyproject.toml
├── requirements.txt                # runtime
└── requirements-dev.txt            # tests / lint / notebook execution
```

The student notebooks contain **no answer keys** — those live only in the instructor
guides (enforced by a test).

## Getting started

```bash
pip install -r requirements.txt -r requirements-dev.txt

# (Re)generate the dataset
make data            # or: python data/gerar_ocorrencias.py

# Open the notebooks
jupyter notebook notebooks/
```

Charts are committed as **static PNG** so they render directly on GitHub. To explore them
**interactively** in a live Jupyter session, set `pio.renderers.default = "notebook"` at
the top of any notebook (the cell shows where).

## How it's verified

Nothing is "done" without a test that proves it. `make verify` (which CI mirrors) runs:

| Check | What it proves | Where |
|---|---|---|
| **Determinism** | `gerar(42)` is pure and the committed CSV matches a fresh regeneration | `tests/conftest.py` |
| **Pedagogical invariants** | the three planted patterns actually hold on freshly generated data (Pareto leader ≥2×, rising trend, ~55% night bias, recurring subtle problem, one-off critical) | `tests/test_data_invariants.py` |
| **Notebook execution** | every notebook runs top-to-bottom and embeds the expected number of PNGs | `tests/test_notebooks.py` |
| **No answer keys** | student notebooks contain no embedded solutions | `tests/test_aluno_sem_gabarito.py` |
| **Anonymity** | no name from an external denylist leaks into the repo (denylist injected via CI secret; skips locally) | `tests/test_anonymity.py` |
| **Lint/format** | `ruff check` + `ruff format --check` | `pyproject.toml` |

```bash
make verify          # data + lint + tests, end to end
make test            # invariants + notebook execution + anonymity + no-answer-key
make lint            # ruff check + format check
make notebooks       # re-execute notebooks in place (refresh committed PNGs)
```

Design decisions are recorded in [`docs/ADRs.md`](docs/ADRs.md).

## Question bank sources (Meeting 3 mock interview)

Interview questions are paraphrased from public question banks and a real job posting:
finalroundai · interviewprep · invensislearning · hirist · theknowledgeacademy ·
itjobswatch (real posting) · yardstick · skilr · interviewquestions.guru · vervecopilot ·
interviewquery · treegarden / vawizard · linkedin (advice).

---

## PT-BR — Resumo

Laboratório prático de **Problem Management (ITIL 4)** focado na parte que cursos
raramente treinam: **olhar um painel de ocorrências e decidir se existe um problema de
verdade**, conduzir a **análise de causa-raiz (RCA)** sobre as evidências e **validar se a
solução realmente resolveu**.

Os dados são **sintéticos** (log de 90 dias de uma fábrica de móveis) e trazem três padrões
plantados: um problema de alto volume e tendência crescente (Serra-02), um problema
recorrente de baixo volume (Coladeira-01) e um evento crítico isolado que *parece* problema
mas é apenas um incidente (incêndio no painel). Os três encontros cobrem: (1) separar ruído
de problema, (2) abrir o registro e rodar a RCA, (3) validar a solução e comunicar.

## License

MIT — see `LICENSE`.
