<!-- 
    Project: WholeBrainedIntelligence (WBI)
    Author: Reece Dixon
    Contact: info@quantascript.com
    Created: 2023-06-15
    Last Updated: 2024-06-25
    License: RAIL License
    
    Copyright (c) 2024 Reece Dixon. All rights reserved.
    
    This file is part of the WholeBrainedIntelligence (WBI) project. Unauthorized copying,
    distribution, modification, or any other use is strictly prohibited without prior
    written consent from the author.
-->
# WholeBrainedIntelligence (WBI)

![WBI_Banner](https://github.com/user-attachments/assets/d9523490-ff86-4522-89d8-5618b68f1357)

![Build Status](https://img.shields.io/github/actions/workflow/status/QuantaScriptor/WholeBrainedIntelligence_WBI/ci.yml)
![License](https://img.shields.io/github/license/QuantaScriptor/WholeBrainedIntelligence_WBI)
![Contributions](https://img.shields.io/github/contributors/QuantaScriptor/WholeBrainedIntelligence_WBI)
[![GitHub issues](https://img.shields.io/github/issues/QuantaScriptor/WholeBrainedIntelligence_WBI)](https://github.com/QuantaScriptor/WholeBrainedIntelligence_WBI/issues)
[![GitHub forks](https://img.shields.io/github/forks/QuantaScriptor/WholeBrainedIntelligence_WBI)](https://github.com/QuantaScriptor/WholeBrainedIntelligence_WBI/network)
[![GitHub stars](https://img.shields.io/github/stars/QuantaScriptor/WholeBrainedIntelligence_WBI)](https://github.com/QuantaScriptor/WholeBrainedIntelligence_WBI/stargazers)
[![GitHub license](https://img.shields.io/github/license/QuantaScriptor/WholeBrainedIntelligence_WBI)](https://github.com/QuantaScriptor/WholeBrainedIntelligence_WBI/blob/main/LICENSE)
[![CodeQL](https://github.com/QuantaScriptor/WholeBrainedIntelligence_WBI/actions/workflows/codeql.yml/badge.svg)](https://github.com/QuantaScriptor/WholeBrainedIntelligence_WBI/actions/workflows/codeql.yml)




---

# Whole-Brained Intelligence (WBI) - Version 3.0.0

Whole-Brained Intelligence (WBI) integrates advanced technologies like Quantum Neural Networks, Neuromorphic Computing, Advanced NLP, and Autonomous Learning.

## Features
- Quantum Neural Networks (QNN)
- Neuromorphic Computing
- Advanced NLP
- Autonomous Learning and Adaptation
- Ethical and Secure AI

## Getting Started
### Prerequisites
- Python 3.8+
- pip

### Installation and Usage

1. Install dependencies:
```sh
pip install -r requirements.txt
```

2. Run the API server:
```sh
python main.py
```

3. Access the API:
- API documentation: http://0.0.0.0:8080/docs
- API endpoint: http://0.0.0.0:8080/analyze 

## Usage

Run the main scripts:
  ```python
  from opensource_scripts.neurosymbolic_ai import hybrid_model as neurosymbolic_hybrid_model
  from opensource_scripts.quantum_integration import hybrid_model as quantum_hybrid_model
  
  inputs = [0.5, 0.6]
  neural_output, symbolic_output = neurosymbolic_hybrid_model(inputs)
  print(f"Neural network output: {neural_output}")
  print(f"Symbolic reasoning output: {symbolic_output}")
  
  inputs = np.array([0.5, 0.6])
  result = quantum_hybrid_model(inputs)
  print(f"Quantum model output: {result}")
  ```

## Testing
1. Run tests using pytest:
  ```sh
  pytest --cov=opensource_scripts tests/
  ```
## Quick Deploy
[![Deploy to Replit](https://replit.com/badge/github/QuantaScriptor/WholeBrainedIntelligence_WBI)](https://replit.com/new/github/QuantaScriptor/WholeBrainedIntelligence_WBI)

Click the button above to instantly deploy this project to Replit!

---

[wbiBanner]: https://github.com/QuantaScriptor/WholeBrainedIntelligence_WBI/raw/main/assets/170899992/7898afcc-b9d5-4692-a69a-0d56d4218769
