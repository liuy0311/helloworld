# Learning GitHub
## this repository will be my document to track myself learning github

helpful link: https://pages.github.ibm.com/jumpstart-developer-labs/fly-tello-python-boilerplate/


# 1. setup SSH Key
go to the following links to:
1. set up new SSH key
  link: https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
  1. ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  2. Enter a file in which to save the key (/Users/you/.ssh/id_rsa): [Press enter] (I put like .ssh/id_git)
  3. Put or skip passphase 

2. Make sure identity file is set up properly
  ssh-add -K ~/.ssh/id_rsa (change 'id_rsa' to whatever it is called that contains your new ssh key)
3. Add new SSH key
  link: https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account
  go to settings --> SSH and GPG keys --> New SSH key --> Paste SSH Key --> save

  $ pbcopy < ~/.ssh/id_rsa.pub (change 'id_rsa.pub' to whatever it is called that contains your new ssh key)
   Copies the contents of the id_rsa.pub file to your clipboard

# 2. Cloning First Repository
Navigate to the repository you want to clone
Click the 'Clone or download' button
In your terminal:
navigate to the folder you want the repository to appear in (for me it's cd ~Git/Main)
git clone {clone_URL}  # Replace {clone_URL} with the URL you copied above.

# 3. Working with Git inside cloned repository
git pull : update your cloned repository with the latest updates from the MAIN online branch
git add filename
git rm filename
git commit -m "put comments here" filename
git push : do this to push your changes to the main branch
git init : create a new repository
