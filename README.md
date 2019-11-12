# MIT BWSI RACECAR Middle School - Official Website   

This website is made using Sphinx:     
https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html   

GitHub Pages is built from the ```gh-pages``` branch.    
The ```gh-pages``` branch is a subtree of the ```master``` branch.    
Run the following commands below to make edits to the website.     

```git clone```     
Make changes to files in /docs folder. If you delete and rebuild the /_build folder, make sure that you re-add the .nojekyll file to the /_build/html folder so that the website css can be displayed properly.          
```make html``` (to build the /_build folder)     
```git add <files_changed>```     
```git commit -m "<commit_message>"```     
```git push```     
```git subtree push --prefix _build/html origin gh-pages```     