# data-contracts

The agreement between whoever produces a dataset and whoever consumes it: what the fields
are, what they mean, what may change, and who to ask.

A contract is the thing that stops "someone renamed a column" from being discovered by a
broken dashboard on a Monday morning.

## Why this repo exists separately

Contracts outlive the pipelines that implement them. A producer may be rewritten three
times while the promise it makes to consumers stays the same. Keeping them apart makes
that distinction visible, and makes a change to a contract a deliberate, reviewed act
rather than a side effect of editing a model.

## Layout

```
ingestion_contracts/     one contract per ingested topic or table
product_contracts/       one contract per data product
```

`ingestion_contracts/` already covers every table in the three shared schemas
(`crypto_currencies_raw`, `synsap_finance_raw`, `fin_internal_jde`). Read those first, and
copy the closest one as the starting point for your own.

**Recommended:** every ingestion in [`ingestion`](https://github.com/datapg-labs/ingestion)
and every project in [`data-products`](https://github.com/datapg-labs/data-products) gets a
contract here.

## What a good contract says

The schema is the easy part. The parts people skip are the ones that matter:

- **Ownership** — a name, not a team alias nobody reads
- **Guarantees** — freshness, completeness, uniqueness. What a consumer may rely on
- **What is allowed to change** — additive columns are usually fine; renames and type
  changes are not, without notice
- **Semantics** — what does `status = 'C'` actually mean? This is where most real
  confusion lives, and almost no schema captures it

A contract that only lists column names and types has not said anything a `DESCRIBE`
would not.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).
