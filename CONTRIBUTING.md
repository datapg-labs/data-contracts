# Contributing

Everything reaches `main` through a pull request, and every pull request is reviewed
before it merges. A contract is a promise to someone else, so contract changes are
reviewed more carefully than code.

## Where things go

```
ingestion_contracts/     one contract per ingested topic or table
  btc_prices.yaml
  pgxxxx_orders.yaml     yours: named after the topic it describes
product_contracts/       one contract per data product
```

## Recommended: a contract for every ingestion

Every producer script and source connector in
[`ingestion`](https://github.com/datapg-labs/ingestion) should have a contract here for the
topic it writes, and every project in
[`data-products`](https://github.com/datapg-labs/data-products) one for what it publishes.
Link the contract from the project's README, and the project from the contract's
description.

## The flow

```bash
git clone https://github.com/datapg-labs/data-contracts.git
cd data-contracts
git checkout -b pgxxxx-orders-contract
cp ingestion_contracts/btc_prices.yaml ingestion_contracts/pgxxxx_orders.yaml
```

1. Edit the contract until it says what a consumer may rely on — see the README for what
   a good contract covers.
2. Commit, push your branch, and open a pull request. Say which project produces the data
   and who consumes it.

If you cannot push branches to `datapg-labs`, fork the repository and open the pull
request from your fork; everything else is the same.

## What a review looks for

- Does the contract match the real topic or table? Check the fields and types.
- Are the guarantees ones the producer can actually keep — uniqueness, freshness, what
  may change?
- Would a consumer understand what each coded value means?
- Does it only change its own contract? Changing a contract someone else relies on needs
  a reason in the pull request.
- No credentials, tokens, keys, or `.env` files. Not even fake-looking ones.

Expect comments; they are meant to teach, not to reject.

## Clone locally, with your own GitHub account

**Do not use the browser-based VS Code on the platform for git work.** It is a shared
workspace. Pushing from it would mean putting your GitHub credentials somewhere other
people can reach. Clone to your own machine, with your own identity.

## CI

Workflows run on **GitHub-hosted runners** only. Never add `runs-on: self-hosted` — a
pull request that does will be closed.
