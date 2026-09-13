# Конспекты лекций

Репозиторий с конспектами, транскрипциями, исходными аудиозаписями,
фотографиями и учебной литературой.

## Структура

```text
.
├── lectures/
│   └── 2026-09-12/
│       ├── notes.tex
│       ├── notes.pdf
│       ├── transcript.md
│       └── assets/
│           ├── audio/
│           └── images/
└── references/
```

## Лекции

| Дата | Тема | Материалы |
|---|---|---|
| 12.09.2026 | Свёртки на группе $\mathbb{Z}_n$ | [Папка лекции](lectures/2026-09-12/) |

## Сборка LaTeX

Из папки соответствующей лекции:

```bash
latexmk -pdf -interaction=nonstopmode notes.tex
```

Если `latexmk` недоступен, документ можно дважды собрать командой:

```bash
pdflatex -interaction=nonstopmode notes.tex
pdflatex -interaction=nonstopmode notes.tex
```

Для сборки нужны стандартные пакеты LaTeX, включая `amsmath`, `babel`,
`geometry`, `hyperref` и `tikz`.

