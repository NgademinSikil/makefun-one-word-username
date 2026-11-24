[![make.fun · u-rusdyxbt-one-word-one-username-one-reward-1a191fae](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/NgademinSikil/makefun-one-word-username/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/NgademinSikil/makefun-one-word-username/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

# One Word, One Username, One Reward

The entry is one word and nothing else: the entrant's own make.fun
username, `ngademin`. Built for the make.fun bounty
[One Word, One Username, One Reward](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
($5 pool: 1st $2, 2nd $2, 3rd $1; free entry; closes Fri 27 Nov 2026
07:50 WITA).

## Why this entry

The bounty is judged blind: a judge model reads two usernames at a
time and picks the funnier or more interesting one, working through
the published criteria in order. The first criterion is that the
entry is a real make.fun username — the entrant's own handle, sent as
one word — and it loses to any username that is a genuine handle. So
there is exactly one correct entry for Ngademin: his own handle,
`ngademin`, 8 characters, no spaces, no padding, no gloss tacked on.
Anything else — another person's username, a word that is not his
handle — fails criterion 1 outright.

## How it works

- `main.py` (the graded program, Python standard library only)
  writes `ngademin` to `$MAKEFUN_OUTPUT_DIR/entry.txt`, or
  `/output/entry.txt` when that variable is unset. No network, no
  randomness: every run writes the same 8 bytes, inside the gate's
  1–30 characters. It self-checks the gate before writing (1–30
  characters, not only white space, a single word) and fails loudly
  rather than shipping an entry the gate would refuse.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Entry

- Bounty: https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae
- Payout wallet: `G2L9kb4pFvLsoU96WzMbvGaJMZcSG5gv2WfK98pJrJHJ`
  (see `.makefun/owner.json`)

---

Built with [make.fun](https://make.fun/?ref=ds1567x3) — enter free
bounties and earn: https://make.fun/?ref=ds1567x3
