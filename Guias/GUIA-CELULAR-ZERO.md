# GUIA — Celular Zero: configuração do zero para tráfego orgânico

> Guia operacional sequencial para quem **acabou de comprar um celular novo** e vai
> configurá-lo do zero para o método **orgânico / non-shop** (mercado EUA).
> Fonte única: `resumo/organico.md` (aulas 01–11, Gustavo Roque + Bifi, +
> GUIA_OPERACIONAL do colega). **Nada aqui é inventado.** Onde a aula não cobriu, está
> marcado `[?] não coberto nas aulas — confirme antes de prosseguir`.
>
> **Legenda:**
> 🔴 = **irreversível** — se errar, a conta/e-mail está queimado e você recomeça do zero.
> 🟡 = **perecível** — pode mudar com atualização da plataforma (data da aula ao lado).
> ⚠️ = alerta de erro. `(fato)/(opinião)/(testado)` = grau de confiança da fonte.
> Você está com o celular na mão agora. Só avance quando o **critério da etapa** estiver
> cumprido — "ter criado a conta" **não basta**.

---

## Antes de ligar o celular

Não toque no aparelho até ter tudo isto comprado/pronto. Faltar um item aqui te obriga a
parar no meio e improvisar — e improviso queima conta.

### 1. Proxy (ou VPN) — a identidade de rede
- **Proxy recomendado:** tipo **ISP residencial estático, plano dedicado**, localização
  **EUA**, protocolo trocado para **SOCKS5** (vem HTTP, você troca) **(testado)**
  [aula03 · 00:04:24; 00:09:26].
- **Fornecedores citados:** ProxyChip, PrivateProxy, IPRoyale [aula03].
- **Compre período maior** (desconto + estabilidade) e ative renovação automática
  **(opinião)** [aula03 · 00:07:42].
- **Confira o fraud score antes de usar:** ≤12 ok; até **25–30** aceitável; **>30 não usa**
  — peça substituição no chat do fornecedor com print **(testado)** [aula03 · 00:10:26].
- **Alternativa VPN:** 1 assinatura = até **5 dispositivos**; fornecedor citado como
  "Moved"/provável **Mudfish** `[?] grafia incerta` [aula03 · 00:16:48; 00:18:00].
- 🟡 **Divergência de fonte (proxy × VPN):** as aulas tratam como **alternativas** (use uma
  ou outra). O GUIA_OPERACIONAL do colega é mais específico: **escolha só uma e prefira
  proxy; não use as duas juntas** [FAQ 2]. **Risco:** misturar proxy + VPN = instabilidade
  de IP. (medido em 2026-08-22)

### 2. E-mail de cadastro
Três formas **(opinião/testado)** [aula02 · 00:00:00; 00:03:44]:
- E-mail antigo **sem cadastro** nas plataformas, **ou**
- Criar do zero (aquecendo **antes** — navegar, aceitar cookies), **ou**
- **Comprar pronto na GGMax** (o que o Gustavo faz hoje). Conferir vendedor: conta antiga,
  muitas vendas, boas avaliações, verificado **(testado)** [aula02 · 00:03:44].
- 🔴 **Só troque a senha do e-mail após ~7 dias** — trocar antes gera flag de "prática
  inadequada" **(opinião/testado)** [aula02 · 00:10:54].
- Configure **tudo** que o servidor pede (recuperação, foto, endereço). Use **o mesmo
  e-mail pessoal como recuperação** de todas as contas (centraliza controle) [aula02 · 00:09:54].

### 3. Número virtual para verificação
- Site de aluguel de número **ou Telegram** (o que o Gustavo prefere); no Gmail pode usar
  número BR **(opinião)** [aula02 · 00:01:56].
- 🟡 O GUIA_OPERACIONAL afina: número virtual **temporário dos EUA** basta; não compensa
  manter número permanente [FAQ 5]. (2026-08-22)

### 4. App de proxy no celular
- **SuperProxy** (Android/iOS) para colar as credenciais do proxy no aparelho.
  **Copie/cole** (evita erro entre `l` e `i`) **(opinião)** [aula03 · 00:10:55].

### 5. Planilha de controle (desde o dia 1)
- @, senha, e-mail de recuperação, plataforma, dispositivo, quem administra, status
  (ativo/banido) **(opinião)** [aula02 · 00:08:04].

