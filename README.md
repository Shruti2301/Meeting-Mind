# MeetingMind

> *Your meetings, clarified.*

**MeetingMind** is a lightweight agentic AI tool that transforms messy meeting transcripts into structured, actionable intelligence — in seconds. Paste a transcript or speak directly into the app, and watch it extract action items, distill a sharp summary, and draft a professional follow-up email, all in one click.

Built on day one after graduation. Not for a job, not for a grade. For the love of building things that matter.

---

## What it does

MeetingMind runs your transcript through a 3-step AI agent pipeline:

**01 — Extract Action Items**

Identifies every task, assigns it to an owner, and sets a deadline. Rendered as a clean, scannable table.

**02 — Summarize**

Distills the entire meeting into 3 focused bullet points — key decisions made, blockers, and next steps.

**03 — Draft Follow-up Email**

Writes a warm, professional follow-up email ready to send to your team. Subject line included.

---

## Features

- 🎙️ **Voice input** — speak your transcript directly in the browser using the Web Speech API
- 📋 **Paste input** — drop in any raw transcript and analyze instantly
- ⚡ **3-step agentic pipeline** — powered by Claude (Anthropic)
- 📤 **One-click copy** — copy any output block with a single click
- 📱 **Fully responsive** — works beautifully on mobile and desktop
- 🎨 **Minimal, refined UI** — warm cream palette, Cormorant Garamond serif typography

---

## Tech stack

| Layer | Technology |
|---|---|
| Frontend | Vanilla HTML, CSS, JavaScript |
| AI | Claude API (Anthropic) — `claude-haiku-4-5` |
| Voice | Web Speech API (Chrome) |
| Deployment | Netlify |

No frameworks. No build step. No dependencies. Just a single `index.html` file.

---

## Getting started

### Run locally

```bash
git clone https://github.com/YOUR_USERNAME/meeting-agent.git
cd meeting-agent
open index.html
```

No server needed — open `index.html` directly in Chrome.

### Use it

1. Get a free API key from [console.anthropic.com](https://console.anthropic.com)
2. Paste your key into the API key field
3. Paste a meeting transcript — or hit **Record** and speak
4. Click **Analyze Meeting**
5. Copy your action items, summary, and follow-up email

---

## Example output

**Input transcript:**
```
Sarah: We need to finalize the landing page by Friday.
John: I can handle the copy once Priya sends the designs.
Priya: I'll have designs ready Wednesday EOD.
Sarah: Great. Also — three-tier pricing model approved for the investor call Tuesday.
Priya: I'll put together a one-pager by Monday.
Sarah: Perfect. Next sync Thursday 10am.
```

**Output — Action Items:**
| Owner | Task | By |
|---|---|---|
| Priya | Send landing page designs | Wednesday EOD |
| John | Write landing page copy | Friday |
| Priya | Create pricing one-pager | Monday |
| Sarah | Finalize landing page | Friday |

**Output — Summary:**
- Key decisions: Three-tier pricing model approved; landing page deadline set for Friday
- Blockers: John needs Priya's designs before completing copy
- Next steps: Priya delivers Wednesday EOD; team syncs Thursday 10am; investor call Tuesday

**Output — Follow-up Email:**
Ready-to-send email with subject line, decisions recap, action items, and warm closing.

---

## Why I built this

Startups waste hours every week on meeting follow-ups — chasing action items, writing recap emails, trying to remember what was actually decided. MeetingMind eliminates all of that in under 10 seconds.

I built the first version in a single evening, on day one after graduating, in San Carlos, CA. It's a small thing. But it works, it's useful, and it reminded me why I love building software.

---

## Roadmap

- [ ] Persistent history — save past meetings locally
- [ ] Export to Notion / Slack
- [ ] Multi-speaker detection
- [ ] Calendar integration — auto-create follow-up events
- [ ] Team mode — shared workspace for meeting notes

---

## Built by

**Shruti Mandaokar** — [LinkedIn](https://linkedin.com/in/shrutimandaokar) · [GitHub](https://github.com/Shruti2301)

---

*© 2026 Shruti Mandaokar · MeetingMind*
