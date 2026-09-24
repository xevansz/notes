---
title: Computer Systems & Hardware
tags:
  - systems
  - operating-systems
  - linux
  - memory
  - low-level
---

# Computer Systems & Hardware

> Notes, papers, and references on operating systems, memory hierarchies, processor architecture, and systems engineering.

---

## 📄 Key Papers & Essential Reading

- **Memory Architecture**:
  - [[Attachments/cpumemory.pdf|What Every Programmer Should Know About Memory (Ulrich Drepper)]] — The definitive Red Hat guide on CPU caches, memory controllers, DMA, and cache lines.
- **Latency Numbers Every Programmer Should Know**:
  Run in terminal:
  ```bash
  curl cheat.sh/latency
  ```
  *(L1 cache ~1ns, Branch mispredict ~3ns, L2 cache ~4ns, RAM ~100ns, SSD ~150μs, Network send NYC->SF ~150ms)*

---

## 🖥️ Operating Systems & Kernel Internals

- [Operating Systems: Three Easy Pieces (OSTEP)](https://pages.cs.wisc.edu/~remzi/OSTEP/) — Free textbook covering Virtualization, Concurrency, and Persistence.
- [Core Dumped (YouTube)](https://www.youtube.com/@CoreDumped) — Visual breakdowns of OS kernels and computer architecture.
- [Brendan Gregg's Homepage](https://www.brendangregg.com/) — Systems performance analysis, flame graphs, and Linux tracing tools (eBPF).
- [Booting from GPT (Rod Smith)](https://www.rodsbooks.com/gdisk/booting.html) — Partitioning tables and EFI bootloader mechanisms.

---

## 🐧 Linux Administration & Systems Tooling

- [Bash Scripting: Complete Guide](https://www.youtube.com/watch?v=Sx9zG7wa4FA)
- [Linux System Hardening Tools](https://www.youtube.com/watch?v=qtzlszWN6Nw)
- [Sysadmin Fundamentals](https://www.youtube.com/watch?v=fwGqm8T9drI)
- [Hardware Control Using Memory](https://www.youtube.com/watch?v=sp3mMwo3PO0)
- [Netcat Tutorial](https://www.youtube.com/watch?v=bXCeFPNWjsM)
- [What Happens When The 'G' Key Is Pressed](https://github.com/alex/what-happens-when#the-gkey-is-pressed)

---

## 🔌 Embedded & Hardware Simulation
- [Wokwi](https://wokwi.com/) — Browser-based ESP32, STM32, and Arduino simulation.
- [PCPartPicker](https://pcpartpicker.com/) — Hardware compatibility matching.

---
*Related: [[Geohot - What is Programming]] | [[System Design]] | [[Cybersecurity]]*
