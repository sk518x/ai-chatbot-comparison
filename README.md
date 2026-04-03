# AI Comparison: ELIZA vs LLM

## Overview

This project compares two conversational AI systems:

* ELIZA (Past AI): Rule-based chatbot using pattern matching.
* LLM (Modern AI): Transformer-based model generating context-aware responses.
  
The project follows a stepwise approach: starting with the original ELIZA chatbot, extending it with custom rules, implementing a Transformer-based LLM, and finally comparing the original ELIZA and LLM side-by-side in a Tkinter GUI using similar inputs.

## Project Structure (Python Scripts)

* eliza.py – Original ELIZA chatbot (predefined rules)
* eliza_modified.py – Modified ELIZA (custom patterns/responses)
* LLM.py – Transformer-based chatbot (Hugging Face)
* chat_comparison.py – GUI for side-by-side comparison

## ELIZA Modifications

The ELIZA chatbot was customized by modifying and extending its response rules. 
Changes include:

- Added new input patterns  
- Improved response phrasing to be more natural and less repetitive  
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
* eliza-modified-output.png – Modified ELIZA with custom patterns/responses
* llm-generative-output.png – Transformer-based chatbot output (Hugging Face)
* gui-chat-comparison-1.jpeg, gui-chat-comparison-2.jpeg, gui-chat-comparison-3.jpeg – GUI comparison of original ELIZA and LLM  

## Conclusion

ELIZA illustrates early rule-based chatbots, while LLMs provide realistic, context-aware interactions; ELIZA is simple and efficient, whereas LLMs are more powerful but computationally demanding.
