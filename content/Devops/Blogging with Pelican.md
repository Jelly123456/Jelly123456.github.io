title: Using Pelican and Flex theme for blog and hosting it on Github pages
date: 3-Dec-2020
author: YiLi

I always want to set up a personal blog to record all the things(research, ideas) around my tech career. After searching the internet, I choose pelican and flex theme to write blogs because I like simpilicity.

# Pelican

Pelican is a static site generator, made in Python. By static, I mean that the content served is the same for everyone because it's generated in advance. Blogs are typically static while ecommerce sites (where you login, have an account, order history, etc.) are typically not. Templates save the blogger from having to muck about with verbose HTML. [Markdown](http://daringfireball.net/projects/markdown/) and [reStructuredText](http://docutils.sourceforge.net/rst.html) are two templating formats that Pelican handles well.

# Github pages

GitHub Pages is a static site hosting service that takes HTML, CSS, and JavaScript files straight from a repository on GitHub, optionally runs the files through a build process, and publishes a website.

# Installation

## Prerequisites

1. Python with Anaconda.
   I like anaconda because this is a very good platform for data scientist.
2. Install git for windows
   The operating system I used for my daily work is windows.
3. Create a account in github
   Because I will publish my blog into github pages

## Step 1 - Test the website locally

1. Install the packages.

```
pip install pelican Markdown ghp-import typogrify
```

2. Create a folder for the website. The folder name is username.github.io.
   
   "username" is the github name. The folder name should be like this because this will be used for github pages hosting later.

```
md username.github.io
cd username.github.io
```

3. Run the website setup

```
pelican-quickstart
```

```
$ pelican-quickstart
Welcome to pelican-quickstart v3.7.1.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.

> Where do you want to create your new web site? [.]  
> What will be the title of this web site? Super blog
> Who will be the author of this web site? username
> What will be the default language of this web site? [en]
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) n
> Do you want to enable article pagination? (Y/n)
> How many articles per page do you want? [10]
> What is your time zone? [Europe/Paris] US/Central
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) y
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) y
> Do you want to upload your website using FTP? (y/N) n
> Do you want to upload your website using SSH? (y/N) n
> Do you want to upload your website using Dropbox? (y/N) n
> Do you want to upload your website using S3? (y/N) n
> Do you want to upload your website using Rackspace Cloud Files? (y/N) n
> Do you want to upload your website using GitHub Pages? (y/N) y
> Is this your personal page (username.github.io)? (y/N) y
Done. Your new project is available at /Users/username/blog
```

Answer all the questions with default except the below:

* Do you want to specify URL prefix?
  Answer https://username.github.io
* Do you want to upload using xxx?
  Answer N untill the xxx = GitHub Pages

4. Ending with this basic folder structure

```
yourproject/
├── content
├── output
├── tasks.py
├── Makefile
├── pelicanconf.py       # Main settings file
└── publishconf.py       # Settings to use when ready to publish
```

##### Pelican handles two types of content:

* Pages: the basic parts of the site
* Articles: basically, kind of blogs post

5. Add pages
   Add a about page. create a file with name "about.md" in the folder "content\pages" with the following content:

```
Title: Welcome to Pelican!
Date: 2019-10-20 09:20
Author: Antonello
## Welcome to Pelican
Hello!
```

6. Add articles with different category
   6.1 create subfolders in folder "content". For example, machine-learning
   6.2 create a new markdown files in each subfolder to write articles.
7. Change the default theme to flex
   7.1 clone flex theme to a folder under the root directory
   
   ```
   git clone https://github.com/alexandrevicenzi/Flex.git
   ```
   
   7.2 change the pelicanconf.py

8.Time to publish the website locally

* Build the website

```
pelican
```

* Test the site locally
  We recommend setting`RELATIVE_URLS = True` when testing (do not forget to revert this before deploying) and then executing the following,

```
pelican --listen output
```

A test version of the website will then be available at `http://localhost:8000`

## Step 2 - Deploying to github pages

1. Change `RELATIVE_URLS = False` in pelicanconf.py
2. Prepare GIT as VersionControlSystem

* Create local git repo

```
git init
```

* Create a remote repo via github.com for your github page build in GitHub. Call it`username.github.io`
* Connect to repo and print remote repo

```
git remote add origin https://github.com/username/username.github.io.git
git remote -v
```

* Create new branch for the pelican source

```
git checkout -b content
```

2. Go live with github pages

* Commit to content branch

```
git add .
git commit -a -m "Initial commit"
git push -u origin content
```

* Commit to master branch

```
pelican content -o output -s pelicanconf.py
ghp-import output -r origin -b master
git push origin master
git checkout content
```

[check the website](https://jelly123456.github.io/)

