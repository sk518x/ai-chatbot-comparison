# AI Comparison: ELIZA vs LLM

## Overview

This project compares two conversational AI systems:

* ELIZA(Past AI): Rule-based chatbot using pattern matching.
* LLM (Modern AI): Transformer-based model generating context-aware responses.

It demonstrates the differences between early symbolic AI and modern data-driven AI.

## Project Structure (Python Scripts)

* eliza.py – Original ELIZA chatbot (predefined rules)
* eliza(1).py – Modified ELIZA (custom patterns/responses)
* LLM.py – Transformer-based chatbot (Hugging Face)
* chat_comparison.py – GUI for side-by-side comparison

## ELIZA Modifications

The ELIZA chatbot was customized by modifying and extending its response rules. 
Changes include:

- Added new input patterns
- Improved response phrasing to be more natural
- Improved phrasing and reduced repetitive responses
- Added context-relevant follow-up questions
  
## Comparison & Observations

* ELIZA uses predefined rules and pattern matching.
* LLM generates responses dynamically based on learned language patterns.
* ELIZA responses are predictable and often repetitive.
* LLM produces more natural, detailed, and context-aware responses.
* ELIZA reflects the user's input using simple transformations.
* LLM provides meaningful suggestions and expands on topics.

## Output Evidence (Screenshots)

* eliza-built-in-output.png – Original ELIZA chatbot output (predefined rules)
* eliza-custom-rules-output.png – Modified ELIZA with custom patterns/responses
* llm-generative-output.png – Transformer-based chatbot output (Hugging Face)
* chat-comparison-1.png, gui-chat-comparison-2.png, gui-chat-comparison-3.png – Sequential GUI screenshots for side-by-side comparison

## Conclusion

ELIZA illustrates early rule-based chatbots, while LLMs provide realistic, context-aware interactions. ELIZA is simple and efficient. LLMs are more powerful but computationally demanding.
