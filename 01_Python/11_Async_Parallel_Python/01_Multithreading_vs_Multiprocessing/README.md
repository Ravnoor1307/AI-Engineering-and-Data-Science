# 🧵 01 — Multithreading vs Multiprocessing

**Section 12: Async/Parallel Python | Topic 1 of 4**

Ek hi PC pe EK-SE-ZYADA kaam — do raaste:
- 🧵 **Threads** = kitchen ke counter boys (saath-baithe, GIL ka ek-chabhi-tala!)
- 🏭 **Processes** = alag-alag kitchens (har-ek apna oven — koI GIL-nahi!)

## 📚 Contents
| Notebook | Focus |
|---|---|
| `01_concepts_theory.ipynb` | PID/stove-demo · IO-magic live (3x) · GIL-photo · mp as printed `.py` |
| `02_comparison_demo.ipynb` | 10-file race · map-vs-as_completed · GIL-crunch experiment · scorecard 🏆 |

## 💡 Golden Rule
**IO-BOUND → Threads** · **CPU-BOUND → Processes (mp!)** · sirf waits? → **ASYNC** (agla topic!)

## 🎯 Prereq: 11 OS_Module. **Next:** `02_Async_Await` 🦸
