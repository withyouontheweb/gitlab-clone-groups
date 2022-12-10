# gitlab-clone-groups

a script that clones all documents in a gitlab group.
a backup script that can be launched automatically.

the script has only been tested on windows 10 and 11 but should theoretically work on other operating systems

### first installation

1.  Install Python, Pip, git.
2.  on gitlab.com, create an "access token", the name of the token does not matter, however, it must be assigned all scopes for security.     Even if in theory only the call to the API will suffice. Then select "never expires".
3.  know the id of the group you want to clone, you can find it under the group on gitlab.com
4.  create an ssh key on the computer:
    **ssh-keygen -t ed25519 -C "Git-Demo"**
    and insert it in the corresponding gitlab.com topic “ssh keys”
5.  open powershell in admin mode then:
    **Get-Service ssh-agent | Set-Service -StartupType Automatic -PassThru | Start-Service**
    then add your previously created ssh keys to the ssh service like this:
    **ssh-add C:\Users\sylva/.ssh\id_ed25519**
    then:
    **git config --global core.sshCommand C:/Windows/System32/OpenSSH/ssh.exe**
6.  Finally in the python script modify the “access token” and “group id”.
7.  restart the computer
8.  click on the script to launch it

