# AI Comparison: ELIZA vs LLM

## Overview

This project compares two types of conversational AI systems:

* **ELIZA (Past AI):** A rule-based chatbot that uses pattern matching to generate responses.
* **LLM (Modern AI):** A transformer-based language model that generates responses dynamically based on context.

The goal is to demonstrate the difference between early symbolic AI and modern data-driven AI by observing how each system responds to the same user inputs.

---

##Project Structure (Python Scripts)

eliza.py – Original ELIZA chatbot (predefined rules)
eliza(1).py – Modified ELIZA (custom patterns/responses)
LLM.py – Transformer-based chatbot (Hugging Face)
chat_comparison.py – GUI for side-by-side comparison

---
## ELIZA Modifications

The ELIZA chatbot was customized by modifying and extending its response rules. 
Changes include:

- Added new input patterns 
- Improved response phrasing to be more natural
- Reduced repetitive generic responses
- Introduced more context-relevant follow-up questions
- Adjusted wording for clarity and variation


## Features

* Side-by-side comparison of ELIZA and LLM responses
* GUI-based interaction using Tkinter
* Real-time response generation
* Demonstrates differences in AI behavior clearly

---

## Comparison Summary

* ELIZA uses predefined rules and pattern matching to generate responses.
* The LLM generates responses dynamically based on learned language patterns.
* ELIZA responses are predictable and often repetitive.
* The LLM produces more natural, detailed, and context-aware responses.
* ELIZA lacks true understanding and memory of context.
* The LLM simulates understanding by leveraging large-scale training data.

---

## Observations

* ELIZA focuses on reflecting the user's input using simple transformations.
* The LLM provides meaningful suggestions and expands on the topic.
* ELIZA works well for structured conversations but fails with complex input.
* The LLM handles a wider range of inputs but requires more computational resources.

---

##Output Evidence (Screenshots)

eliza-built-in-output.png – Original ELIZA chatbot output (predefined rules)
eliza-custom-rules-output.png – Modified ELIZA with custom patterns/responses
llm-generative-output.png – Transformer-based chatbot output (Hugging Face)
chat-comparison-1.png, gui-chat-comparison-2.png, gui-chat-comparison-3.png – Sequential GUI screenshots for side-by-side comparison

## Conclusion

ELIZA demonstrates how early chatbots created the illusion of intelligence through pattern matching. In contrast, modern LLMs generate more realistic and context-aware responses using machine learning techniques. While ELIZA is efficient and simple, LLMs are more powerful but computationally demanding.
