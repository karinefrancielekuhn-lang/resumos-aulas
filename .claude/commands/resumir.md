---
description: Atualiza os resumos POR TEMA em resumo/ a partir das transcrições novas (síntese consolidada + registro por aula).
---

# /resumir — resumos por tema, que crescem a cada aula

Os resumos **não são por aula, são por tema**. Cada arquivo em `resumo/` junta
tudo que já entrou naquele tema e é **destilado** a cada aula nova. Escreva sempre
em **português do Brasil**.

## Temas (um arquivo por tema, criados conforme aparecem)

`resumo/facebook-ads.md`, `resumo/copy.md`, `resumo/google-ads.md`,
`resumo/metricas.md`, `resumo/gestao-de-trafego.md`, `resumo/criativos.md`.

Uma mesma aula pode alimentar **vários** temas (ex.: a primeira aula é
`copy` + `criativos`). Crie o arquivo do tema só quando a primeira aula daquele
tema entrar.

## Estrutura de cada arquivo de tema (duas camadas)

```markdown
# {Tema}

<!-- ===== SÍNTESE CONSOLIDADA (reescrita por inteiro a cada aula nova) ===== -->
{ver seção "Síntese consolidada" — é destilação, não acúmulo}

<!-- ===== REGISTRO POR AULA (append-only, ordem cronológica) ===== -->
{blocos de aula empilhados; NUNCA reescreva nem apague um bloco já existente}
```

- **SÍNTESE CONSOLIDADA (topo):** reescrita por inteiro a cada aula nova. Não é
  acúmulo — é a destilação de tudo que já entrou no arquivo.
- **REGISTRO POR AULA (abaixo):** empilhado em ordem cronológica, **append only**.
  Nunca reescreva nem apague um bloco de aula já existente.

## Passo a passo

1. Leia `glossario.txt` — use só para grafar corretamente nomes próprios
   (professores) e jargão. Não é fonte de conteúdo.
2. Liste `transcricao/*.txt`.
3. Para cada transcrição, descubra **data**, **tema(s)** e **professores** a
   partir do **nome do arquivo de áudio** correspondente (mesmo nome-base em
   `audio/`). Veja "Inferência" abaixo.
4. Consulte `resumo/_indice.md` para saber se aquela aula **já entrou naquele
   tema**. Se já entrou, **pule** (não reprocessa a mesma aula no mesmo tema).
5. Para cada par (aula, tema) ainda não registrado:
   a. **Append** do bloco de aula no fim de `resumo/<tema>.md`.
   b. **Rewrite** da síntese consolidada no topo de `resumo/<tema>.md`.
   c. Atualize `resumo/_indice.md`.
6. Ao final, liste o que foi criado/atualizado.
7. **Commit automático** das mudanças (ver "Commit ao final").

## Inferência (data, tema, professores)

Extraia do nome do arquivo de áudio. Convenção (ver INSTRUCOES.md):
`AAAA-MM-DD-<tema[+tema]>-<professor[+professor]>-NN`.

- **Data:** o campo `AAAA-MM-DD` no início. Se for `sem-data`, a data é
  **indefinida** — registre "indefinida" no `_indice.md` e ordene por `NN`.
- **Tema(s):** os códigos entre a data e os professores, separados por `+`.
  Mapeie os códigos para os arquivos de tema:
  `copy→copy`, `criativos/criativo→criativos`,
  `facebookads/facebook/fbads→facebook-ads`, `googleads/google→google-ads`,
  `metricas→metricas`, `trafego/gestao→gestao-de-trafego`.
- **Professores:** os nomes após os temas, separados por `+`, confirmados contra
  `[PROFESSORES]` do glossário.

> Se tema(s) ou professores **não puderem ser inferidos com segurança do nome —
> PARE e pergunte ao usuário.** Data `sem-data` é caso esperado (não pergunte;
> use "indefinida"). Não invente tema nem presuma professor. Registre a resposta
> no `_indice.md` para não perguntar de novo.

