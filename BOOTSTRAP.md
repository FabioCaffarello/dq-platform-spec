<!-- path: BOOTSTRAP.md -->
> Language: Portuguese (Brazilian)

# Bootstrap — DQ Platform Spec

Do zero ao primeiro spec. O fluxo prioriza fluidez com qualidade: sem
gates, sem critérios numerados, sem cerimônia. A qualidade vem dos
templates e da auto-crítica que encerra cada documento.

---

## Fase 1 — Criar o repositório

```sh
cd dq-platform-spec
git init && git add . && git commit -m "chore: bootstrap spec workspace"
git branch -M main
git remote add origin <url-do-seu-repo>
git push -u origin main
```

Versionado: o guia (`CLAUDE.md`, `AGENTS.md`, `.codex/AGENTS.md`), a
plumbing de references, os quatro templates, as quatro skills, os
quatro comandos, e os planos vazios. **Não** versionado: o conteúdo de
`references/dq-platform/`.

As travas de qualidade são duas: `pre-commit` localmente (instalável
com `pre-commit install --hook-type pre-commit --hook-type commit-msg`)
e o workflow `.github/workflows/ci.yml`, que roda exatamente os mesmos
hooks em todo PR e push para `main`. Local e CI nunca divergem porque
compartilham o mesmo `.pre-commit-config.yaml`.

---

## Fase 2 — Hidratar a reference

```sh
make refs-sync
make refs-status   # dq-platform  pin=main  lock-sha=4124478...  on-disk=<sha>
```

A reference aparece em `references/dq-platform/`, read-only e ignorada
pelo git.

**Atualizar no futuro:** `make refs-sync` (se o pin é uma branch) traz
o que há de novo. Para travar numa versão exata — recomendado quando um
spec depende de um estado preciso — edite `ref` no
`references/dq-platform.lock` para um SHA ou tag, num commit próprio, e
rode `make refs-sync`. Cada documento cita o SHA contra o qual foi
escrito, então a rastreabilidade nunca se perde.

---

## Fase 3 — A cadeia de destilação

Três planos, sete artefatos. Cada plano alimenta o seguinte; dentro de
cada plano, cada artefato destila o anterior. Você não precisa
percorrer tudo toda vez — deixe o trabalho decidir até onde subir.
Mas nunca pule pra frente (sem spec sem a arquitetura, sem brief sem
a vision, sem study sem a referência aberta).

```text
Learning   :  scout  →  study
                          │
                          ▼
Strategic  :            vision  →  brief
                                     │
                                     ▼
Execution  :                       system-design  →  spec  →  roadmap
```

### 3.1 Plano de aprendizado

#### `/scout <slug>` — o mapa amplo

Varre a referência em largura e produz um mapa: o que ela É, o que
ela FAZ, vocabulário, decisões estruturantes, e os tópicos que
merecem um `/study` depois. Uma vez por reference (ou de novo se o
pin mover muito). Sai em `studies/scout/`.

> Scout orienta; não mergulha. Se você abriu um ADR e leu até o fim,
> parou de fazer scout.

#### `/study <tópico>` — o mergulho

Lê a reference em profundidade num tópico e extrai aprendizado: o que
existe, o que vale manter, o que deixar pra trás, o que você faria
diferente. Não é decisão, é leitura honesta. Sai em `studies/`.

> Regra de ouro: leu, citou. Nunca raciocine sobre a reference de
> memória — abra os arquivos reais.

### 3.2 Plano estratégico

#### `/vision <slug>` — o horizonte

Define a direção de longo prazo: o problema de fundo, o estado futuro
desejado, princípios que orientam escolhas, anti-metas, temas/pilares
de trabalho, e as premissas não-validadas que sustentam tudo.
Duradoura — só se reescreve quando uma premissa load-bearing quebra.
Sai em `docs/strategy/`.

> Visão sem premissas explícitas é liturgia. Visão sem anti-metas
> vira lista de features por gravidade.

#### `/brief <slug>` — o elo operacional

Pega UM pilar da vision e o vira contexto operacional que um agente
carrega por meses: missão, done state observável, in/out of scope,
decisões já tomadas (com citação), constraints, handoffs, e — no topo
de "open decisions" — um **princípio de decisão** ("quando bater numa
escolha não listada, otimize por X sobre Y") que sustenta delegação
autônoma de longo prazo. Sai em `docs/strategy/`.

> O princípio de decisão é o load-bearing. A lista de open decisions
> envelhece; o princípio guia o que ninguém antecipou.

### 3.3 Plano de execução

#### `/system-design <tópico>`

Transforma o aprendizado acumulado em arquitetura: componentes,
fronteiras, fluxo de dados, modos de falha. Responde ao brief que o
enquadra. É o primeiro artefato **publicado** do plano de execução —
tem que se sustentar sozinho, sem estudos nem reference. Sai em
`docs/system-design/`.

> O esforço mora nos modos de falha e nas fronteiras. Um design só do
> caminho feliz não é design.

#### `/spec <tópico>`

Pega uma fatia do system design e a torna construível: escopo,
comportamento, interface, aceitação. É o que você entrega pro Claude
Code / Codex / um humano implementar. Sai em `docs/specs/`.

> Uma fatia construível por spec. Aceitação verificável de verdade
> ("X retorna Y para Z"), não "código revisado".

#### `/roadmap`

Sequencia as specs existentes. Não inventa escopo — decide ordem e
defende o porquê, a partir do mapa de dependências. Sai em
`docs/roadmap/`.

---

## Fase 4 — A auto-crítica é o gate

Não há rodada de crítica separada nem findings bloqueantes. Cada
template termina numa seção de auto-crítica obrigatória: a parte mais
frágil, o que não foi validado, o que mudaria a conclusão. É aí que a
qualidade é cobrada — embutida, não cerimonial.

A revisão humana é o gate final. Você lê, e se a auto-crítica do
documento for honesta, ela já te aponta onde olhar primeiro.

---

## Fase 5 — Crescer sem reescrever

- **Nova reference:** crie `references/<nome>.lock`, adicione
  `references/<nome>/` ao `.gitignore`, rode `make refs-sync`.
- **Novo ofício que se repete:** vira uma skill em `.claude/skills/`.
- **Novo tipo de artefato:** template + skill + comando, mesma forma
  dos sete que existem (scout, study, vision, brief, system-design,
  spec, roadmap).
- **Decisão durável demais pra ficar só num design:** promova a um ADR
  em `docs/adr/`.

Cresça por adição. Quando uma regra estiver errada pro trabalho à sua
frente, diga e mude o `CLAUDE.md`. Divergir em silêncio é a única
violação real.

---

## Resumo

Você tem um workspace que versiona o **como** (o pin, o método, os
templates) e ignora o **quê** (o conteúdo da reference). A referência
alimenta o plano de aprendizado (scout/study); o aprendizado alimenta
o plano estratégico (vision/brief); o plano estratégico alimenta o
plano de execução (system-design/spec/roadmap). Um terceiro repositório
de desenvolvimento consome as specs. Cada documento publicado se
sustenta sozinho, cita o commit exato contra o qual foi escrito, e
termina sendo honesto sobre suas próprias fraquezas. Os mesmos
documentos que orientam humanos orientam agentes de IA — por meses,
sem re-derivar contexto a cada sessão.
