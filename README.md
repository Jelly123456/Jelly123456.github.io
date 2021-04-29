# Environment setup

```
conda create --name blog python=3
conda activate blog
pip install pelican markdown typogrify ghp-import
```

# Build the blog

```
pelican
```

# Test the blog locally

```
pelican --listen output
```

