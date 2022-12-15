# Dynamic Analysis Framework for Python

This is a framework which performs dynamic analysis of Python code. The tool accepts a piece of Python code along with a valid input, executes it and creates a graph representation which captures the runtime semantics of the program. The framework proceeds to feed the graph into a Graph Convolutional Neural Network which predicts a NumPy API which is semantically closest to it. 

More details on the tool and how it works can be found in the Report <a href="https://drive.google.com/file/d/1kVi5bVQst01KCZkf_lrV7iaoKnILgkYr/view?usp=sharing">here</a>.

---

## Installation

The tool has been tested on Python 3.8.2 and 3.8.10. Before proceeding to install the tool, please check the version of your Python install using the command: 

```bash
python --version
```

If the output is not `Python 3.8.*`, we strongly recommend either installing Python 3.8 <a href="https://www.python.org/downloads/">from here</a>, if you do not have an existing Python installation, or installing a virtual environment using Anaconda, if you already have one or more versions of Python installed. Please follow the following instructions to install Python 3.8 using Anaconda, if applicable, else skip to the installation of this repository.

### Installing Python 3.8 using Anaconda (Optional)

1. Download the Anaconda installer from <a href="https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html">here</a> and follow all the steps to install.
2. Run the following to create a new environment with Python 3.8.2 and follow the prompts:
```bash
conda create --name myenv python=3.8.2
```
3. Run the following to activate the new environment
```bash
conda activate myenv
```
4. Verify the Python version using the command: 
```bash
python --version
```

### Installing the Repository

1. Clone the repository using the following command (you may use the SSH link as well) and navigate inside the directory:
```bash
git clone https://github.com/shadaj/python-analysis.git
cd python-analysis
```
2. Run the following to install dependencies:
```bash
pip install -r requirements.txt
```
