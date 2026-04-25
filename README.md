<h1 align="center">TaijiOS · 诸葛亮</h1>

<p align="center">
  Building <strong>TaijiOS</strong> — a hexagram-guided reliability and learning runtime for AI agents.
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

This is not a funding story yet. It is an execution-density snapshot. Check each repo for the latest state.

---

## 🌀 Core Projects

This profile is the portfolio entrance. Start here, then follow the repo that matches your use case:

| Project | What | Language |
|---|---|---|
| **[taiji](https://github.com/yangfei222666-9/taiji)** | Current main repo — hexagram-guided reliability/runtime system, live HUD, five-engine architecture | Python |
| **[self-improving-loop](https://github.com/yangfei222666-9/self-improving-loop)** | Standalone reliability layer — v0.1.1 released; trace failures, apply guarded changes, and rollback on regression | Python |
| **[taijios-bundle](https://github.com/yangfei222666-9/taijios-bundle)** | Installer / release snapshot / local trial bundle | Python |
| **[TaijiOS](https://github.com/yangfei222666-9/TaijiOS)** | Legacy prototype — archive candidate; current main development is `taiji` | Python |
| **[TaijiOS-Lite](https://github.com/yangfei222666-9/TaijiOS-Lite)** | Lite prototype / example pack — archive candidate; reusable ideas move into `taiji` | Python |
| **[zhuge-skill](https://github.com/yangfei222666-9/zhuge-skill)** | 诸葛亮 · AI Prediction Advisor — 64-hexagram reasoning for football prediction (demo of TaijiOS decision engine) | Python |

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

Multi-LLM with auto-failover across 12 providers:
`Claude` · `GPT` · `Gemini` · `DeepSeek` · `Kimi` · `Qwen` · `ZhipuAI` · `Doubao` · `Yi` · `Baichuan` · `MiniMax`

---

## 🔬 Technical Highlights

- **Five-engine architecture** — each engine's responsibility is defined by an *I Ching* state role, not decoratively but as engineering constraints:
  `震 Zhen` = only recovery · `师 Shi` = only scheduling · `颐 Yi` = only experience learning · `乾 Qian` = situational awareness · `随 Sui` = persona switching.
- **Ising Heartbeat** — maps 6 system dimensions to quantum spins (σ = ±1); 6 spins × 2 states = **64 hexagrams**. In a **346-heartbeat experiment**, the system exhibited a clean phase transition at tick 37 (ΔH = +0.30), then locked 99% of subsequent time in a new stable state. The self-adaptive field converged toward a *kun-virtue* (accommodating) coupling pattern — a physics-level emergence consistent with classical Taoist cosmology.
- **LLM Gateway** — unified auth / rate-limit / multi-provider failover / audit, 12/12 extreme-scenario tests passed.
- **Safe Click (4 gates)** — default-deny RPA click executor: window-binding + region-blacklist + whitelist + OCR-confidence.
- **Self-Improving Loop** — standalone reliability package released as `v0.1.1`; feedback, guarded strategy, and rollback are now separate from the main repo.

---

## 💬 Philosophy

> *任何学说，都只是你的片面镜子。完整的镜子早在你心里 — 我们只是造工具让你看见它。*
>
> *Any school of thought is just a partial mirror of you. The complete mirror is already inside you — we just build the tools to let you see it.*
>
> — from the **ICI protocol**

Not fortune-telling. **Life engineering.**

---

## 🤝 How to Collaborate

**If you're an investor** — I don't have growth curves yet. What I can verify is execution density, technical originality, and a working portfolio of small releases. If you believe "solo + AI collaboration" is a future engineering unit and are open to betting on signal over metrics at Pre-seed, let's talk.

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

<p align="center">
  <sub>⚡ This README is part of TaijiOS dogfooding. Numbers are project snapshots; verify the latest state from each repository before citing.</sub>
</p>
