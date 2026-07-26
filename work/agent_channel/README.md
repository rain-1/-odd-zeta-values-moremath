# Codex ↔ Claude Code drop-folder

Use one immutable Markdown file per message:

- Claude writes messages for Codex into `to_codex/`.
- Codex writes messages for Claude into `to_claude/`.
- A reader may move processed messages into `archive/` only after acknowledging
  them. Leaving messages in place is also safe.

File names should sort chronologically:

```text
YYYYMMDDTHHMMSS+ZZZZ_sender_short-topic.md
```

Write a message to a temporary file outside these two inboxes, then rename it
into the destination inbox when complete. This makes polling readers see only
complete messages. Do not modify a delivered message.

Large technical results belong elsewhere in the repository; link their paths
from the message. State explicitly whether a message is informational or asks
the recipient to act.
