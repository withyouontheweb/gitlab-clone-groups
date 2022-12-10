# -------------- Program modified on 2/12/2022 by Sylvain [free software with no licence] --------------

import requests
import subprocess, shlex
import os
import urllib3




# we suppress the warning of web browser url
urllib3.disable_warnings()



def main():

    print("Programm starting")

    # main data
    group_id="your_group_id_here"
    gitlab_url="https://gitlab.com"
    token="your_access_token_here"
    
    # get current directory
    pathtodir = os.getcwd() 

    print("Backup is starting ...")

    total_pages = 1
    page = 0
    while page < total_pages:
        page += 1
        
        # get response api from gitlab
        response = requests.get(
            f"{gitlab_url}/api/v4/groups/{group_id}/projects?private_token={token}&include_subgroups=True&per_page=100&page={page}&with_shared=False", verify=False)
        for project in response.json():
            path = project['path_with_namespace']
            ssh_url_to_repo = project['ssh_url_to_repo']
            default_branch = project['default_branch']
            id = project['id']


            # choose between clone or pull
            try:
                if not os.path.exists(path):
                     
                     #sub-branches loop

                     total_pages_sousbranches = 1
                     page_sousbranches = 0

                     while page_sousbranches < total_pages_sousbranches:
                         page_sousbranches += 1

                         response_sousbranches = requests.get(
                             f"{gitlab_url}/api/v4/projects/{id}/repository/branches?private_token={token}",
                             verify=False)

                         for project_sousbranches in response_sousbranches.json():
                             name_sousbranches = project_sousbranches['name']

                             pathsousbranches = path + "/" + name_sousbranches + "/"

                             
                             command = shlex.split(
                                 f"git clone --branch {name_sousbranches} {ssh_url_to_repo} {pathsousbranches}")
                             subprocess.Popen(command)

                         total_pages_sousbranches = int(response_sousbranches.headers['X-Total-Pages'])





                else:
                    

                     
                     #sub-branches loop

                     total_pages_sousbranches = 1
                     page_sousbranches = 0

                     while page_sousbranches < total_pages_sousbranches:
                         page_sousbranches += 1

                         response_sousbranches = requests.get(
                             f"{gitlab_url}/api/v4/projects/{id}/repository/branches?private_token={token}",
                             verify=False)

                         for project_sousbranches in response_sousbranches.json():
                             name_sousbranches = project_sousbranches['name']

                             pathsousbranches = path + "/" + name_sousbranches

                             pathfinal= pathtodir + "/" + pathsousbranches 


                             
                             os.chdir(pathfinal)


                             command = shlex.split(f" git pull")
                             subprocess.Popen(command)


                         total_pages_sousbranches = int(response_sousbranches.headers['X-Total-Pages'])




            except Exception as e:
                print(f"{e}")


    

        total_pages = int(response.headers['X-Total-Pages'])

    

if __name__ == '__main__':

    main()
