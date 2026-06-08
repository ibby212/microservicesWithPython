# Module 3 — Reflection

**Team name**: ibaad
**Branch**: `module-03/ibaad`
**Submitted**: before Module 4 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

All client requests now go through the gateway. No client ever calls a service directly.

**Why does that single entry point exist? What would the client's life look like without it?**

Think about what the client would need to know and manage if it talked to each service on its own port.

> *Your answer:* The gateway exists so the client only needs to know one address. Without it, the frontend would have to hardcode the port for every service, user-service on 8001, game-service on 8002, activity-service on 8003. The moment any service moves to a different machine or port, the client breaks. The gateway absorbs all of that complexity and the client never needs to know what's behind it.

---

## 2. Your choice

The activity-service makes two outbound calls: one to validate the user (with retry logic), one to fetch game data (with a null fallback if it fails).

**Why are these two calls treated differently? Why does one retry and the other just give up gracefully?**

What is the consequence for the user in each case if the downstream service is unavailable?

> *Your answer:* The two calls have different consequences if they fail. User validation is load bearing, if you skip it or let it fail silently, you end up saving activities for user IDs that don't exist, which corrupts the data and breaks anything that relies on it downstream. That is why it retries once before giving up. The game enrichment is decoration. The activity happened regardless of whether game service is reachable. Blocking the whole request on optional data would mean a failing game service kills a core feature. Returning "game": null keeps the system working for the user even when a dependency is down.

---

## 3. The tradeoff

Every time a client creates an activity, three services are involved synchronously. They all have to be running, healthy, and fast.

**What is the systemic risk of chaining synchronous calls like this?**

What happens to the user experience if the slowest service in the chain takes 3 seconds to respond?

> *Your answer:* When calls are chained synchronously, latency and failures stack. If validate_user takes 1 second and fetch_game takes 1 second, the user waits at least 2 seconds before getting a response, and that is before network overhead. If the slowest service in the chain takes 3 seconds, the user feels all 3 of those seconds on every single request. And if any service in the chain goes down entirely, the request fails even though the other services are healthy. The more services you chain, the more ways there are for a single request to go wrong.

---

*Keep this file. You will refer back to it during the oral presentation.*
