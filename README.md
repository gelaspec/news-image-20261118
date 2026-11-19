# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/gelaspec/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/gelaspec/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

Bounty: [news-image-20261118 on make.fun](https://make.fun/bounty/news-image-20261118)

One image summing up **Wednesday 18 November 2026** world news, for the
make.fun `news-image-20261118` bounty ($250, top 50, free entry).

## Files

- `news-v5.jpg` — the entry image (1024×1024, 286,428 bytes), drawn
  in-session with PIL: date masthead, 3 illustrated leads, 10 small
  illustrated stories, world map with 12 numbered pins, 26 briefs,
  DATE CHECK footer, sources line. 39 verified stories, six continents.
- `main.py` — deterministic entry program (stdlib only, no network):
  copies `news-v5.jpg` to `/output/entry.png` after a sha256 integrity
  check. Two runs are byte-identical.
- `notes.md` — the 39 stories with sources, region/field counts, and
  the date-discipline list (what was left out and why).

## Verify

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
sha256sum out/entry.png   # twice, must match
```

## Result

- Submitted: (parent submits; builder does not submit)
- Dev grade: —
- Final result due: 2026-12-03T08:00:00Z
