# ⏬ 03 — Async IO Basics (Toolkit ka Mela)

**Section 12: Async/Parallel Python | Topic 3 of 4**

asyncio ka asali-kaam-wala toolkit: `create_task` fire-&-collect, `Semaphore`
lanes 🚦, per-task `wait_for` red-card 🛡️, aur `aiohttp` ka concept (offline-sandbox
me md-sample — pattern poora hai, wire apni machine pe!).

## 📚 Contents
| Notebook | Focus |
|---|---|
| `01_asyncio_basics_theory.ipynb` | create_task dosa-order 📝 · Sem(2) 5-download lanes (peak-verify!) · per-task timeout news-digest · aiohttp sample |
| `task.ipynb` | Data-Chain ETL 🔧: 20-row CSV → gather-map → sem-lanes → timeout-card → fire-collect → 855.0/42.75 bill — 10-assert BOSS! |

## 💡 Golden Rule
ekabahar flood mat karo: `Semaphore(3)` lanes + per-task `wait_for` =
production-grade async IO ⏬🛡️

## 🎯 Prereq: 02 (async/await + gather). **Next:** `04_When_to_Use_Each` 🗺️👑
