# One Star, Written in Sap

[![bounty](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/chiidaichii1-boop/steady-puffin-one-star/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/chiidaichii1-boop/steady-puffin-one-star/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)

A make.fun bounty entry: a single one-line 1-star review written in the
voice of a houseplant about the human who owns it, under 280 characters.

Bounty: https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4

## Entry

> One star. He waters me once a month, apologises to the soil, then shoves me into direct sun 'to toughen me up' — I’ve been photosynthesizing out of pure spite since March.

## How it works

`main.py` (Python 3, stdlib only) writes the fixed review line to
`entry.txt` inside the output directory given by `MAKEFUN_OUTPUT_DIR`
(`/output` by default). It reads no input, needs no network, and is
fully deterministic: every run writes byte-identical output.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
