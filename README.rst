===================
IC4A - Main details
===================

``IC4A`` - stands for **Interactive Console 4 Automation**.

Writing this tool was caused by having more and more challenges related with repeating quickly tasks
which I am doing every day (Searching for files, creating templates for scripts, analysing scripts,
checking code, automation, configuration manager, etc).

**Goal:**

- Create software which can work like ``git`` (commands: ``init``, ``prepare``, ``ansible``) - using
  many arguments and do some actions with this commands.
- Track changes in one folder (``HOME`` directory) and allow work much more effectievly.
- Have modular (if possible) structure.
- Workflow similar like ``Metasplit`` / ``DAC`` / ``routersploit`` / etc.


Installation
============

Project should be easy installed from ``GitHub`` repository.


Install from source
-------------------

Following steps should help to install this project from source code.


**Downloading repository from GIT**

Clone this project from ``GitHub``

.. code-block:: bash

  git clone https://github.com/marcinpraczko/osl-ic4a.git
  cd ic4a

**Python Virtual Environment**

The best is working with ``python-virtualenv`` tool which allow create separate environment for
python projects without impacting main system. This brings benefits that project can be removed
with all dependencies just by removing folder with project.

* Install ``python-virtualenv`` via packages manager on your Distro

* Next step is to create Python Virtual Environment for this project:

.. code-block:: bash

  # Create Virtual Environment
  mkdir venv
  virtualenv venv

  # Active Virtual Environment
  source venv/bin/activate
  cd venv

  # Update standard packages
  pip install --upgrade pip
  pip install --upgrade setuptools

* Once this is done, run following commands to install all required dependencies.

.. code-block:: bash

  pip install -r python_requirements.txt

* When work is done - ``python-virtual`` environment should be deactivate with command:


.. code-block:: bash

  deactivate
