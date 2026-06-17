# Cheat sheet — Problem Management na prática (1 página)

> Único material que você leva. Cabe a régua de decisão, os passos de RCA e as perguntas
> prováveis de entrevista.

## As 4 lentes (ruído vs problema)

| Lente | Pergunta | É problema quando… |
|---|---|---|
| **Tendência** | o volume sobe e se mantém? | há rampa sustentada vs baseline |
| **Pareto (80/20)** | poucas máquinas concentram tudo? | uma líder isolada (degrau grande p/ a 2ª) |
| **Recorrência** | a mesma assinatura se repete? | cadência regular, *mesmo* com volume baixo |
| **Severidade** | é grave? | ⚠️ gravidade **não** define problema |

## Régua de decisão

- **Problema** = tendência sustentada **OU** concentração no Pareto **OU** recorrência da
  mesma assinatura. Sempre com **evidência no dado**.
- **Incidente isolado** = evento único, sem tendência e sem recorrência — *mesmo que seja
  Crítico*. (O "incêndio no painel" é a armadilha clássica.)
- Em dúvida? Peça a evidência. Sem tendência/Pareto/recorrência → é incidente.

## Da fábrica para a TI → laboratório de ensaios (ITIL 4)

| Fábrica | TI / ITIL | → Laboratório de ensaios |
|---|---|---|
| Ocorrência (refugo, parada) | Incidente | Resultado inválido / amostra p/ reanálise |
| Máquina com refugo recorrente | Problema | Método/instrumento/LIMS com reanálise sistemática |
| Recalibrar todo turno | Workaround | Recalibrar/repetir o ensaio a cada lote |
| Causa conhecida + contorno | Known Error (KEDB) | Known Error do método/instrumento |
| Manutenção preventiva / padrão | Solução permanente | Validação/calibração de método padronizada |
| Refugo evitado (R$) | Impacto de negócio | TAT/SLA e taxa de reanálise (custo + atraso) |

## RCA em dois passos

**5 Porquês** — cada porquê preso a uma **evidência** (não opinião). Pare quando chegar a
uma causa de **processo/sistema** que você pode corrigir, não a um culpado.

**Ishikawa (6 M)** — organize as hipóteses em famílias e marque ★ só o que o dado sustenta:
> **Má**quina · **Mé**todo · **Ma**terial · **Mã**o de obra · **Me**dição · **Me**io ambiente

## Provar que a correção funcionou

1. **Declare a métrica antes** (ex.: ocorrências/semana da assinatura).
2. **Alvo + janela**: voltar ao baseline e **manter ≥4 semanas**.
3. **Não confunda medição com projeção** — rotule projeções como tal.
4. Traduza para **R$** (refugo/retrabalho evitado) ao falar com a liderança.

## Perguntas prováveis (com bullets de resposta)

- **Quando incidentes viram problema?** → padrão (recorrência/tendência), não severidade.
- **Reativo vs proativo?** → proativo = tendência aponta antes da crise (ex.: a rampa).
- **Workaround vs solução permanente?** → alívio temporário documentado vs cura da causa-raiz.
- **Chamado repete toda semana — o que faz?** → abre problema, liga incidentes, roda RCA.
- **Como prova a eficácia?** → métrica declarada antes + alvo + janela; medição ≠ projeção.
- **Traduz técnico → negócio?** → fale em R$ evitado e risco, não em séries temporais.

> Método de resposta: **STAR** (Situação · Tarefa · Ação · Resultado). Puxe exemplos reais
> do que você analisou no lab.
