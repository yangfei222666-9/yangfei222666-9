<h1 align="center">Yang Fei — Building TaijiOS</h1>

<p align="center">
  <strong>TaijiOS</strong> is a hexagram-guided reliability and learning runtime for AI agents.
</p>

<p align="center">
  <strong>Not fortune-telling. Life engineering.</strong>
</p>

<p align="center">
  It turns event flow, rollback, learning gates, and auditable agent evolution into reusable infrastructure for vertical decision engines. <strong>zhuge-skill</strong> is the first public case: football prediction built on a 64-hexagram reasoning structure.
</p>

<p align="center">
  <a href="https://github.com/yangfei222666-9?tab=followers"><img src="https://img.shields.io/github/followers/yangfei222666-9?label=Follow&style=social" alt="GitHub followers"/></a>
  <a href="https://taijios-hud.netlify.app"><img src="https://img.shields.io/badge/HUD-Live%20Demo-00d1b2" alt="HUD demo"/></a>
  <a href="https://taijios-cyberpet.netlify.app"><img src="https://img.shields.io/badge/CyberPet-Live%20Demo-ff3860" alt="CyberPet demo"/></a>
</p>

<p align="center">
  <a href="https://taijios-hud.netlify.app">
    <img src="./assets/taijios-proof-card.svg" alt="TaijiOS execution proof card: first 60-day snapshot, 14 modules, 346 heartbeats, 12/12 LLM gateway tests, 70,748 lines of code, 2 live demos" width="100%" />
  </a>
</p>

---

## 👋 关于我 / About

> Independent builder of TaijiOS. The current focus is not a broad "AI OS" claim, but a smaller engineering target: event flow, reliability, rollback, learning gates, and auditable agent evolution.
>
> 中文：当前重点不是继续扩大概念，而是把 TaijiOS 收口成可运行、可验证、可回滚、可复盘的 AI Agent 可靠性系统。

---

## ⚡ 执行密度 / Build Velocity

```
First 60-day build snapshot, starting 2026-02-17
                    ↓
           ✅ 14 modules live (1 🔄 in progress)
           ✅ Ising Heartbeat · 346 heartbeats · 18.8h physics experiment
           ✅ LLM Gateway · 12/12 extreme-scenario tests passed
           ✅ zhuge-skill published to 3 platforms (GitHub + ClawHub + Xiaping)
           ✅ 2 live Netlify demos (HUD + CyberPet)
           ✅ release repo · 48 commits · 70,748 LoC (8-day consolidation)
```

**$0 budget · 0 team · first 60-day snapshot · 70,748 LoC · 14 modules · 1 phase transition observed.**

This README is part of TaijiOS dogfooding: it was co-drafted with Claude Opus 4.7 from real commit logs, then personally verified by me. I own every claim and every word.

Numbers are project snapshots, not marketing claims. Verify the latest state from each repository before citing.

---

## 🚀 Current Release / 当前入口

