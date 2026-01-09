Links and Resources:
https://medium.com/@himanshusingour7/how-i-learned-system-design-d7444d454367 - blog
https://youtube.com/playlist?list=PLDzeHZWIZsTr3nwuTegHLa2qlI81QweYG&si=q6ZMEIwwFJbozol9 - OS
https://www.youtube.com/playlist?list=PLDzeHZWIZsTpukecmA2p5rhHM14bl2dHU - DBMS
https://www.youtube.com/playlist?list=PLinedj3B30sBlBWRox2V2tg9QJ2zr4M3o - system design basics
https://www.youtube.com/playlist?list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX - gaurav sen



System Design is not one big subject it’s a set of interconnected building blocks.  
So I made a map for myself:

## a) The Basics

- What happens when you type a URL in the browser
- What is DNS, Load Balancer, CDN
- TCP vs UDP, HTTP vs HTTPS

Even these basics were eye-opening. Like  
Did you know DNS is like a phonebook of the internet? And CDNs are why YouTube loads fast?

## b) Data and Storage

- SQL vs NoSQL
- Indexing, Replication, Sharding
- When to choose MongoDB vs PostgreSQL

I learned this the hard way. In one project, we chose Mongo for transactional data. Later, we regretted it.

## c) Scaling Techniques

- Horizontal vs Vertical scaling
- Caching (Redis, Memcached)
- Load balancing (Round-robin, IP Hashing)

I loved this part. It made me feel like I could finally design something for millions of users even if it was just on paper.

## d) Architecture Patterns

- Monolith vs Microservices
- Event-Driven Architecture
- Pub/Sub, Message Queues (Kafka, RabbitMQ)

This made me understand _why_ companies like Netflix use microservices not just because it’s trendy, but because it makes sense at scale.

## 3. I Watched Real People Think, Not Just Teach

==Instead of watching tutorial-style videos, I started watching mock interviews.==

Channels that really helped:

- Gaurav Sen explains from the ground up
- Exponent mock interviews with real candidates
- ByteByteGo visual, storytelling approach

I learned how to:

- Ask the right clarifying questions
- Define functional and non-functional requirements
- Walk through API design, DB choices, scaling logic
- Always talk about **tradeoffs**, not just choices

## 4. I Started Drawing Even If It Was Just on Paper

One surprising thing that helped me?  
==Drawing==.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:700/0*SXByOhjvsphJRqrF)

I’m not an artist. But sketching out a flow from client → load balancer → app servers → DB made it click.

Here’s how I practiced:

- Pick a real-world system: WhatsApp, YouTube, Zomato, Instagram
- Write the **functional requirements** first (what the system should do)
- Then add **non-functional requirements** (scale, availability, latency)
- Do rough estimation (users, QPS, DB size)
- Design a **high-level architecture**

Go deeper into:

- DB schema
- APIs
- Scaling strategies
- Handling failures
- Edge cases

I wrote one design per week.  
And not just one solution but **multiple possibilities**.