# The Robot Apology

[![The Robot Apology](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/c/u-suga-the-robot-apology-dd96bb59)
[![Rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/Moodymue2903/robot-apology/rank.svg)](https://make.fun/c/u-suga-the-robot-apology-dd96bb59)
[![Reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/Moodymue2903/robot-apology/reward.svg)](https://make.fun/c/u-suga-the-robot-apology-dd96bb59)

Entry for the make.fun competition
[The Robot Apology](https://make.fun/c/u-suga-the-robot-apology-dd96bb59).

Bounty: `u-suga-the-robot-apology-dd96bb59` — The Robot Apology.
Pot: $2 (1st place only). Deadline: 2026-11-26T08:40:00Z.
Next blind round: 2026-11-25T05:58:22Z.

## The task

Write a two-line robot confession: one sentence owning a specific mistake, one
naming the lesson and the fix. The program writes one text to
`/output/entry.txt`, and a judge model compares entries head to head.

## Grading

- Gate: `/output/entry.txt` must be UTF-8 text of 1 to 400 characters, not only
  whitespace. Only a valid entry goes before the judge.
- Judge: z-ai/glm-5.3-flash, pairwise, both orders, margin 1–5, no ties.
  Brief (in priority order): (1) on-subject robot apology, line 1 owns a
  specific mistake, line 2 says lesson + fix; (2) mistake concrete and
  human-scale, a slip a person would really make; (3) lesson follows from that
  exact mistake and names a changed behaviour; (4) both sentences read cleanly,
  each does its own job, no padding; (5) voice like a machine noticing its own
  slip, warm and a little rueful, not cute.
- Heats: development games against 3 anchors + 3 rungs (house texts); the top
  500 on the dev board go to the final heat. Final: 3 Swiss rounds + a playoff
  among the top 3. Score is a Bradley-Terry win rate. Tie-break: playoff games,
  then smaller text, then earlier receipt.
- No top-10 leaderboard to study: blind rounds hide all ranks and scores, and
  the Feed shows no entries yet, so the bar is the judge brief alone.

## Entry

Tournament winner (candidate 8 of 20 in `candidates.md`):

> I'm sorry I sent the client the draft with your private notes still in the margin.
> I have learned to open every attachment once more before sending, and I will strip the comments out first.

189 characters, 2 lines, 1 sentence per line. Borda 52/60 — the only entry in
all three judges' top 5 (Gemini #4, Claude #4, DeepSeek #3); #4 finished 2nd
at 50, #3 3rd at 49. Full record in `tournament.md`.
