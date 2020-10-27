# Learning GitHub
### This repository will be my document to track myself learning github

helpful link: https://pages.github.ibm.com/jumpstart-developer-labs/fly-tello-python-boilerplate/  
Other helpful links: https://guides.github.com/introduction/git-handbook/  
Git cheatsheet: https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet  
Youtube tutorial: https://www.youtube.com/watch?v=oFYyTZwMyAg      
MD basic syntax: https://www.markdownguide.org/basic-syntax/

## 1. setup SSH Key
go to the following link to: https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
1. set up new SSH key
  a. ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  b. Enter a file in which to save the key (/Users/you/.ssh/id_rsa): [Press enter] (I put like .ssh/id_git)
  c. Put or skip passphase 

2. Make sure identity file is set up properly
  ssh-add -K ~/.ssh/id_rsa (change 'id_rsa' to whatever it is called that contains your new ssh key)
3. Add new SSH key
  link: https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account <br />
  a. go to settings --> SSH and GPG keys --> New SSH key --> Paste SSH Key --> save <br />
  b. go to terminal and <br />
    pbcopy < ~/.ssh/id_rsa.pub (change 'id_rsa.pub' to whatever it is called that contains your new ssh key)
    This copies the contents of the id_rsa.pub file to your clipboard

## 2. Cloning First Repository
Navigate to the repository you want to clone <br />
Click the 'Clone or download' button <br />
In your terminal: <br />
navigate to the folder you want the repository to appear in (for me it's cd ~Git/Main) <br />
git clone {clone_URL}  # Replace {clone_URL} with the URL you copied above. <br />

## 3. Working with Git inside cloned repository
git pull : update your cloned repository with the latest updates from the MAIN online branch <br />
git add filename <br />
git rm filename <br />
git commit -m "put comments here" filename <br />
git push : do this to push your changes to the main branch <br />
git init : create a new repository <br />

## 4. Git merge issues
If you run into this issue:  
! [rejected]        master -> master (fetch first).   
error: failed to push some refs to 'https://github.com/liuy0311/helloworld.git'.  

solution:  
git add filename (that was modified). 
git commit -m "comment" filename. 
git push  
git pull  

the first part is the stuff that was added  
underneath '======' is the stuff that was there before. 

<<<<<<< HEAD
This is the result of the local edits to this section of code
-------
This is the result of the edits you are trying to merge in
>>>>>>> other_branch

you can also do:  
git stash : to put merges to the side and come back to that later
