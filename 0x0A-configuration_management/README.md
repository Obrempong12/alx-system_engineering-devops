0x0A-configuration_management

This project in the System engineering & DevOps series is about:
Configuration Management
Puppet

Requirements
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 14.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
Your Puppet manifests must pass puppet-lint without any errors
Your Puppet manifests must run without error
Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
Your Puppet manifests files must end with the extension .pp
Files will be checked with Puppet v3.4

TASKS-
0. Create a file
Using Puppet, create a file in /tmp.
Requirements:
File path is /tmp/school
File permission is 0744
File owner is www-data
File group is www-data
File contains I love Puppet
1. Install a package
Using Puppet, install flask from pip3.
Requirements:
Install flask
Version must be 2.1.0
2. Execute a command
Using Puppet, create a manifest that kills a process named killmenow.
Requirements:
Must use the exec Puppet resource
Must use pkill
