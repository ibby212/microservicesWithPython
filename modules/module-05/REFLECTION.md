# Module 5 — Reflection

**Team name**: _______________
**Branch**: `module-05/<team-name>`
**Submitted**: before Module 6 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

The game-service now has two models for the same data: SQLite for writes, Redis for reads. They store the same games in two different shapes.

**Why go through the trouble of maintaining two representations of the same data?**

Think about what kind of queries each model is optimised for, and what would happen if you tried to use the write model for high-traffic read operations.

> *Your answer:* SQLite is optimised for writes and accurate reads, it handles complex queries, joins, and transactions well but is slower under high read traffic. Redis is an in-memory store that can serve thousands of reads per second with microsecond latency. If every game summary request hit SQLite, the database becomes a bottleneck as traffic scales.

---

## 2. Your choice

The logging-service checks GDPR consent before recording any activity. If a user has not opted in, the log is silently dropped.

**What does this consent check force you to accept about your data?** It is incomplete by design — some activities will never be recorded.

From a system design perspective: where is the right place to enforce this rule — in the logging-service, in the activity-service, or at the gateway? Why?

> *Your answer:* he consent check forces you to accept that your data is intentionally incomplete, users who haven't opted in simply don't appear in the logs, and that's correct behaviour, not a bug. The right place to enforce this is in the logging service, not at the gateway or in activity service. The gateway doesn't know what data is being logged or for whom. Activity-service shouldn't need to know about GDPR rules, that's not its responsibility. The logging-service is the one writing the data, so it's he only service that can make the decision about whether writing is permitted.

---

## 3. The tradeoff

With CQRS, your write model and read model can drift out of sync — a game is updated in SQLite but the Redis projection still shows the old data.

**In what scenario does this inconsistency matter to the user? In what scenario is it completely acceptable?**

Is there a class of applications where eventual consistency is never acceptable? What are they?

> *Your answer:* The inconsistency matters when a user updates something and immediately tries to read it back, they'd see stale data in the summary endpoint and think the update didn't work. It's completely acceptable for data that changes rarely and where exact freshness doesn't matter, like a game's cover image or genre. Applications where eventual consistency is never acceptable include financial systems, bank balances, payment confirmations, and stock trades all require the read model to reflect the latest write immediately. A user seeing a stale account balance after a transfer is not acceptable

---

*Keep this file. You will refer back to it during the oral presentation.*
