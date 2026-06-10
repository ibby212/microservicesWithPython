# Module 4 — Reflection

**Team name**: _______________
**Branch**: `module-04/<team-name>`
**Submitted**: before Module 5 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

In Module 3, services called each other directly over HTTP. Now activity-service drops a message into a broker and moves on — it never waits for a reply.

**What does the activity-service gain by not waiting? And what does the notification-service gain by consuming at its own pace?**

Think about what happens under load, or when notification-service is temporarily down.

> *Your answer:* activity service gains the ability to move on quicky without waiting for notification service to respond. Under load, if thousands of activities are being logged, notification service doesn't become a bottleneck that slows down every single request. If notification service is temporarily down, the messages just queue up in RabbitMQ and get processed when it comes back up, no data is lost and no activity creation fails

---

## 2. Your choice

In Module 3 you already knew how to call another service directly over HTTP — you did it for user validation and game enrichment.

**Why not use the same approach for notifications? What does introducing a broker give you that a direct HTTP call doesn't?**

Think about what happens if notification-service is slow, or crashes mid-message.

> *Your answer:* A direct HTTP call to notification service would mean activity service is coupled to it aka if notification service is slow, the activity request slows down too. If it crashes mid-request, the notification is lost with no way to retry. The broker decouples them completely. The message sits in the queue until notification service is ready to consume it, and delivery is guaranteed regardless of whether the consumer is up at the time of publishing.

---

## 3. The tradeoff

With synchronous REST, you get an immediate answer: success or failure. With async messaging, the activity is saved and the message is sent — but you have no idea if the notification was ever delivered.

**How would a user know if their notification was never sent? How would you know as a developer?**

What visibility do you lose when you go async?

> *Your answer:* With synchronous REST you get an immediate success or failure response. With async messaging, activity service only knows the message was published to the queue, it has no idea if notification service actually processed it or if the user ever received the notification. As a developer you'd need to check the RabbitMQ management UI or add logging in the consumer to know if delivery failed. The user would have no idea at all, they'd just never see the notification.

---

*Keep this file. You will refer back to it during the oral presentation.*
