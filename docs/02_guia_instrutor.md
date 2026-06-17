# Guia do instrutor — Encontro 2: Abrir o registro e rodar a RCA

> **Notebook do aluno:** [`notebooks/02_aluno_registro_e_rca.ipynb`](../notebooks/02_aluno_registro_e_rca.ipynb)
> **Duração sugerida:** 90 min.

## Objetivo do encontro

Transformar o achado do Encontro 1 (Serra-02) em **registro de problema** e conduzir a
**RCA** ancorada na evidência: 5 Porquês com cada degrau preso a um dado, Ishikawa (6 M)
destacando o que o dado sustenta, e uma RCA documentada no modelo curto. A aluna repete o
ciclo sozinha na **Coladeira-01**.

## Roteiro e tempo

| Bloco | Tempo | O que fazer |
|---|---|---|
| Gatilho proativo vs reativo | 15 min | Por que abrir o registro agora (rampa, não crise). |
| Evidência antes da hipótese — turno | 15 min | Viés noturno específico da Serra-02. |
| 5 Porquês ancorados | 20 min | Cada porquê → uma evidência ou verificação concreta. |
| Ishikawa (6 M) | 15 min | Marcar ★ só o que o dado sustenta. |
| RCA documentada | 10 min | Preencher o modelo curto. |
| Exercício Coladeira-01 | 15 min | A aluna conduz o ciclo inteiro. |

## Conceitos que valem reforçar

- **Proativo > reativo.** A Serra-02 nunca teve um "P1" estrondoso; ela sangrou refugo numa
  rampa. Abrir o registro *antes* da crise é o que distingue um analista sênior.
- **O dado sugere a hipótese, não o contrário.** O recorte por turno (viés noturno
  específico) vem antes de qualquer teoria sobre "por que à noite".
- **Hipótese ≠ causa confirmada.** O Porquê nº 4 (treino/iluminação/supervisão) é hipótese
  a validar com operadores e manutenção. A RCA aponta a direção; a confirmação é no chão.

## SETOR_ALVO

A célula `SETOR_ALVO` parametriza **apenas** os exemplos de tradução fábrica→setor (e a
coluna "→ Laboratório de ensaios" da tabela). Default atual: `"laboratorios-de-ensaios"`
(life sciences); `"generico"` (service desk de TI) fica como fallback. Para adaptar o
vocabulário a outro setor, adicione uma entrada em `TRADUCAO_SETOR` com as mesmas chaves e
troque o rótulo — **nada nos dados, na análise de fábrica ou nos gráficos muda**.

## Gabarito do exercício — RCA da Coladeira-01

**Confirmação da recorrência:** ~13 ocorrências em 90 dias, **cadência ~semanal**, todas
com a **mesma assinatura** ("Falha de colagem na fita de borda"), espalhadas por mais de
60 dias. Volume baixo → invisível no Pareto; **a recorrência regular é o sinal**.

**5 Porquês (modelo):**

| # | Pergunta | Resposta ancorada |
|---|---|---|
| 1 | Por que há retrabalho recorrente na Coladeira-01? | Falha de colagem na fita de borda — mesma assinatura reincidindo toda semana. |
| 2 | Por que a fita não cola? | Adesão insuficiente — verificável medindo temperatura da cola e força de adesão na amostra. |
| 3 | Por que a adesão é insuficiente? | Hipótese: **cola fora da janela de temperatura** ou **lote de cola/fita fora de especificação**. |
| 4 | Por que isso passa batido? | Sem **checagem de temperatura/lote** na preparação; a falha só aparece depois, na inspeção. |
| 5 | Por que não há checagem? | Falta **padrão de processo** (controle de temperatura + rastreio de lote) — causa-raiz de **material/método**. |

**Ishikawa (6 M) — ★ sustentado por dados / hipótese forte:**

- **Material** ★ — lote de cola/fita fora de especificação (assinatura idêntica reincidente sugere insumo).
- **Método** ★ — sem controle de temperatura da cola / sem rastreio de lote.
- **Máquina** — calibração de temperatura da coladeira (a verificar).
- **Medição** — ausência de checagem de adesão (a verificar).
- **Mão de obra / Meio ambiente** — sem evidência no dado (diferente da Serra-02, **não há
  viés de turno** na Coladeira-01 — bom contraste para a aluna notar).

**RCA documentada (modelo):**

> **Problema.** Retrabalho recorrente por falha de colagem na fita de borda na Coladeira-01
> (~13 ocorrências, cadência ~semanal, 90 dias).
> **Evidências.** Assinatura idêntica reincidente; cadência regular; volume baixo e estável
> (não é tendência, é recorrência); sem viés de turno.
> **Causa-raiz provável.** Insumo (lote de cola/fita) e/ou temperatura da cola fora de
> especificação, sem controle no processo — **material/método**.
> **Causas afastadas.** Turno/operador (sem viés no dado); tendência de degradação (volume
> é estável, não crescente).
> **Ação recomendada.** Controle de temperatura da cola + rastreio de lote de cola/fita +
> checagem de adesão por amostragem.

> **Ponto didático central:** Serra-02 e Coladeira-01 são **problemas de naturezas
> diferentes** — uma é **tendência+Pareto** (degradação de processo no turno), a outra é
> **recorrência** (insumo/método estável). Mesma régua, sinais diferentes.

## Se a aluna travar

- **Pula direto para a causa** ("é a cola ruim") → peça o porquê anterior e a evidência.
- **Copia o viés de turno da Serra-02** → mostre que a Coladeira-01 **não** tem viés de
  turno; a evidência manda, não o exemplo anterior.
- **Quer Ishikawa cheio de ★** → ★ é só para o que o *dado* sustenta; o resto é hipótese.

## Perguntas de entrevista para fechar

- "Diferença entre Problem Management **reativo e proativo**." *(hirist)*
- "Que **metodologias de RCA** você usa e quando?" (5 Porqués, Ishikawa, Kepner-Tregoe) *(itjobswatch)*
- "Conte sobre um **problema recorrente** cuja causa-raiz você descobriu." *(yardstick)*
