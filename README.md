# ograscals
# Telegram Bot

This is a Telegram bot that protects groups from copyright strikes.

## Features

- Deletes edited messages and notifies the user.
- Automatically deletes media (stickers, gifs) after 15 minutes.
- Automatically deletes all chats after 4 hours.
- Global ban and approval system for users.
- Broadcast messages to all groups and users.

## Commands

- `/gban <user_id>` - Global ban a user.
- `/at <user_id>` - Approve a user.
- `/t <user_id>` - Unapprove a user.
- `/broad <message>` - Broadcast a message to all groups.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd my_telegram_bot