> **Sobre o aparelho em si:** as aulas pedem "celular guardado/barato mas **fluido**",
> Android **(opinião/testado)** [aula03 · 00:01:59; aula04 · 00:04:51]. Você comprou um
> novo — serve. `[?] modelo específico não coberto nas aulas — qualquer Android fluido.`
> O **funil/link da oferta** (encurtar com domínio próprio + SSL, tag `organic`) é
> pré-requisito de **conteúdo**, não de configuração do aparelho — ver `organico.md`.

---

## Sequência obrigatória — passo a passo

Não pule etapa. Cada passo só termina quando o **Sinal de OK** aparecer.

### Passo 1 — Isolar o aparelho
- **O que fazer:** este celular **nunca** é o seu pessoal. Ele existe só para a operação.
- **Por que importa:** isolamento/contingência. Uma red flag numa conta contamina as
  outras contas do **mesmo dispositivo** **(fato/testado)** [aula03 · 00:00:29].
- **Sinal de OK:** o aparelho não tem nenhuma conta pessoal sua vinculada.
- ⚠️ 🔴 Usar o celular pessoal ou logar várias contas no mesmo dispositivo = red/yellow
  flag em cascata — pode derrubar tudo [aula03 · 00:00:29].

### Passo 2 — Hard reset
- **O que fazer:** faça **hard reset** e garanta que **nenhuma outra conta** esteja logada.
  `[?] o passo a passo do hard reset por modelo não é coberto nas aulas — confirme no
  manual do aparelho antes de prosseguir.`
- **Por que importa:** começar do zero real, sem rastro de conta anterior [aula03 · 00:01:59].
- **Sinal de OK:** aparelho limpo, zero contas logadas.

### Passo 3 — Aquecimento básico do dispositivo
- **O que fazer:** navegue como um usuário comum — abrir sites, **aceitar cookies** — por
  um tempo, antes de qualquer app de trabalho **(opinião/testado)** [aula03 · 00:01:59–00:02:52].
