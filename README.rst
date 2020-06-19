====================
Bash Jupyter kernel
====================

For details of how this works, see the Jupyter docs on `wrapper kernels
<http://jupyter-client.readthedocs.org/en/latest/wrapperkernels.html>`_, and
Pexpect's docs on the `replwrap module
<http://pexpect.readthedocs.org/en/latest/api/replwrap.html>`_

Installation
============

This requires IPython 3.

To install::

    pip install bash_kernel
    python -m bash_kernel.install

To use it, run one of:

.. code:: shell

    jupyter notebook
    # In the notebook interface, select Bash from the 'New' menu
    jupyter qtconsole --kernel bash
    jupyter console --kernel bash

Background tasks
================

It is possible to register background tasks when the Bash kernel starts. This
can be useful if you want to modify the running environment of the kernel from
the outside (e.g., to set/override environment variables). Background tasks
execute for each instance of the kernel; if a background task/operation should
affect all running kernels, it is probably best to implement as a task
directly on the host running the kernel processes.

.. code::

   [options.entry_points]
   bash_kernel.tasks =
       refresh_env_token = my_module.tasks:refresh_env_token

The entry point should return a tuple of a task function and any args to the
task (currently, ``interval_s``, an interval of how often the task should run.)

.. code:: python

   def refresh_env_token():
       def task_fn():
           pass  # Do some task
       return task_fn, {'interval_s': 300}
