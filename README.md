# rms-website
MIT BWSI RACECAR Middle School - Official Website .  

The GitHub Pages site is currently being built from the ```gh-pages``` branch.    
The ```gh-pages``` branch is a subtree off the ```master``` branch.    
Run the following commands below to make edits to the website.     

```git clone```     
*make changes to files in /docs folder*     
```make html``` (to build the /_build folder)     
```git add <files_changed>```     
```git commit -m "<commit_message>"```     
```git push```     
```git subtree push --prefix _build/html origin gh-pages```     