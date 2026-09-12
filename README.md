# data-contracts

The agreement between whoever produces a dataset and whoever consumes it: what
the fields are, what they mean, what may change, and who to ask.

A contract is the thing that stops "someone renamed a column" from being
discovered by a broken dashboard on a Monday morning.

## Why this repo exists separately

Contracts outlive the pipelines that implement them. A producer may be rewritten
three times while the promise it makes to consumers stays the same. Keeping them
apart makes that distinction visible, and makes a change to a contract a
deliberate, reviewed act rather than a side effect of editing a model.

## Layout

```
_template/contract.yml     copy this
<your-pg-id>/
  my-dataset.yml
```

## What a good contract says

The schema is the easy part. The parts people skip are the ones that matter:

- **Ownership** — a name, not a team alias nobody reads
- **Guarantees** — freshness, completeness, uniqueness. What a consumer may rely on
- **What is allowed to change** — additive columns are usually fine; renames and
  type changes are not, without notice
- **Semantics** — what does `status = 'C'` actually mean? This is where most real
  confusion lives, and almost no schema captures it

A contract that only lists column names and types has not said anything a `DESCRIBE`
would not.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Contracts are reviewed more carefully
than code, because changing one is a promise to someone else.
