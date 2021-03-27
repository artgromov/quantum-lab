# Quantum-lab
Tested on ubuntu 20.04.

## Environment setup
1. Install anaconda: https://www.anaconda.com/products/individual
2. Install direnv: https://direnv.net/
3. Initialize shell for usage with conda

```
$ conda init
```

4. Clone this repo

```
$ git clone https://github.com/artgromov/quantum-lab.git
```

5. Create and setup env

```
$ cd quantum
$ direnv allow
```

6. Install conda env jupyter-lab kernel

```
$ ipython kernel install --name quantum-lab --display-name 'Quantum Lab' --user
```

## Environment usage after setup
You can change to quantum-lab dir to activate env and run any code directly.

```
$ cd quantum-lab
direnv: loading ~/quantum-lab/.envrc
direnv: export +CONDA_PREFIX_1 ~CONDA_DEFAULT_ENV ~CONDA_PREFIX ~CONDA_SHLVL ~PATH
```

Or just start jupyter-lab and run notebook files with "Quantum Lab" kernel.

## IBMQ credentials setup
1. Create account on https://quantum-computing.ibm.com/
2. Create `~/.qiskit directory` if not present.
3. Add `ibmq` section to `~/.qiskit/qiskitrc` file

```
[ibmq]
token = <your token here>
url = https://auth.quantum-computing.ibm.com/api
verify = True
```

replace <your token here> string with your actual API token from https://quantum-computing.ibm.com/

4. Done. Now you can use following code to access IBMQ:
    
```
import helpers
provider = helpers.get_ibmq_provider()
``` 
    
## Useful links
- [Getting started with Qiskit](https://qiskit.org/documentation/getting_started.html)
- [Learn Quantum Computation using Qiskit](https://qiskit.org/textbook)