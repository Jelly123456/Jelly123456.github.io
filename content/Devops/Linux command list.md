title: Everything about Linux
date: 9-Feb-2021
author: YiLi

# Linux command list

* copy the contents from one folder to another folder
* `cp -R <source_folder>/* <destination_folder>`
* copy the file in one folder to another folder

  * `cp filename <destination_folder>`
* delete the contents of a directory

  * `rm /path/to/directory/*`
* delete a directory which is not empty

  * `rm -r /path/to/dest/`
* delete a file from a directory

  * `rm /path/to/dest/filenae`
* Find a file from a directory

  * `find /path/to/directory -name "filename"`
* count the number of files in a directory

  * `ls | wc -l`
* find all empty files in a directory

  * current directory
    * `find . -type f -empty`
  * any directory
    * `find /path/to/dest -type f -empty`
* Check OS information

  * One of them in below
    * `cat /etc/os-release`
    * `lsb_release -a`
    * `hostnamectl`
* Unzip the file with extension "*.zip"

  * `unzip *.zip`
* Display "PATH" variable

  * `echo $PATH`
* Check current directory size

  * du -sh
* Check a specific folder size

  * `du -sh folder destination`
* Move the files in a folder to a new folder

  * `mv source target`
  * It will move the source folder into the target folder

# Automatically set path in .bashrc

* where is .bashrc
  * ~/.bashrc ~ stands for home directory
* run below command to set new path
  * `source ~/.bashrc`

# Redirecting make command output to a file

* Redirect all the outputs to a file regardless it is stdout or stderror
  * `make > log.txt 2>&1`
  * Each process gets a few "default" file handles, named stdin, stdout and stderr. Each file handle has an integer associated with it. 0 is stdin, 1 is stdout and 2 is stderr.