> **Estado atual:** `sem-data-copy+criativos-bifi+amanda-01` → data indefinida,
> temas copy + criativos, professores Bifi e Amanda. Já confirmado pelo usuário.

## Priorização: Ouro — o que é acionável e específico

Aplique isto **tanto ao bloco de aula quanto à síntese consolidada**. É a regra
mais importante do comando.

Extraia com **prioridade máxima**:
- **Números concretos:** thresholds, limites, percentuais, orçamentos iniciais,
  janelas de tempo, quantos criativos por conjunto, quando cortar, quando escalar.
  **Sempre com o contexto e a condição em que valem.**
- **Regras "se X então Y"** — critérios de decisão, não princípios genéricos.
- **O que o professor faz e que contraria o que se ensina por aí** — e o porquê.
- **Erros** que ele diz ter cometido, ou que vê alunos cometendo.
- **Sequências e ordem de execução:** o que fazer primeiro, o que depois.
- **Comentários laterais e improvisados** com critério prático — ditos rápido,
  quase como aparte. São os mais valiosos e os mais fáceis de perder. Não os perca.

**Distinga sempre estas três coisas, e nunca as misture** (marque cada item):
- **(fato)** o que o professor afirma como fato;
- **(opinião)** o que ele apresenta como opinião ou preferência pessoal;
- **(testado)** o que ele apresenta como testado, com resultado observado.

**Proporção honesta:** não busque equilíbrio de espaço. Um número específico com
condição de uso vale mais que um parágrafo conceitual. Se a aula tem 80 minutos e
só 6 são acionáveis, o resumo reflete isso — e **diz explicitamente** que o resto
foi contextual ou motivacional.

**Não infle:** se ele não deu o número, não invente um plausível. Escreva
"mencionou o critério sem quantificar" e o timestamp.

No **bloco de aula**, isto vira a primeira seção, **## Ouro**, antes do roteiro.
Na **síntese consolidada**, o Ouro se acumula/destila no topo (números com condição,
regras de decisão, contrarianismos), com as marcações (fato)/(opinião)/(testado).

## Bloco de aula (append — nunca editar depois)

```markdown
## {AAAA-MM-DD} — {título da aula} · {professores}
Fonte: transcricao/{arquivo}.txt

**Ouro** (acionável e específico; marque (fato)/(opinião)/(testado))
- {número/threshold com a condição em que vale} — [{data} HH:MM:SS]
- Se {X} então {Y} — {critério de decisão}
- Contraria o mercado: {o que ele faz diferente} porque {motivo}
- Erro (dele/dos alunos): {qual} — {consequência}
- (Se pouco da aula for acionável, diga: "Aula majoritariamente contextual/
  motivacional; acionável abaixo.")

**Roteiro**
- [{AAAA-MM-DD} HH:MM:SS] {tópico} — {frase curta}

**Conceitos e definições** (como o professor formulou)
- **{conceito}:** {definição}

**Exemplos e casos concretos**
- {exemplo trabalhado, passo a passo}

**Números citados** (envelhecem rápido — sempre com a data)
- {CPA/ROAS/orçamento/benchmark} = {valor} — dito em {AAAA-MM-DD} por {professor}

**Ambiguidades**
- [?] [{AAAA-MM-DD} HH:MM:SS] {trecho duvidoso}
```

## Síntese consolidada (rewrite do topo)

Ao regravar o topo, compare o que a aula nova diz com o que já estava no arquivo.
Comece pelo **## Ouro consolidado** (números com condição, regras de decisão,
contrarianismos e erros recorrentes, com (fato)/(opinião)/(testado)) e depois
organize nestas seis subseções:

