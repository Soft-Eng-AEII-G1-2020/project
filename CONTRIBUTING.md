# Useful links

1. [Python](https://www.python.org/downloads/)
1. [Visual Studio Code](https://code.visualstudio.com/)
1. [Git](https://git-scm.com/downloads)
1. [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
1. [PEP 8](https://www.python.org/dev/peps/pep-0008/)

# Getting started

## Setup of environment

You should start from installing Python3. To do that visit first link - [Python](https://www.python.org/downloads/), and download latest Python release. During installation check those options:
- *Add Python 3.9 to PATH*
And then proceed with installation clicking Install Now.

After installation is complete, you will see window with header **Setup was successful**. In this window, select *Disable path length limit* and close.

## Code editor

After installing Python, go to [Visual Studio Code](https://code.visualstudio.com/) and chose **Download for Your System (Stable Build)**. After the file is downloaded, run it, accept the license and select:

- *Add "Open with Code action to Windows Explorer file context menu*
- *Add "Open with Code action to Windows Explorer directory context menu*
- *Register Code as an editor for supported file types*
- *Add to PATH (requires shell restart)*

Click **Next** and **Install**.

## Git 

When previous steps are completed, proceed with Git installation. Go to [Git](https://git-scm.com/downloads) and download Git client for your Operating System. On windows, during installation select components:

- *Windows Explorer Integration*
    - *Git Bash Here*
- *Associate `.git` configuration files with the default text editor*
- *Associate `.sh` files to be run with Bash*

On next page select:

- *Use Visual Studio Code as Git's default editor*

On the page **Adjusting your PATH environment** select:

- *Git from the command line and also from 3rd-party software*

On next pages select:

- *Use the OpenSSL library*
- *Checkout as-is, commit Unix-style line endings*
- *Use Windows' default console window*
- *Default (fast-forward or merge)*
- *Git Credentials Manager Core*
- *Enable file system caching*

After that, you can open folder where you will store your project, and then right click, and invoke this command:

```
git clone https://github.com/Soft-Eng-AEII-G1-2020/project
```

# Style

## Commit messages

To keep things clean and readable, follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) rules. For most of the time, your commit messages will look like this:

```
fix(converter): conversion from string to int was broken

feat(serializer): added serialization to json from data struct

test(serializer): written test for struct to json serializer
```

## Coding style

On every pull request GitHub Action with [PEP 8](https://www.python.org/dev/peps/pep-0008/) style formatter will be triggered, **BUT** try to write your code as close to standard as you can.

This repository includes `.vscode/settings.json` with some settings for Visual Studio Code, that will ensure we are all using same encoding, tab width, and that we are using spaces instead of tabs.

## Git Flow

---

***Git Flow***

*In the Git flow development model, you have one main development branch with strict access to it. It’s often called the `develop` branch.*

*Developers create feature branches from this main branch and work on them. Once they are done, they create pull requests. In pull requests, other developers comment on changes and may have discussions, often quite lengthy ones.*

*It takes some time to agree on a final version of changes. Once it’s agreed upon, the pull request is accepted and merged to the main branch. Once it’s decided that the main branch has reached enough maturity to be released, a separate branch is created to prepare the final version. The application from this branch is tested and bug fixes are applied up to the moment that it’s ready to be published to final users. Once that is done, we merge the final product to the `main` branch and tag it with the release version. In the meantime, new features can be developed on the `develop` branch.*

---
Konrad Gadzinowski, [toptal.com](https://www.toptal.com/software/trunk-based-development-git-flow)

# Additional notes

This repository also includes `.vscode/extension.json`. While opening this folder you will be prompted to install recommended extensions. Most of them are not necessary, but I strongly recommend using this icon pack and theme, as it greatly improves readability of code. The extensions are listed in the order from crucial one, to least important.
