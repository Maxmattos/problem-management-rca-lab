# Guia do instrutor — Encontro 3: Validar a solução e comunicar

> **Notebook do aluno:** [`notebooks/03_aluno_validar_comunicar.ipynb`](../notebooks/03_aluno_validar_comunicar.ipynb)
> **Duração sugerida:** 90 min.

## Objetivo do encontro

Fechar o ciclo: distinguir **causa-raiz de sintoma** (workaround vs solução permanente),
**provar eficácia** com uma métrica declarada e um antes/depois honesto, **comunicar** via
PIR e tradução técnico→negócio, e treinar a **entrevista** (mock) com o banco de perguntas.

## Roteiro e tempo

| Bloco | Tempo | O que fazer |
|---|---|---|
| Causa-raiz vs sintoma | 15 min | Workaround estabiliza; solução permanente derruba. |
| Provar eficácia + ADR-05 | 20 min | Métrica declarada; honestidade do "depois ilustrativo". |
| Comunicação: PIR + R$ | 15 min | Traduzir ocorrências/semana em refugo evitado (R$). |
| Mock interview | 30 min | Conduzir 4–6 perguntas em STAR; usar critérios abaixo. |
| Fechamento | 10 min | O que levar para a entrevista real. |

## O ponto não-negociável (ADR-05): honestidade da métrica

A correção **não ocorreu** no log de 90 dias. O "depois" no notebook é uma **projeção
determinística rotulada como ilustrativa**, não uma medição. Faça a aluna verbalizar isso:
**apresentar projeção como medição destrói credibilidade** numa entrevista e na vida real.
O gráfico marca o ponto da intervenção e rotula o trecho verde como ilustrativo de propósito.

## Como conduzir o mock

1. Escolha 4–6 perguntas do banco (sugestão de mix: 2 fundamentos, 2 RCA-STAR, 1 validação,
   1 comunicação).
2. A aluna responde em **STAR** (Situação · Tarefa · Ação · Resultado), puxando da Serra-02
   e da Coladeira-01.
3. Use os **critérios de boa resposta** e os **sinais de alerta** abaixo.

## Respostas-modelo (gabarito do mock)

> **Setor-alvo: laboratório de ensaios analíticos / life sciences.** As perguntas e fontes
> são de ITIL/RCA (agnósticas); peça à aluna para **traduzir** os exemplos da fábrica para o
> vocabulário do laboratório — LIMS, amostra→resultado, ensaio/análise, instrumento
> analítico, TAT/SLA, reanálise, rede de laboratórios. Equivalências rápidas: Serra-02 →
> método/instrumento que força reanálise sistemática; Coladeira-01 → integração de
> equipamento que perde dados ~semanal; refugo → reanálise de amostras; métrica de eficácia
> → TAT e taxa de reanálise. **Nenhum nome de empresa real** deve aparecer nas respostas.

**"Quando um conjunto de incidentes vira um problema?"** *(interviewquestions.guru)*
> Quando incidentes **reincidem com a mesma assinatura** ou seguem **sem correção
> permanente** — não é a severidade, é o padrão. Ex.: a Serra-02 (tendência+Pareto) e a
> Coladeira-01 (recorrência regular de baixo volume) viram problema; o incêndio isolado,
> apesar de Crítico, **não**.
> ✔ Cita padrão (tendência/recorrência), não severidade. ✘ Diz "quando é P1/Crítico".

**"Reativo vs proativo."** *(hirist)*
> Reativo: investigar depois que o incidente machucou. Proativo: a **análise de tendência**
> aponta degradação antes da crise — foi o caso da Serra-02 (rampa, sem P1).
> ✔ Dá exemplo concreto de detecção proativa. ✘ Só define os termos.

**"O que é workaround e como se relaciona com a solução permanente?"** *(theknowledgeacademy)*
> Workaround é alívio temporário (recalibrar a serra todo turno) — legítimo **enquanto** a
> solução permanente (padrão de calibração/manutenção preventiva) não entra, e deve ser
> **documentado** (KEDB). Parar no workaround mantém o problema aberto.
> ✔ Workaround documentado + temporário. ✘ Trata workaround como solução final.

**"Um mesmo chamado se repete toda semana — o que você faz?"** *(skilr; hirist)*
> Identifico o padrão no histórico (recorrência/cadência), **abro registro de problema**,
> ligo os incidentes e inicio RCA. Exatamente o caminho da Coladeira-01.
> ✔ Abre problema + RCA. ✘ Só "resolve o chamado de novo".

**"Problema recorrente cuja causa-raiz você descobriu."** (STAR) *(yardstick)*
> Espera-se a estrutura STAR com uma causa-raiz de **processo/insumo**, não um culpado.
> Bom exemplo: Coladeira-01 → lote/temperatura de cola sem controle.
> ✔ Resultado mensurável + ação permanente. ✘ Anedota sem métrica nem ação.

**"Trataram o sintoma; você resolveu na raiz."** (STAR) *(yardstick)*
> Serra-02: parar de só recalibrar (sintoma) e criar padrão de calibração/checagem por
> turno (raiz). ✔ Distingue contorno de cura. ✘ Confunde os dois.

**"Que metodologias de RCA você usa e quando?"** *(itjobswatch; hirist)*
> 5 Porquês (rápido, causa linear), Ishikawa/6 M (organizar múltiplas famílias de causa),
> Kepner-Tregoe (decisão estruturada com muitos candidatos). ✔ Sabe quando usar cada uma.

**"Como prova que a correção funcionou? Qual métrica?"** *(PIR; vervecopilot)*
> Declaro a métrica **antes** (volume semanal de corte-fora-medida da Serra-02; **no
> laboratório: TAT e taxa de reanálise**), defino alvo (≤ baseline) e janela de sustentação
> (≥4 semanas), e mostro antes/depois — com o "depois" rotulado como projeção até existir
> medição real.
> ✔ Métrica declarada antes + honestidade medição/projeção. ✘ "Os usuários pararam de
> reclamar" sem número.

**"Como traduz um achado técnico em impacto de negócio?"** *(interviewquery)*
> Converto ocorrências/semana em **refugo/retrabalho evitado (R$)** e falo em economia
> mensal, não em séries temporais (**no laboratório: amostras reanalisadas evitadas, ganho
> de TAT/SLA**). ✔ Fala a língua da liderança (R$, risco). ✘ Despeja jargão técnico.

## Critérios gerais de boa resposta / sinais de alerta

- ✔ Usa **evidência do próprio dado** (Serra-02/Coladeira-01) e fecha com **resultado**.
- ✔ Separa **medição** de **projeção**; nomeia a métrica antes de "consertar".
- ✘ Mede sucesso por "sumiram as reclamações"; confunde severidade com problema; trata
  workaround como solução; aponta culpado em vez de causa de processo.

## Fontes do banco de perguntas

finalroundai · interviewprep · invensislearning · hirist · theknowledgeacademy ·
itjobswatch (anúncio real) · yardstick · skilr · interviewquestions.guru · vervecopilot ·
interviewquery · treegarden / vawizard · linkedin (advice). Lista detalhada no `README`.
