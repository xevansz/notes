---
title: Geohot — What is Programming?
tags:
  - computer-science
  - paradigms
  - mental-models
  - geohot
---

# Geohot — What is Programming?

> *"Learn something from nature, not people. Don't learn object-level skills, learn meta-level skills."*
> — Notes on George Hotz (Geohot)

---

## 1. The Core Paradigm

$$\text{Input} \longrightarrow \text{System (Computation)} \longrightarrow \text{Output}$$

* Languages to consider: Rust? C.
* **GC (Garbage Collection)**: Automated memory management vs manual control.

### What is a Computer?
- **Processor**: Stream of instructions.
- **RAM**: Instructions + Data.

### Anatomy of a Running Program
| Segment | Purpose |
| :--- | :--- |
| `text` | Instructions (executable machine code) |
| `bss` | Static / uninitialized data |
| `stack` | Local variables & control flow (call stack) |
| `heap` | Dynamic memory allocation (`malloc`) |

```c
void a() {
    int variable_on_the_stack;
    // return by popping off the stack
}

void b() {
}

int main() {
    a(); // pushes return location onto stack
    b();
}
```

---

## 2. Programming for Work: Translators vs Engineers

What does a software engineer typically do?
- Most don't write algorithms.
- Some work on infrastructure.
- **Most are translators**: They translate `Business Requirements` $\longrightarrow$ `Code`.

Frameworks (e.g., Ruby on Rails) power standard **CRUD** apps (Create, Read, Update, Delete):
- **Frontend (View)**
- **Business Logic (Controller)**
- **Database (Model)**

### What Bootcamps / Tutorials Teach:
1. Build a CRUD app contracting firm.
2. Record all developer inputs (translators).
3. Train AI models to translate `Business Logic` $\longrightarrow$ `Code`.

> **Takeaway**: Most only learn framework syntax and write code within that box without understanding how computers actually function under the hood.

---

## 3. What is Hacking?

Applying the same input/system paradigm:
> *"What input to the system achieves my desired outcome?"*

- **Pure Model**: $\text{Domain} \longrightarrow \text{Function} \longrightarrow \text{Range} \quad (y = f(x))$
- **Reality**: Most computations are *impure* (side effects, state).
- **Hacking**: Figuring out how to make the function behave how you want. Practice until you understand the edge cases and internals.

---

## 4. High-Brow Software Engineering

A repeatable paradigm to hone mastery:
1. **Understand** a complex system.
2. **Modify** the system to add a feature.
3. **Ship** the new system (test thoroughly).

### Machine Learning Engineering Loop:
1. Download a research paper.
2. Implement it from scratch.
3. Repeat continuously until deep intuition is built.

---

## 5. Mental Models, Funnels & Capitalist Consent

### Sales Funnels (Example: Selling Cars)
1. **10,000**: Top of funnel (advertising) — *1% conversion*
2. **100**: Visit the dealership — *5% conversion*
3. **1**: Buy the car

### Capitalism & Money
Capitalism is fundamentally structured around **consent**:
- Both buyer and seller must consent to the transaction.
- To get money in a capitalist system: **convince others to give it to you willingly**.

To make **$1,000,000**:
- $\$1$ from $1,000,000$ people
- $\$1,000$ from $1,000$ people
- $\$1,000,000$ from $1$ person
*(There is no other way.)*

---

## 6. Algorithmic Thinking & Dynamic Programming

- Dynamic Programming (DP): Write state $(x, y)$ in terms of subproblems $(x-1, y-1)$.
  $$f(x, y) \Longleftarrow f(x-1, y-1)$$
- Build a table using previous outputs to calculate subsequent states without redundant work.
- Algorithmic Complexity: Understand $O(n), O(\log n), O(n^2)$.

---

## 7. Life Principles & The Knowledge Tree

- **Existentialism**: You construct your own meaning.
- **Avoid Skinner Boxes**: Don't fall into funnels designed by others; resist advertising.
- **College & Power**:
  - Reject power over people (political/bureaucratic).
  - Embrace power over nature (physics, engineering, computation).
- **Data Science**:
  - Statistics $\longrightarrow$ **YES**
  - Tool obsession $\longrightarrow$ **NO**

### Building a Knowledge Tree (Elon vs Geohot)
- New information must fit into a cohesive tree structure so interpolation is possible.
- *Elon* roots his knowledge tree in **Physics** (Modernist).
- *Geohot* roots his knowledge tree in **Information** (Postmodernist).
- **Post-structuralism & Constructivism (Math)**: Making money is never a terminal value.
- Reference reading: *Dictatorless Dystopia* (Slate Star Codex).

---

## 8. Open Questions in Computer Architecture
- *"Two hard problems in computer science: cache invalidation and naming things."*
- Does there exist a more concise programming language? What is the next GC?
- How much can automated programming help?

---
*Related: [[Programming Fundamentals]] | [[Computer Systems & Hardware]] | [[System Design]]*
