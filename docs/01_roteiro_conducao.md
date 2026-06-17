# Roteiro de condução — Aula 1 (1 página) · ~90 min

> Companheiro do [`01_guia_instrutor.md`](01_guia_instrutor.md) (gabarito, "se a aluna
> travar", régua de decisão). Aqui é o roteiro minuto a minuto.
> Os `#N` são a **posição** da célula no notebook (0–24).

**Regra de ouro:** hoje é **triagem, não diagnóstico**. Meta = decidir *se* existe problema, não achar a causa.
**Frase-âncora (repita):** "Incidente é o evento; problema é a causa que faz o evento se repetir."
**Números na manga:** 343 ocorrências · MTTR mediano 24h · 5 críticos · Serra-02: baseline 3,5/sem → 10,5/sem · 57% Noite · Pareto 99 vs 40 (~2,5× a 2ª).

---

## Abertura — 10 min · md #0–1
- Mostra tabela fábrica→TI. Diz: a régua é a mesma em TI; a fábrica é só andaime.
- **Não** roda código ainda.

## KPIs + painel cru — 10 min · roda #2 e #5
- Roda #2 (carrega df, 343 linhas) e #5 (KPIs).
- **Pergunta:** "Essa tabela responde *existe problema?* Por que não?" → ela deve dizer: lista eventos, não padrão.

## Lente 1 — Tendência — 15 min · roda #7, depois #8
- Roda #7 (total semanal). **Pausa.** Pergunta: "O total te diz onde está o problema?" (não — precisa abrir por máquina).
- Roda #8 (top 5, **anônimas A–E**). **Pausa real (conta até 5).**
  - **Pergunta:** "Qual linha se comporta diferente das outras?" → ela aponta a que sobe (=Máquina A).
  - Só **depois** ela apontar, revela: A = Serra-02. (mapa no comentário da célula)
- **Se travar:** "Esquece volume num dia. Olha a *direção* ao longo das semanas."

## Lente 2 — Pareto — 15 min · roda #11
- **Pergunta:** "Se só pudesse atacar UMA essa semana, qual? Por quê?" → quer a *justificativa* (topo do Pareto = maior retorno da RCA).
- Aponta o degrau: 99 vs 40 (a líder é ~2,5× a 2ª).

## Lente 3 — Recorrência — 15 min · roda #14
- Roda a tabela (head 10). **Pergunta:** "A Coladeira-01 está aqui?" → **não está** (13 ocorr., cai fora do corte).
- **Ensina o ponto:** esta tabela mede *volume*, não *cadência*. Volume baixo + repetição regular some daqui.
- Roda `investigar("Coladeira-01")`. Mostra: 1/semana por 13 semanas, assinatura idêntica. **Recorrência ≠ volume.**
- ✅ **Verificado:** o gráfico da Coladeira-01 mostra TODAS as semanas W09–W22 (semanas vazias = 0, não colapsam), então a cadência fica óbvia.

## Lente 4 — Severidade ≠ problema (a pegadinha) — 10 min · roda #19
- Roda lista de críticos (5 linhas, sem contagem). Aponta o **Incêndio (Prensa-01)** com algum drama.
- **Pergunta-armadilha:** "Esse é o problema nº 1 da lista?"
  - Se ela morder: "Grave, concordo. Mas problema é sobre susto de uma vez ou sobre o que se repete?" → ela mesma desmonta.
  - **Plano B (se ela NÃO morder):** "Isso. Por que tanta gente erra aqui?" → vira professora 30s.
- Leva: **gravidade ≠ recorrência.**

## Baseline (opcional, reforço) — roda #17
- Só rode **depois** dela ter escolhido a suspeita. Preencher `MAQUINA_SUSPEITA = "Serra-02"`.
- Mostra rampa vs baseline (3,5 → 10,5/sem).

## Exercício — 15 min · #24 (ela digita)
- Ela responde as 3 perguntas usando `investigar()`. Você só pergunta, não responde.
- **Gabarito (só você):** candidatas = Serra-02 (tendência+Pareto+recorrência) e Coladeira-01 (recorrência); falso problema = Incêndio; próxima ação Serra-02 = abrir registro de problema proativo + RCA (gancho Aula 2).

## Fechamento — 5 min
- Ela reconstrói as 4 lentes de memória (sem olhar).
- Veredito: **"Problema é padrão, não susto. Tendência, concentração e recorrência acendem o sinal; gravidade sozinha não."**
- Gancho: "Aula 2 a gente abre o registro da Serra-02 e a Coladeira-01 é tua."

---
**Se faltar tempo:** corte minutos do Pareto (#11), nunca a Lente 4. Ela é o clímax.
**Material que ela leva hoje:** nada. O cheat sheet é o material final das 3 aulas.
