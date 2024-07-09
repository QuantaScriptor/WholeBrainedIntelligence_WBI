# Setup

© Reece Dixon - All rights reserved.

CONFIDENTIALITY NOTICE: This information is the exclusive property of Reece Dixon and is provided under strict confidentiality. Unauthorized use, reproduction, or distribution is prohibited.

## Introduction
The WholeBrainedIntelligence (WBI) system is designed to provide advanced AI capabilities by integrating various cognitive modules. This guide will help you set up the WBI system on your machine.

## Prerequisites
- Python 3.8 or higher
- Git
- Virtual environment tool (e.g., `venv`, `virtualenv`)
- Required libraries (listed in `requirements.txt`)

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/QuantaScriptor/WholeBrainedIntelligence_WBI.git
cd WholeBrainedIntelligence_WBI
```

### Step 2: Set Up the Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure the Environment
Create a `.env` file in the root directory and add necessary environment variables.

### Step 5: Run Initial Setup Script
```bash
python setup.py
```

## Troubleshooting
- Ensure all dependencies are installed correctly.
- Verify the Python version using `python --version`.

For further assistance, refer to the [troubleshooting guide](./troubleshooting.md).
