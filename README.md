# PIR – BLE Reader

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/PIR-IDS/ble-reader">
    <img src="https://avatars.githubusercontent.com/u/99486891" alt="Logo" width="130">
  </a>

  <p align="center">
    IDS: Code for the BLE reader used during the training phase of our model
    <br />
    <a href="https://github.com/PIR-IDS/ble-reader/releases"><strong>See Releases »</strong></a>
    <br />
    <br />
    <a href="https://github.com/PIR-IDS/research-paper">Research Paper</a>
    ·
    <a href="https://github.com/PIR-IDS/ble-reader/actions/workflows/test.yml">Test Results</a>
    ·
    <a href="https://github.com/PIR-IDS/.github/blob/main/profile/README.md#usage">See Global Usage</a>
  </p>
  
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#execution">Execution</a></li>
      </ul>
    <li><a href="#tree-structure">Tree Structure</a></li>
    <li><a href="#credits">Credits</a></li>
    <li><a href="#contact">Contact</a></li>

  </ol>
</details>

***

<!-- ABOUT THE PROJECT -->
## About The Project

This code will be used in order to read the BLE during the training phase of our model for our IDS.

### Built With
* [Python](https://www.python.org/)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Install the latest version of pyenv (https://github.com/pyenv/pyenv-installer [ UNIX ], https://pyenv-win.github.io/pyenv-win/ [ WINDOWS ]) or update it with the following command:
  ```sh
  pyenv update
  ```
* Install the latest version of pipenv (https://pipenv.pypa.io/) or update it with the following command:
  ```sh
  pip install pipenv --upgrade
  ```
  
### Installation

1. Clone the project
   ```sh
   git clone https://github.com/PIR-IDS/ble-reader.git
   ```
2. Install the dependencies by typing the following command while being in the project root:
   ```sh
   pipenv install --dev
   ```
> :warning: **If you are using pyenv-win (WINDOWS)** : If you do not have the version of Python used in the project, it is possible that pipenv does not detect pyenv, preventing you from using it directly. To solve this problem, first install the desired version `pyenv install 3.10.0` and then instead of the above command use this one: `pipenv --python %USERPROFILE%\.pyenv\pyenv-win\versions\3.10.0\python.exe install --dev`
3. The project is now ready to run.

<!-- USAGE EXAMPLES -->
## Usage

### Execution

Run the following instructions to launch the reader, with `<address>` the device address and `<filename>` the file where you want the output to go in the `out` directory:
   ```sh
   pipenv run read <address> [<filename>]
   ```

<!-- TREE STRUCTURE -->
## Tree Structure
<details>

_TODO_

</details>

<!-- CREDITS -->
## Credits

Romain Monier [ [GitHub](https://github.com/rmonier) ] – Co-developer
<br>
Noé Chauveau [ [GitHub](https://github.com/Noecv) ] – Co-developer

<!-- CONTACT -->
## Contact

Project Link : [https://github.com/PIR-IDS/ble-reader](https://github.com/PIR-IDS/ble-reader)

Organization Link : [https://github.com/PIR-IDS](https://github.com/PIR-IDS)