1. **Consenso** — o que se repete e se confirma entre aulas. É o núcleo estável.
2. **Evoluiu** — onde uma aula posterior mudou, refinou ou contradisse uma
   anterior. Mostre as **duas versões com data e professor**: "Em {data} Bifi
   dizia X; em {data} Amanda ajustou para Y". É o mais valioso do arquivo —
   **nunca** resolva a contradição silenciosamente escolhendo um lado.
3. **Perecível** — o que depende do estado atual da plataforma (interface do
   Gerenciador, políticas do Meta, benchmarks de custo, formatos disponíveis).
   Marque com a data e um aviso de que precisa ser **reconferido**.
4. **Estável** — princípios de copy, psicologia de oferta, estrutura de funil.
   O que não expira.
5. **Divergência entre professores** — quando dois professores ensinam
   abordagens diferentes para a mesma coisa, registre como **divergência**, não
   como erro.
6. **Lacunas** — o que foi prometido para uma aula futura ou ficou pela metade.

## Preservar "## Minhas anotações" (regra inviolável)

O usuário pode adicionar, no **fim** de qualquer arquivo de tema, uma seção que
começa exatamente com o título `## Minhas anotações`. Ao **regravar a síntese
consolidada** (ou qualquer parte do arquivo):

1. Antes de reescrever, **localize** a seção `## Minhas anotações` (do título até o
   fim do arquivo ou até o próximo `## ` de mesmo nível, o que vier primeiro) e
   **guarde o conteúdo dela na íntegra**.
2. Reescreva a síntese e mantenha os blocos de aula normalmente.
3. **Reanexe** a seção `## Minhas anotações`, sem alterar uma vírgula, ao **final**
   do arquivo.

Nunca edite, resuma, mova o conteúdo ou apague essa seção. Se não existir, não crie.

## Commit e push ao final

Depois de gravar tudo, faça **um** commit com as mudanças dos resumos e, em
seguida, **push**:

```bash
git add resumo/
git commit -m "resumo: <mensagem>"
git push
```

A `<mensagem>` deve descrever **qual aula entrou em quais temas**, por exemplo:
`resumo: aula 01 (Bifi, Amanda) → copy, criativos`.

Regras de robustez (nunca trave o fluxo por causa do git):
- Se nenhuma aula nova foi processada (tudo já estava no `_indice.md`), **não**
  commite nem faça push — apenas informe que não havia nada novo.
- Se o `git` não estiver inicializado ou não houver mudanças a commitar, avise e
  siga sem falhar.
- **O push é o último passo e é "best effort":** se ele falhar (sem remote
  configurado, sem internet, autenticação pendente), **avise o usuário mas NÃO
  trave** — o commit local já está feito e nada se perde. Diga que basta rodar
  `git push` depois para sincronizar. Nunca desfaça o commit por causa de um push
  que falhou.

## resumo/_indice.md (controle)

Tabela de controle. Uma linha por (aula × tema). Exemplo:

```markdown
# Índice de processamento

| Aula (transcrição) | Data da aula | Tema | Professores | Último processamento |
|---|---|---|---|---|
| sem-data-copy+criativos-bifi+amanda-01 | indefinida (01) | copy | Bifi, Amanda | AAAA-MM-DD |
| sem-data-copy+criativos-bifi+amanda-01 | indefinida (01) | criativos | Bifi, Amanda | AAAA-MM-DD |
```

Use esta tabela como fonte da verdade sobre o que já foi processado.

## Regras invioláveis

- **Não invente.** Só entra o que está na transcrição.
- **Todo timestamp referencia aula + horário** (`[AAAA-MM-DD HH:MM:SS]`), porque
  o arquivo de tema agora reúne várias aulas.
- Marque ambiguidade / trecho inaudível com **`[?]` e o timestamp**.
- **Preserve números, nomes próprios e termos técnicos** exatamente (corrigindo
  só grafia óbvia de nomes via `glossario.txt`; não traduza anglicismos do nicho).
- Escreva em **pt-BR**.