Start with **[self-improving-loop v0.1.1](https://github.com/yangfei222666-9/self-improving-loop/releases/tag/v0.1.1)**.

It is the smallest reusable slice of TaijiOS: a hexagram-guided reliability layer for AI agents that records execution traces, maps runtime signals into six engineering lines, applies guarded policy patches, and rolls back on regression.

中文：如果你只想看一个能直接安装、能验证、能复用的入口，先看 `self-improving-loop v0.1.1`。它不是完整 TaijiOS，而是从 TaijiOS 拆出来的 AI Agent 可靠性与回滚层。

---

## 🌀 Core Projects

This profile is the portfolio entrance. Start here, then follow the repo that matches your use case:

| Project | What | Language |
|---|---|---|
| **[taiji](https://github.com/yangfei222666-9/taiji)** | Current main repo — hexagram-guided reliability/runtime system, live HUD, five-engine architecture | Python |
| **[self-improving-loop](https://github.com/yangfei222666-9/self-improving-loop)** | Standalone reliability layer — v0.1.1 released; trace failures, apply guarded changes, and rollback on regression | Python |
| **[zhuge-skill](https://github.com/yangfei222666-9/zhuge-skill)** | First vertical case — 64-hexagram reasoning for football prediction | Python |
| **[taijios-bundle](https://github.com/yangfei222666-9/taijios-bundle)** | Installer / release snapshot / local trial bundle | Python |
| **[TaijiOS](https://github.com/yangfei222666-9/TaijiOS)** | Archived legacy prototype; current main development is `taiji` | Python |
| **[TaijiOS-Lite](https://github.com/yangfei222666-9/TaijiOS-Lite)** | Archived lite prototype / example pack; reusable ideas move into `taiji` | Python |

---

## 🧊 Shared Crystal Pool

**[zhuge-crystals](https://github.com/yangfei222666-9/zhuge-crystals)** is the public collaboration surface behind `zhuge-skill`: a sanitized, PR-reviewed decision-crystal pool.

Current public state:

- Public pool file: `crystals.jsonl`
- Privacy rule: whitelist schema only; no user IDs, team names, timestamps, raw odds, API keys, or free-text notes
- Contribution model: local users sanitize crystals, then submit a PR for maintainer review
- Public entries at last profile update: `0` — the infrastructure exists; the next traction target is the first valid sanitized PR

---

## 🛠 Stack

`Python 3.12` · `FastAPI` · `SQLite` · `pyautogui` · `Whisper` · `edge-tts` · `Telegram Bot API` · `Lark / Feishu SDK`

Runs on a multi-LLM gateway with failover across 12 providers:
`Claude` · `GPT` · `Gemini` · `DeepSeek` · `Kimi` · `Qwen` · `ZhipuAI` · `Doubao` · `Yi` · `Baichuan` · `MiniMax`

---

## 🔬 Technical Highlights

- **Five-engine architecture** — each engine has a constrained engineering role: recovery, scheduling, experience learning, situational awareness, or persona switching.
  `震 Zhen` = only recovery · `师 Shi` = only scheduling · `颐 Yi` = only experience learning · `乾 Qian` = situational awareness · `随 Sui` = persona switching.
- **Ising Heartbeat** — maps six system dimensions into 64 hexagram states; the 346-heartbeat experiment observed a phase transition and stable-state lock-in.
- **Safe Click (4 gates)** — default-deny RPA click executor: window-binding + region-blacklist + whitelist + OCR-confidence.
- **Self-Improving Loop** — standalone reliability package: feedback, guarded strategy, and rollback separated from the main repo.

---

## 💬 Philosophy

> *任何学说，都只是你的片面镜子。完整的镜子早在你心里 — 我们只是造工具让你看见它。*
>
> *Any school of thought is just a partial mirror of you. The complete mirror is already inside you — we just build the tools to let you see it.*
>
> — from the **ICI protocol**

## TaijiOS Wedge

TaijiOS is infrastructure for building vertical 64-hexagram decision engines on top of the ICI protocol. The core idea: map messy real-world signals into auditable six-line state transitions, then use reliability gates, rollback, and learning loops to make the decision process inspectable instead of mystical.

`zhuge-skill` is the first public vertical case: football prediction. The next cases can be any domain where decisions are high-context, evidence-heavy, and hard to audit — finance, operations, healthcare, law, or founder decision support.

---

## 🤝 How to Collaborate

**If you're an investor** — what is verifiable at this stage: 14 production modules in 60 days as a solo builder, 5 shipped surfaces, a released reliability package, and a novel architecture around five engines + Ising heartbeat.

This is a Pre-seed signal, not a growth-metrics story yet: the bet is builder velocity, original architecture, and whether "solo + AI collaboration" becomes a new engineering unit. Open an issue if that thesis resonates.

**If you're a potential co-founder** — clone [taiji](https://github.com/yangfei222666-9/taiji), run the live HUD path, and open a GitHub issue if something resonates. No polished CV needed.

**If you're a potential user** — describe your business pain point. We'll evaluate whether a custom skill on top of TaijiOS could be your industry's first landing case.

---

## 📬 Contact

- **GitHub issues preferred** — open an issue on the repo closest to your topic
- Telegram bot: [@TaijiOS_bot](https://t.me/TaijiOS_bot)
- ClawHub: [Zhuge · AI Prediction Advisor](https://clawhub.ai/@yangfei222666-9/zhuge-skill)
- Xiaping: [诸葛亮 · AI 推演军师](https://xiaping.coze.site/)

---

<p align="center">
  <strong>太极生两仪，两仪生四象，四象生万物。</strong><br>
  <em>From Taiji comes Yin and Yang; from Yin and Yang come all things.</em>
</p>
