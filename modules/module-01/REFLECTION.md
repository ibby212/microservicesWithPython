## YOU NEED TO COMMIT THIS FILE BEFORE MOVING ON TO THE NEXT MODULE ! 🚨

**feel free to delete this comment**

# Module 1 — Reflection

**Team name**: **\*\***\_\_\_**\*\***
**Branch**: `module-01/<team-name>`
**Submitted**: before Module 2 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

You started from a painful monolith. Now you're splitting it into separate services.

**What concrete problem does that split solve: and for whom?**

Think about it from three angles: the developer who has to change code, the team that has to deploy it, and the user who has to live with its failures. You don't need to cover all three, pick the one that felt most real to you today.

> _Your answer:_ In the monolith, one restart takes everything down, login, feed, notifications, all of it. A fix to the game catalogue means the user has no platform at all for however long the restart takes. That's not a code problem, it's a UX problem and a reliability problem. Splitting into services means failures stay contained. If notification-service crashes, users can still log games and see their feed. The attack surface shrinks.

---

## 2. Your choice

Look at your service map. Every arrow between two services is a decision someone made.

**Pick one boundary, one place where you decided service A should not be part of service B. Explain why that line exists.**

What would break, slow down, or become harder to manage if you merged those two services back together?

> _Your answer:_ I kept activity-service separate from game-service. A game is catalogue data aka it describes what exists. An activity is user behaviour aka it describes what someone did. If you merge them, game-service becomes responsible for tracking user behaviour, building feeds, and firing notifications. That's too much. Changes to how the feed works would require touching the same service as changes to the game catalogue, which means more risk, more coordination, more reasons for things to break.

---

## 3. The tradeoff

Microservices solve the monolith's problems. But they create new ones.

**Name one thing that was simpler in the monolith and is now harder in your distributed design.**

No need to solve it: just name it honestly. This is exactly the tension the rest of the course is about.

> _Your answer:_ In the monolith, calling a function was one line. Activity logic could grab a username directly from memory. Now activity-service has to ask user-service over HTTP, handle the case where it's slow, handle the case where it's down etc.

---

_Keep this file. You will refer back to it during the oral presentation._
