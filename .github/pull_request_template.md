<!-- path: .github/pull_request_template.md -->

## Artefato

<!-- Marque o que este PR produz ou evolui. Um PR carrega um artefato. -->

- [ ] Study (`studies/`)
- [ ] System design (`docs/system-design/`)
- [ ] Spec (`docs/specs/`)
- [ ] Roadmap (`docs/roadmap/`)
- [ ] ADR (`docs/adr/`)
- [ ] Nenhum (devops, plumbing, refactor de templates/skills)

## Resumo

<!-- 1-3 bullets: o que muda e por quê. Foque no "porquê", o "o quê"
     fica claro pelo diff. -->

-
-

## Como verificar

<!-- Passos concretos pra revisão. Para artefatos da cadeia, aponte a
     seção crítica e a auto-crítica. Para devops/plumbing, comandos. -->

```sh
# exemplo
pre-commit run --all-files
```

## Checklist

- [ ] Todo `.md` novo/movido começa com `<!-- path: ... -->`.
- [ ] `pre-commit run --all-files` passou limpo localmente.
- [ ] Se for artefato da cadeia: a seção **Self-critique** está
      preenchida e é honesta (parte mais frágil, o que não foi
      validado, o que mudaria a conclusão).
- [ ] `references/` intocado; pin não bumpado sem intenção explícita
      (bump é seu próprio commit, com uma linha de motivo).
- [ ] Documento publicado (system-design / spec / ADR) se sustenta
      sem ler o study ou a reference por trás.
