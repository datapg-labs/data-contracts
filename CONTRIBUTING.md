# Contributing

Everything reaches `main` through a pull request, and every pull request is reviewed
before it merges. A contract is a promise to someone else, so contract changes are
reviewed more carefully than code.

## Join the Discord

**[datapg.dev/discord](https://datapg.dev/discord)** is where the community lives. Ask
there when you are stuck, find the team that produces or consumes the data you are
describing, and post your pull request when it is ready for review. Never paste
credentials into Discord.

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

Nobody pushes to `datapg-labs` directly — every change arrives from a **fork**.

1. Fork the repository on GitHub (the **Fork** button, top right), then clone your fork:

   ```bash
   git clone https://github.com/<your-github-user>/data-contracts.git
   cd data-contracts
   git remote add upstream https://github.com/datapg-labs/data-contracts.git
   git checkout -b pgxxxx-orders-contract
   cp ingestion_contracts/btc_prices.yaml ingestion_contracts/pgxxxx_orders.yaml
   ```

2. Edit the contract until it says what a consumer may rely on — see the README for what
   a good contract covers.
3. Commit, push the branch to your fork (`git push -u origin pgxxxx-orders-contract`), and
   open a pull request into `datapg-labs/data-contracts`. Say which project produces the
   data and who consumes it.

Before you start something new, bring your fork up to date — **Sync fork** on GitHub, or
`git fetch upstream && git switch main && git merge --ff-only upstream/main`.

Writing the contract for a project a team is building? Ask for collaborator access to their
fork, or open your own pull request here and link theirs.

## Reviews and merging

A pull request merges once a member of the **reviewers** team approves it — someone other
than the author. Automated checks run on every pull request; on your first one they wait
until a maintainer approves the run — GitHub does that for every new contributor.

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
people can reach. Clone your fork to your own machine, with your own identity.

## CI

Workflows run on **GitHub-hosted runners** only. Never add `runs-on: self-hosted` — a
pull request that does will be closed.
