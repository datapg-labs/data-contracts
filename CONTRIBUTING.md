# Contributing

This repository is a shared codebase, worked on the way a data team works on one:
contracts live side by side, every change goes through a pull request, and teammates
review each other's work before it merges.

## How the repository is organised

```
reference/                  maintained contracts — read them, don't edit them
  ingestion_contracts/      one per table you can query
  product_contracts/
projects/                   learner contracts, one directory per project
  btc-daily-candles/
    README.md               Authors: @alice, @bob
    btc_daily_candles.yaml
```

- **`reference/`** is kept in shape for everyone. Only maintainers change it. Found a
  mistake in a reference contract? Open an issue.
- **`projects/<name>/`** belongs to the people on its `Authors:` line. Name a project
  after the dataset it describes (`btc-daily-candles`), not after a person.

## Start a project

```bash
git clone https://github.com/datapg-labs/data-contracts.git
cd data-contracts
git checkout -b btc-daily-candles
mkdir -p projects/btc-daily-candles
cp reference/ingestion_contracts/btc_prices.yaml projects/btc-daily-candles/btc_daily_candles.yaml
```

1. Add `projects/btc-daily-candles/README.md` with your handle on its `Authors:` line:
   `Authors: @your-github-user` — and say which dataset the contracts describe and who
   consumes it.
2. Edit the contract until it says what a consumer may rely on — see the README for
   what a good contract covers.
3. Commit, push your branch, and open a pull request.

If you have not accepted your `datapg-labs` invitation yet, fork the repository and
open the pull request from your fork — everything else is the same.

## Work on someone else's project

Projects are meant to be shared. To join one, open a pull request whose **only**
change adds your handle to that project's `Authors:` line. One of its authors reviews
it; once it merges you work on the project like any other author.

To suggest a change without joining, open an issue or comment on a pull request.

## Reviews

A pull request merges when it has:

1. **A peer review.** Ask a teammate — an author of the project, or whoever consumes the
   dataset. A contract is a promise to someone else, so the consumer's view matters most.
2. **A maintainer's approval.** Maintainers merge; you don't need to chase them.
3. **A passing scope check** (next section).

What a good review looks for:

- Does the contract match the real table? Check the columns and types in Hue.
- Are the guarantees ones the producer can actually keep — uniqueness, freshness,
  what may change?
- Would a consumer understand what each coded value means?
- No credentials, tokens, keys, or `.env` files. Not even fake-looking ones.

Expect comments on your pull requests; they are meant to teach, not to reject.

## The scope check

An automated check runs on every pull request. It fails, and says exactly which file
and why, when a pull request:

- changes anything outside `projects/` — `reference/`, the docs, `.github/` — unless
  you are a maintainer
- changes a project you are not an author of (joining, as above, is the exception)
- adds a project without a `README.md` that lists you on its `Authors:` line
- adds a credentials file (`.env`, `*.pem`, a private key) or a line that looks like a
  hard-coded password, token or key

## Clone locally, with your own GitHub account

**Do not use the browser-based VS Code on the platform for git work.** It is a
shared workspace. Pushing from it would mean putting your GitHub credentials
somewhere other people can reach, and any commit you made would be attributed to
whoever set the workspace up. Clone to your own machine, with your own identity.

## CI

Workflows run on **GitHub-hosted runners** only, and live in `.github/`, which
maintainers look after. Never add `runs-on: self-hosted` — a pull request that does
will be closed.
