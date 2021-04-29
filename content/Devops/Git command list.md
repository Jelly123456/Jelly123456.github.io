title: Everything about Git
date: 9-Feb-2021
author: YiLi

# Git command list

* Update from remote server and ignore local changes
  * First fetch all changes:
    * `git fetch --all`
  * Then reset the master:
    * `git reset --hard origin/master`
  * Pull/update:
    * `git pull`
* Download a specific release/tag from github
  * `git clone ***.git`
  * list all the tags in the repo
    * `git tag -l`
  * Get current tag information
    * `git describe --tags`
  * Checkout and create a branch locally
    * `git checkout tags/<tag_name> -b <branch_name>`
  * List all branch name in this repo
    * `git branch`
