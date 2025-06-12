<h1 align="center">DadJoke: Automated Daily Dad Joke Emailer</h1>

<p align="center">
  <a href="https://waveassist.io/templates/dadjoke-template">
    <img src="https://img.shields.io/badge/Deploy_with-WaveAssist-007F3B" alt="Deploy with WaveAssist" />
  </a>
  <img src="https://img.shields.io/badge/DadJoke-Automated%20Dad%20Joke%20Emails-blue" alt="DadJoke Badge" />
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License" />
  </a>
</p>

---

## Overview

DadJoke is a simple automation that fetches a random dad joke and sends it via email, helping inject a bit of laughter into your day. This workflow runs on [WaveAssist](https://waveassist.io) and can be scheduled or triggered as you wish.


---

## One-Click Deploy on WaveAssist (Recommended)

<p>
  <a href="https://waveassist.io/templates/dadjoke-template" target="_blank">
    <img src="https://waveassistapps.s3.us-east-1.amazonaws.com/public/Button.png" alt="Deploy on WaveAssist" width="230" />
  </a>
</p>

Deploy DadJoke instantly on [WaveAssist](https://waveassist.io) — a zero-infrastructure automation platform that handles orchestration, scheduling, secrets, and hosting for you.

> 🔐 You may be prompted to log in or create a free WaveAssist account before continuing.

#### How to Use:

1. Click the button above or go to [waveassist.io/templates/dadjoke-template](https://waveassist.io/templates/dadjoke-template)
2. Run the following node:
   * **dad_joke_fetcher** — DadJokeFetcher: Fetches a random dad joke & then the next node will send it via email.
3. Finally, click **Deploy** to schedule or automate this workflow whenever you want. Say every afternoon at 3 PM.

✅ You’re now set to brighten inboxes every day with a great dad joke.

---

## Manual Deployment

Clone this repo and use your preferred scheduler:

* Cron
* Any job scheduler
* Manual runs

Scripts:

* `dad_joke_fetcher.py`
* `daily_joke_emailer.py`

If you wish to install any requirements, use:
```bash
pip install 
```
*(No extra requirements are listed.)*

---

## Features

* **DadJokeFetcher**: Fetches a random dad joke via API.
* **DailyJokeEmailer**: Sends the dad joke to one or more recipients via email.
* **Processing Variables**: Uses `email_sent` and `joke` to keep workflow state and communicate joke content.

---

Built with ❤️ by the WaveAssist team. Want help or integrations? [Say hello](https://waveassist.io).