- **Por que importa:** simular humano reduz o instaban logo na criação da conta.
- **Sinal de OK:** o aparelho já "navegou" como pessoa normal por um período.
- Ver a seção **[Aquecimento](#aquecimento)** para o detalhe.

### Passo 4 — Configurar a rede (proxy OU VPN) — e não mexer mais
- **O que fazer:** configure o **proxy** no SuperProxy (credenciais coladas, protocolo
  **SOCKS5**) **ou** ligue a **VPN** no país/estado/servidor **em cascata** (evita ficar
  alternando = instabilidade) **(testado)** [aula03 · 00:09:26; 00:21:21].
- **Por que importa:** identidade de rede **estável** é a base de tudo. Configurou, **não
  troca** IP nem localização depois **(fato)** [aula03 · 00:03:03].
- **Sinal de OK:** proxy/VPN ativo, apontando para os EUA.
- ⚠️ 🔴 **Depois de configurado, não troque** dispositivo, IP ou localização. Trocar pode
  exigir refazer aquecimento e **perder a conta** [aula03 · 00:03:03; aula04 · 00:06:24].
- ⚠️ **1 proxy/IP por dispositivo — nunca misturar** conexões entre dispositivos
  **(fato)** [aula04 · 00:07:53].

### Passo 5 — Verificar fraud score e geolocalização
- **O que fazer:** confira o **fraud score** do IP no site próprio do fornecedor e abra um
  **link de geolocalização** no navegador do aparelho para checar o país **(testado)**
  [aula03 · 00:10:26; aula04 · 00:21:32].
- **Por que importa:** IP "sujo" ou geolocalização errada derruba a entrega antes de começar.
- **Sinal de OK:** fraud score **≤12** (até 25–30 tolerável) **e** geolocalização = **EUA**.
- ⚠️ Fraud score **>30** → peça substituição do IP (print no chat) e **não avance**
  [aula03 · 00:06:45].

### Passo 6 — Instalar o e-mail antes dos apps de trabalho
- **O que fazer:** baixe **Gmail/Outlook** e logue o e-mail de cadastro **antes** de instalar
  Instagram/TikTok **(opinião)** [aula04 · 00:22:32].
- **Por que importa:** ordem de instalação coerente com um usuário real.
- **Sinal de OK:** e-mail logado e funcionando no aparelho.

### Passo 7 — Criar a conta da plataforma
> **Regra de plataforma:** 🔴 **Instagram só em celular físico** — em virtual o instaban na
> criação é altíssimo (nos testes, só ~3 contas de virtual ficaram de pé) **(testado)**
> [aula05 · 00:00:00; aula11 · 01:28:44]. **TikTok e Facebook:** físico **ou** virtual.

**Instagram** [aula05]:
- **O que fazer:** criar **com e-mail** (não com número). **Pule** sugestões de número e de
  seguir contas (não poluir o algoritmo). **NÃO** coloque foto, bio nem link na criação —
  isso vem depois **(opinião/testado)** [aula05 · 00:01:05–00:03:34].
- **Por que importa:** conta "limpa" na criação passa pela análise; poluir cedo flaga.
- **Sinal de OK:** conta criada **sem travar** na tela de nome/avatar.
- ⚠️ 🔴 **Travou na tela de nome/avatar** = conta já flagada. Revise fraud score, aquecimento
  e e-mail; se persistir, **descarte e refaça do zero** [aula05 · 00:03:34].
- ⚠️ 🔴 **Pediu verificação de documento** → **descarte a conta e o e-mail** e recomece.
  **Não envie documento** **(opinião)** [aula05 · 00:06:21].
- **Pediu Face ID** → faça com o **seu próprio rosto** (é IA, não cruza com o nome/gênero do
  avatar) — isto **não** é problema **(fato)** [aula05 · 00:05:21].

**TikTok** [aula07]:
- **O que fazer:** **antes de criar**, nas configs do celular desabilite contatos,
  atualização em 2º plano, dados celulares e tracking/localização. Crie **com e-mail**,
  pule o nickname **(testado)** [aula07 · 00:01:48; 00:03:41].
- **Sinal de OK:** no rodapé da criação **não aparece país** (EUA correto).
- ⚠️ Se o rodapé mostra **"Brasil"** = proxy/VPN mal configurado. Volte ao Passo 4/5 antes
  de seguir **(fato)** [aula07 · 00:02:47].

**Facebook** [aula06]:
- **O que fazer:** use um **perfil pessoal ANTIGO** (seu ou de parente/cônjuge) para criar
  as **fanpages** — perfil novo é "cru" e o Facebook limita a criação de páginas
  **(fato/opinião)** [aula06 · 00:00:29].
- Crie a página **com tudo de uma vez** (diferente do IG): nome **igual ao do IG**, categoria
  "blog", **bio em 4 linhas** (as 3 do IG + linha 4 com o link), endereço americano
  qualquer, horário "sempre aberto", foto/capa congruentes [aula06 · 00:02:59].
- **Segurança:** compartilhe a página como **admin com um 2º perfil de confiança** — se
  perder o principal, não perde as páginas **(opinião/testado)** [aula06 · 00:07:40].
- **Vincule Instagram ↔ Facebook** sempre pelo **perfil pessoal**, não pela página
  **(fato)** [aula06 · 00:11:11].
- **Sinal de OK:** página criada, com link clicável na bio, vinculada ao IG.

### Passo 8 — Aquecer a conta
- Vá para a seção **[Aquecimento](#aquecimento)**. **Não publique conteúdo de venda nem
  configure automação de DM** antes do aquecimento estar concluído.

---

## Aquecimento

**O que é:** simular um usuário humano comum por dias antes de operar, para a plataforma não
tratar a conta como bot. É consenso em toda etapa (e-mail, dispositivo, conta) [aulas 02, 03,
05, 07].

**Onde se faz:**
- **E-mail** (criar/aquecer): pode ser no **computador**, em um **perfil do Chrome por
  conta** (sem login inicial; nome tipo "perfil aula 0001") **(opinião)** [aula02 · 00:00:30].
- **Dispositivo e contas (IG/TikTok):** no **próprio celular** (scroll, curtir, comentar,
  postar) — é o aparelho que precisa parecer humano.

### Instagram — 5 dias (o mais longo)
**(opinião/testado)** [aula05 · 00:06:51–00:20:45]:
- **Dias 1–3:** aquecer **≥30 min/dia** — scrollar Reels, curtir, comentar, salvar, buscar
  hashtags do nicho (isso já é benchmark simultâneo).
- **Dia 3:** finalizar configs — foto do avatar, **bio em 3 linhas** (1: identidade + âncora
  EUA; 2: promessa; 3: CTA + setinha para o link), habilitar **conta profissional** (para
  ver métricas de entrega/país).
- **Dia 4:** aquecer **~15 min** + **primeiro post** (vídeo de **engajamento**, não de venda;
  habilite "vídeo em alta qualidade").
- **Dia 5 em diante:** **5–10 vídeos de engajamento**.

### TikTok — aquecimento rápido
**(testado)** [aula07 · 00:07:11–00:12:30]:
- Poste um vídeo **direto da câmera do TikTok** (qualquer coisa) → aguarde **24h** → poste o
  2º. Se não pegar views, poste **de 4 em 4h** até pegar.
- **Configs dia 2:** verificar e-mail; desativar "atividades do perfil para seguidores" e
  "sugestões de contato/Facebook"; foto = mesma do IG/FB; bio (identidade/promessa/CTA).

### Facebook — mesma estrutura do Instagram
**(fato)** [aula07 · 00:05:41].

### Métricas que indicam aquecimento bem-sucedido (pode seguir)
🟡 (dependem da interface/algoritmo atuais — medido em **2026-08-22**):
- **≥200 views** nos primeiros vídeos = perfil saudável (ou já conseguir ver a localização
  de entrega) [aula05 · 00:18:45; aula07 · 00:08:40].
- **Alcance EUA — Instagram:** **≥60–61% saudável**; 0–60% → revisar conteúdo/proxy; sem
  alusão aos EUA mas com proxy ok fica ~40–45% [aula05 · 00:33:32].
- **Alcance EUA — TikTok:** **≥76% saudável**; 0–75% → revisar [aula07 · 00:30:05].
- No TikTok o alcance depende do **local de criação** da conta (criou com proxy EUA → entrega
  EUA); no Instagram depende do conteúdo/alusão [aula07 · 00:25:40].

### Regras que valem durante o aquecimento
- **Alusão explícita aos EUA em tudo** (bandeira, lojas — Target/Macy's/Best Buy/Walmart —,
  esportes, música nativa, inglês 100%): a **visão computacional** analisa frame, áudio, copy
  E legenda **(testado)** [aula05 · 00:22:15].
- **Bloqueio geográfico + idade mínima 25** (IG) / **24+** (FB) para BR, Índia, Canadá,
  Austrália, UK **(opinião/testado)** [aula05 · 00:30:34; aula06 · 00:16:11].
- **Link na bio só com ≥1.000 seguidores**; antes disso, CTA para a **DM** (comentar keyword)
  **(fato)** [aula07 · 00:13:30].
- 🔴 **Automação de DM só após 7–10 dias** de conta. Antes, DM **100% manual** **(opinião/
  testado)** [aula11 · 00:58:36]. (Ver divergência em **Sinais de alerta**.)
- 🔴 **Trocar senha** (e-mail e TikTok) só após **~7 dias** de conta ativa [aula02 · 00:10:54;
  aula07 · 02:22:45].

---

## Sinais de alerta

### 🔴 Red flags (banimento / conta queimada — recomeça do zero)
- **Travou na criação** (tela de nome/avatar no IG) → conta flagada [aula05 · 00:03:34].
- **Pediu verificação de documento** → **descarte conta e e-mail**, não envie [aula05 · 00:06:21].
- **Instagram criado em dispositivo virtual** → instaban altíssimo [aula05 · 00:00:00].
- **Celular pessoal / várias contas no mesmo dispositivo** → red flag em cascata
  [aula03 · 00:00:29].
- **Trocar dispositivo/IP/localização após configurar** → pode perder a conta [aula04 · 00:06:24].

### 🟡 Yellow flags (alerta que pode se propagar entre contas do mesmo dispositivo)
> Conceito: **red flag = banimento (vermelho)**; **yellow flag = alerta (amarelo)** que pode
> se propagar entre contas do mesmo dispositivo [aula03 · 00:00:59].
- **Automação de DM cedo demais** → yellow flag e risco de perder a conta [aula11 · 00:59:49].
- **Trocar senha antes de ~7 dias** → flag de prática inadequada [aula02 · 00:10:54].
- **Rodapé "Brasil" no TikTok** na criação → proxy/VPN errado; corrija antes de seguir
  [aula07 · 00:02:47].
- **Fraud score >30** → troque o IP [aula03 · 00:10:26].
- **Alcance abaixo do saudável** (IG <60% / TikTok <76%) → revisar conteúdo/proxy e voltar a
  interagir ≥20 min/dia [aula05 · 00:33:32; 00:35:00].
- **Encurtador grátis** → Meta/TikTok travam ou avisam "link inseguro"; passagem cai de ~70%
  para 20–30% → use **domínio próprio + SSL + encurtador pago** [aula01 · 00:19:44].

### Divergência a decidir (não escolho por você)
- 🟡 **Automação de DM no começo:** o `organico.md` (aula 11, Gustavo/Bifi) é enfático —
  **DM 100% manual nos primeiros 7–10 dias**, automação (ManyChat/mini chat) só depois. O
  GUIA_OPERACIONAL do colega (FAQ 11) admite **"operação manual OU automação nativa"** já no
  início, deixando o ManyChat para quando a conta amadurecer.
  **Risco de automatizar cedo:** yellow flag / perder a conta. **Risco de manual:** mais
  trabalho manual nos primeiros dias. [aula11 · 00:58:36 × GUIA_OPERACIONAL FAQ 11] (2026-08-22)
- 🟡 **Contas por dispositivo:** Instagram = **1 conta/dispositivo** (regra). TikTok = número
  **operacional** do colega diz **até ~4 contas/dispositivo** — perecível, depende da
  tolerância atual da plataforma. **1 proxy por dispositivo continua valendo nos dois casos.**
  [GUIA_OPERACIONAL FAQ 4] (18/08/2026)

---

## Checklist de conferência

Revise **antes** de cada etapa crítica.

### Antes de ligar o celular
- [ ] Proxy ISP residencial estático/dedicado EUA comprado, **SOCKS5**, fraud score **≤12**
- [ ] (ou VPN — e **não** as duas juntas)
- [ ] E-mail de cadastro pronto (comprado/criado e aquecido) — **senha NÃO trocada** (esperar 7 dias)
- [ ] Número virtual (temporário EUA) disponível para verificação
- [ ] App **SuperProxy** instalado
- [ ] **Planilha de controle** criada (@, senha, recuperação, plataforma, dispositivo, responsável, status)

### Antes de criar a conta
- [ ] Este **não** é o celular pessoal
- [ ] **Hard reset** feito; **nenhuma** outra conta logada
- [ ] Aquecimento básico do dispositivo feito (navegar/cookies)
- [ ] Proxy/VPN ativo e **apontando para EUA** (geolocalização conferida no navegador)
- [ ] Fraud score **≤12** (até 25–30 tolerável; >30 troca)
- [ ] **1 proxy por dispositivo** (não misturado)
- [ ] Gmail/Outlook instalado e logado **antes** dos apps de trabalho
- [ ] Instagram? → **celular físico** (nunca virtual)

### Durante a criação da conta
- [ ] Criando **com e-mail** (não com número)
- [ ] IG: **sem** foto/bio/link na criação; pulou sugestões
- [ ] TikTok: rodapé **não** mostra "Brasil"; tracking/contatos desabilitados
- [ ] **Não** travou na tela de nome/avatar
- [ ] **Não** pediu documento (se pediu → descarta)

### Antes de publicar / operar
- [ ] Aquecimento da plataforma **concluído** (IG 5 dias / TikTok rápido)
- [ ] Métrica de saúde batida: **≥200 views**, alcance IG **≥60%** / TikTok **≥76%**
- [ ] Alusão aos EUA presente em avatar/bio/conteúdo
- [ ] Bloqueio geográfico + idade mínima configurados (IG 25 / FB 24+)
- [ ] DM **manual** (automação só após 7–10 dias)
- [ ] Link na bio **só se ≥1.000 seguidores** (senão, CTA para DM)
- [ ] Link encurtado com **domínio próprio + SSL** (nunca encurtador grátis; nunca editar o
      link de afiliado na mão — 🔴 quebra a afiliação [aula01 · 00:04:19])
- [ ] Conta e senhas registradas na **planilha**
```
