# Uncertainty-Lab

An Artificial Intelligence (CS485) lab demonstrating Bayesian Networks and probabilistic reasoning using the classic burglar alarm problem.

## Overview

This project implements a Bayesian Network to model uncertainty and conditional dependencies in a real-world scenario. The network models the relationships between burglaries, earthquakes, alarm systems, and witnesses (John and Mary) who might call about the alarm.

## Problem Description

The burglar alarm problem is a classic example in probabilistic reasoning:

- A house has a burglar alarm that can be triggered by either a **burglary** or an **earthquake**
- Two neighbors, **John** and **Mary**, might call if they hear the alarm
- Each event has associated probabilities and conditional dependencies

The Bayesian Network captures these relationships:

```
Burglar ──┐
          ├─→ Alarm ──┬─→ John
Earthquake┘           └─→ Mary
```

## Files

- `model.py`: Defines the Bayesian Network structure with nodes and conditional probability tables
- `inference.py`: Performs probabilistic inference given observed evidence (John and Mary both called)

## Requirements

```bash
pip install pomegranate
```

## Usage

Run the inference script to calculate probabilities:

```bash
python inference.py
```

### Example Output

Given that both John and Mary called (evidence), the model computes the posterior probabilities for each variable:

```
burglar: Probability distribution over {yes, no}
earthquake: Probability distribution over {yes, no}
alarm: Probability distribution over {yes, no}
john: yes (observed)
mary: yes (observed)
```

## Model Details

### Prior Probabilities

- Burglary: 0.001 (0.1%)
- Earthquake: 0.002 (0.2%)

### Conditional Probabilities

- **Alarm** depends on Burglar and Earthquake
  - P(Alarm=yes | Burglar=yes, Earthquake=yes) = 0.95
  - P(Alarm=yes | Burglar=yes, Earthquake=no) = 0.94
  - P(Alarm=yes | Burglar=no, Earthquake=yes) = 0.29
  - P(Alarm=yes | Burglar=no, Earthquake=no) = 0.001

- **John calls** depends on Alarm
  - P(John=yes | Alarm=yes) = 0.9
  - P(John=yes | Alarm=no) = 0.05

- **Mary calls** depends on Alarm
  - P(Mary=yes | Alarm=yes) = 0.7
  - P(Mary=yes | Alarm=no) = 0.01

## Learning Outcomes

This lab demonstrates:

- Bayesian Network construction and representation
- Conditional probability tables (CPTs)
- Probabilistic inference using evidence
- Reasoning under uncertainty
- The pomegranate library for probabilistic modeling

## License

See [LICENSE](LICENSE) file for details.
