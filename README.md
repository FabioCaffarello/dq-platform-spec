<!-- path: README.md -->

# DQ Platform Spec

A spec-authoring workspace. You read a pinned **reference**
([`dq-platform`](https://github.com/FabioCaffarello/dq-platform)) and
distill it into the documents that guide real development.

```text
study → system-design → spec → roadmap
```

Low ceremony, high quality. There are no gates and no acceptance-criteria
rituals. Quality comes from good templates that make you think about the
right things, and from every document ending in an honest self-critique.

## The planes

- **`references/`** — vendored upstream material, pinned by a lockfile.
  Content is git-ignored; the lockfile is versioned. Read-only.
- **`studies/`** — learning extracted from the reference. Scaffolding.
- **`docs/system-design/`** — architecture. The first published plane.
- **`docs/specs/`** — buildable specs handed to implementers.
- **`docs/roadmap/`** — specs sequenced into a plan.
- **`docs/adr/`** — the rare decision durable enough to record formally.
- **`templates/`** + **`.claude/skills/`** — the shape and the craft for
  each artifact type.

## Quick start

```sh
make refs-sync      # hydrate references/dq-platform/ at the pinned commit
make refs-status    # pin vs. what's on disk
make help           # all targets
```

Then open Claude Code or Codex here and run a command:

```text
/study <topic>          # read the reference, extract learning
/system-design <topic>  # turn learning into architecture
/spec <topic>           # turn a design slice into a buildable spec
/roadmap                # sequence the specs
```

See **[`BOOTSTRAP.md`](BOOTSTRAP.md)** for the full walk-through and
**[`CLAUDE.md`](CLAUDE.md)** for the operating guide.

## Qualidade local

Travas leves rodam antes de cada commit. O CI (`.github/workflows/ci.yml`)
espelha exatamente esses hooks em todo PR e push para `main`, então
local e servidor nunca divergem. Sem rituais de revisão extra.

```sh
pre-commit install --hook-type pre-commit --hook-type commit-msg
pre-commit run --all-files
```

Os hooks cobrem markdown (`markdownlint-cli2` com config própria em
`.markdownlint.yaml`), higiene de arquivos (trailing whitespace,
final-of-file, YAML válido, sem marcadores de merge), a regra do
path-header do `CLAUDE.md` (todo `.md` começa com `<!-- path: ... -->`),
e a integridade de `references/*.lock`.

Mensagens de commit seguem [Conventional Commits][cc] e são validadas
pelo hook `commit-msg` (`commitlint`). Exemplos:

```text
feat: add roadmap template
fix(refs-sync): handle missing lockfile
chore(devops): bootstrap pre-commit gates
```

`markdownlint-cli2` e `commitlint` precisam de Node disponível no PATH
(o `pre-commit` cuida do resto, instalando os pacotes em
`~/.cache/pre-commit/`).

Além do pre-commit, o CI também roda um verificador de links (lychee)
nos `.md` versionados — links internos quebrados falham o build,
externos são apenas warning.

[cc]: https://www.conventionalcommits.org/
