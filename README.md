# lib-version: Version Aware Library

A simple Python library designed to be version-aware. It automatically determines its version from Git tags during the build process using `setuptools-scm`. This library is a component of the REMLA (Reliable Machine Learning Applications) course project.

## Installation

This library is installed directly from its GitHub repository using release tags (e.g., `v0.1.0`).

**Option 1: Direct pip install**

Install the library directly using pip:

```bash
pip install https://github.com/remla25-team5/lib-version/releases/download/\<version\>/\<wheel-filename\>
```

Then install dependencies: pip install -r requirements.txt

**Option 2: Add to requirements**

Add the following line to your project's `requirements.txt`. Replace `<tag>` with the specific release version you want to use (like `v0.1.0`):

```txt
lib-version @ https://github.com/remla25-team5/lib-version/releases/download/\<version\>/\<wheel-filename\>
```
