\# AI Business Requirements Assistant



\## Business problem

Business Analysts spend hours turning messy stakeholder conversations into requirements documents. Drafts often silently resolve disagreements or add assumptions nobody stated.



\## What it does

Paste a stakeholder interview or meeting transcript and get a structured BRD draft: business objective, in-scope and out-of-scope items, functional requirements, non-functional requirements, open questions and user stories.



\## Results

Tested on three transcripts: one stakeholder with unresolved details, two stakeholders in conflict, and a clean request with one buried ambiguity.

\- The first prompt version invented specific non-functional requirements (uptime, encryption, compliance standards) that the stakeholder never mentioned. An explicit grounding instruction fixed this.

\- When stakeholders disagreed, the tool now names both positions in Open Questions instead of picking a side.

\- Known limitation: minor inference drift remains, for example describing an audit trail as "immutable" when the stakeholder did not say so.



Full write-up: BA\_Requirements\_Assistant\_Report.pdf. Screenshots of all three tests are in the Screenshots folder.



\## Tools

Python, Groq API (openai/gpt-oss-120b), Streamlit



\## Run it

Set a GROQ\_API\_KEY environment variable, then run: streamlit run app.py

