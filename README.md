# Persona activity log (messenger, calendar) data generation prototype for [PERSONA-Bench](https://github.com/zhadyz/PERSONA-Bench)

## Overview

This program provides a pipeline to simulate app activity logs from [synthetic personas based on real-world demographics](https://huggingface.co/datasets/nvidia/Nemotron-Personas-USA) for retrieval tasks. Various interview agents generate and validate rich context to create in-depth representations of personas and their social circles. 

**Credits: [genagents: Generative Agent Simulations of 1,000 People](https://github.com/StanfordHCI/genagents)**

## Installation

### Requirements

- Python 3.7 or higher
- An OpenAI API key with access to GPT-4 or GPT-3.5-turbo models

### Dependencies

Install the required Python packages using pip:

```bash
pip install -r libs/genagents/requirements.txt
```
```bash
pip install -e libs/genagents
```

### Configuration

See [genagents README](libs/genagents/README.md/#configuration).

## Usage

**See usage in [main](main.py).**

In the [data folder](data),
- `step_1` displays the initial required data format.
- `step_2` displays the generated interview with four agent analyses.
- `step_3` displays the social circle.
- `step_4_5` displays the synthesized activity in chat and calendar formats. Additionally, the chat log prior to contextual awareness is included.
- `step_6_7` displays generated retrieval test cases.

## License

This project is licensed under the [Apache 2.0 License](LICENSE).