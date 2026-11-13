# ANVI Analytics integration preparation

Repository: `undefined-jaat-cmd/Smart_Calculator`
Detected stack hints: Python

## Added files
- `anvi_analytics_client.py`: dependency-free event sender.
- This guide.

## Tracking is not active yet
ANVI cannot obtain historical users, messages, or commands from GitHub source code. This PR does not modify your Telegram polling or webhook configuration and does not silently change bot handlers.

After reviewing and merging this PR:
1. Create an ANVI project in your dashboard and copy its API key (shown once).
2. Add `ANVI_API_KEY` as a secret in your hosting provider. Never commit it.
3. Set `ANVI_ENDPOINT` to your ANVI deployment URL plus `/api/v1/events`.
4. Add `track(...)` calls at the event points you want measured.

Example: `from anvi_analytics_client import track` then `track("command:start", user_id=telegram_user_id)`.

Keep your existing Telegram webhook/polling setup unchanged. Do not share your Telegram bot token with ANVI.
