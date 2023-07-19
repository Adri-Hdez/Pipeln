<p align="center"><img src="https://github.com/Adri-Hdez/Pipeln/blob/main/docs/static/img/Pipeln.png" alt="logo" width="80%" /></p>

<p align="center">
 <i>A Python open source package to create a custom pipeline</i>
</p>


----------------------

# 💾 Installation & Upgrade

- Installation: `pip install pipeln`
- Upgrade: `pip install pipeln --upgrade`

# 📦 What is this?

<p align="justify">
Pipeln is a Python package aimed at creating a pipeline or a sequence of custom methods execution. The goal is to enable the creation of different procedural sequences that can be encapsulated within a method, allowing for the selection of order, return values, etc. Although some functionalities are still pending implementation, for a better overview, please refer to the objectives calendar.
</p>

<p align="center">📃​ <b>Last version 0.2.0-alpha out now!</b> 📃​</p>

# 💬 Contribution & Questions

| Contribution & Questions Type     | Platforms                               |
| ------------------------------- | --------------------------------------- |
| 🐞​​ **Bug Reports**              | [GitHub Issues](https://github.com/Adri-Hdez/Pipeln/issues)                  |
| 📦​ **Feature Requests & Ideas** | [GitHub Discussions](https://github.com/Adri-Hdez/Pipeln/issues)                    |
| 🛠️​ **Usage Questions & Discusions**          | [GitHub Discussions](https://github.com/Adri-Hdez/Pipeln/issues) |

# ​🔧​ Install & Use Pipeln

To start using Pipeln use the next command:

```bash
pip install pipeln
```

To use the library properly, we follow these steps:

- Import the library.
- Initialize an object of the Pipeln class, providing the names and parameters of our methods, and setting the execution order.
- Create the execution structure.
- Execute the pipeline.

```Python
from Pipeln.pipeline import Pipeline
from features.auxiliar_test_methods import add, sub, cap

obj = Pipeline(methods=[add, sub, cap], params=[{'a': 2, 'b': 4}, ('1', 2), ('spain',)], orders=[3, 1, 2], debug=True)
obj.create()
obj.run()
```

Expected output:


```bash
DEBUG: *****************************
DEBUG:      > Starting pipeline
DEBUG:
DEBUG: EXEC: Method add executed successfully.
ERROR: ERROR: There is an error in sub method. Inappropiate argument type.
DEBUG: EXEC: Method cap executed successfully.
DEBUG:
DEBUG:   Pipeline finished in 10.9
DEBUG: *****************************
```

# 💳 License

Pipeln is licensed under [MIT License](LICENSE).

# 🗃️ Shields

<p align="center">
  <a href="https://pypi.org/project/pipeln/">
    <img src="https://img.shields.io/pypi/v/pipeln" alt="PyPI" />
  </a>
  <a href="https://pypi.org/project/pipeln/">
    <img src="https://pepy.tech/badge/pipeln" alt="downloads" />
  </a>
  <a href="https://pepy.tech/project/pipeln">
    <img src="https://img.shields.io/badge/python-3.9.x_%2F_3.10.x_%2F_3.11.x-blue" alt="versions" />
  </a>
  <a href="https://github.com/Adri-Hdez/Pipeln/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green" alt="license" />
  </a>
</p>
