# MIT BWSI RACECAR Middle School - Official Website   

This website is made using Sphinx:     
https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html   

### Manual process to verify as necessary

GitHub Pages is built from the ```gh-pages``` branch.    
The ```gh-pages``` branch is a subtree of the [default branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches#about-the-default-branch).    
Run the following commands below to make edits to the website.     

```git clone```     
Make changes to files in /docs folder. If you delete and rebuild the /_build folder, make sure that you re-add the .nojekyll file to the /_build/html folder so that the website css can be displayed properly.          
```make html``` (to build the /_build folder)     
```git add <files_changed>```     
```git commit -m "<commit_message>"```     
```git push```     
```git subtree push --prefix _build/html origin gh-pages```

If there are git subtree issues, force overwrite remote with local (use this with caution):
```git push origin `git subtree split --prefix _build/html origin`:gh-pages --force```

### Github actions, automatic process

This repo also is setup for github actions.

The docs will build automatically on merge to the default branch and the gh-pages site will automatically be updated with the changes.

---
**To ensure that this happens the owner of main repo should:**

    * Add Personal Access Token under developer settings, make a note of or copy token for the next step
    * Add it as secret named TOKEN_MITLL_RACECAR in target repo
    * Merge to default branch and gh-pages will build

To make changes simply:
```git clone```

Make changes to the file in the docs folder, when complete type `make html` per the Sphinx instructions and verify the changes deployed by opening the below file in a browser:
``
_build/index.html
``

If everything looks good and you are ready to deploy then type:
```
make clean
```
The _build file is not needed for the automatic process.

Then:
```git add <files_changed>```     
```git commit -m "<commit_message>"```     
```git push```     

## Assumptions

You have:
    * a modern version of python installed > 3.7
    * Sphinx and the sphinx-rtd-theme installed `python -m pip install -r requirements.txt`
