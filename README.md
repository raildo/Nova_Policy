Policy tests to OpenStack Compute API (Nova)
=================================================

This project provides a sample policy.json that defines three
different roles:

- A super admin, which is able to peform any operation in the cloud scope: cloud_admin
- A project scope admin: project_admin
- A project scope member: project_member

Also, tests scripts are provided for each role described above. They test 
if a user with a given role is able to peform the actions it should be
able to perform.

Those tests create and delete actual elements. They were designed to be executed
in a running devstack environment.

Tests setup
-------------

There is a script called ``nova_tests.py``.
It creates a user called cloud_admin, a project called cloud_admin_project. 

After that, you can replace or use the provided policy.json file as your
default policies file.

Running the tests
-----------------

After the tests setup, just run the tests directly:

    python nova_tests.py

If you are interested in a smaller set of tests, open the tests file and comment
the not interesting ones.

