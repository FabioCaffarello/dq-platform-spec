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

Quatro estágios, cada um consumindo o anterior. Você não precisa
percorrer a cadeia inteira toda vez — deixe o trabalho decidir até onde
subir. Mas nunca pule pra frente (sem spec sem a arquitetura que o
enquadra existir).

### 3.1 Estudo — `/study <tópico>`

Lê a reference e extrai aprendizado: o que existe, o que vale manter, o
que deixar pra trás, o que você faria diferente. Não é decisão, é
leitura honesta. Sai em `studies/`.

> Regra de ouro: leu, citou. Nunca raciocine sobre a reference de
> memória — abra os arquivos reais.

### 3.2 System design — `/system-design <tópico>`

Transforma o aprendizado acumulado em arquitetura: componentes,
fronteiras, fluxo de dados, modos de falha. É o primeiro documento
**publicado** — tem que se sustentar sozinho, sem o estudo nem a
reference. Sai em `docs/system-design/`.

> O esforço mora nos modos de falha e nas fronteiras. Um design só do
> caminho feliz não é design.

### 3.3 Spec — `/spec <tópico>`

Pega uma fatia do system design e a torna construível: escopo, comportamento,
interface, aceitação. É o que você entrega pro Claude Code / Codex / um
humano implementar. Sai em `docs/specs/`.

> Uma fatia construível por spec. Aceitação verificável de verdade
> ("X retorna Y para Z"), não "código revisado".

### 3.4 Roadmap — `/roadmap`

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
- **Novo tipo de artefato:** template + skill + comando, mesma forma dos
  quatro que existem.
- **Decisão durável demais pra ficar só num design:** promova a um ADR
  em `docs/adr/`.

Cresça por adição. Quando uma regra estiver errada pro trabalho à sua
frente, diga e mude o `CLAUDE.md`. Divergir em silêncio é a única
violação real.

---

## Resumo

Você tem um workspace que versiona o **como** (o pin e o método) e
ignora o **quê** (o conteúdo da reference). A reference alimenta
estudos; estudos viram arquitetura; arquitetura vira specs construíveis;
specs viram roadmap. Um terceiro repositório de desenvolvimento consome
as specs. Cada documento se sustenta sozinho, cita o commit exato que o
gerou, e termina sendo honesto sobre suas próprias fraquezas.
