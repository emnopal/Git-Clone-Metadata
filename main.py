import requests
import argparse
import json
import os
from datetime import datetime

class GitClone:
    
    def __init__(self, url):
        self._APIbaseUrl = 'https://api.github.com/repos'
        self.url = url
        if ".git" not in self.url:
            self.url += ".git"
        else:
            self.url
        self.github_username, self.repository_name = self.url[:-4].split('/')[-2:]
        self.res = requests.get(f'{self._APIbaseUrl}/{self.github_username}/{self.repository_name}')
        self.now = datetime.now()
        self.dt_string = self.now.strftime("%d-%m-%Y-%H-%M-%S")
        self.filename_format = f"{self.repository_name}-{self.dt_string}.json"

    def fetch_id(self):
        repository_id = self.res.json().get('id')
        print("Repository ID: {}".format(repository_id))
    
    def fetch_name(self):
        repository_name = self.res.json().get('name')
        print("Repository Name: {}".format(repository_name))

    def fetch_date(self):
        repository_create = self.res.json().get('created_at')
        repository_update = self.res.json().get('updated_at')
        repository_push = self.res.json().get('pushed_at')
        print("Repository Created at: {}".format(repository_create))
        print("Repository Updated at: {}".format(repository_update))
        print("Repository Pushed at: {}".format(repository_push))
        
    def fetch_size(self):
        repository_size = self.res.json().get('size')
        if repository_size < 1000:
            print("Repository Size: {} KB".format(repository_size))
        else:
            print("Repository Size: {} MB".format(repository_size/1000))
        
    def fetch_license(self):
        repository_license = self.res.json().get('license')['name']
        print("Repository License: {}".format(repository_license))

    def fetch_desc(self):
        repository_desc = self.res.json().get('description')
        print("Repository Desc: {}".format(repository_desc))
    
    def fetch_lang(self):
        repository_lang = self.res.json().get('language')
        print("Repository Language: {}".format(repository_lang))

    def fetch_minimal(self):
        print("Metadata: ")
        self.fetch_id()
        self.fetch_name()
        self.fetch_lang()
        self.fetch_size()
        self.fetch_license()
        self.fetch_date()
        self.fetch_desc()
    
    def fetch_all(self):
        self.repository_size = self.res.json()
        print(self.repository_size)
    
    def show_fetch(self, show):
        show_list = ["no", "minimal", "all" , "id", "name", "lang", "size", "license", "date", "desc"]
        if show in [show_list[0], "0"]:
            pass
        elif show in [show_list[1], "min", "8"]:
            self.fetch_minimal()
        elif show in [show_list[2], "9"]:
            self.fetch_all()
        elif show in [show_list[3], "1"]:
            self.fetch_id()
        elif show in [show_list[4], "2"]:
            self.fetch_name()
        elif show in [show_list[5], "3"]:
            self.fetch_lang()
        elif show in [show_list[6], "4"]:
            self.fetch_size()
        elif show in [show_list[7], "5"]:
            self.fetch_license()
        elif show in [show_list[8], "6"]:
            self.fetch_date()
        elif show in [show_list[9], "7"]:
            self.fetch_desc()
        else:
            pass

    def save(self, show, save):
        if save in ["0", "no", "False", "false"]:
            self.show_fetch(show)
        elif save in ["yes", "1", "default_format", "default", "True", "true"]:
            self.show_fetch(show)
            with open(self.filename_format, 'w') as f:
                json.dump(self.res.json(), f)
        else:
            self.show_fetch(show)
            with open(save+".json", 'w') as f:
                json.dump(self.res.json(), f)

    def shows(self, show, save, clone):
        if clone in ["0", "no", "false", "False"]:
            self.save(show, save)
        elif clone in ["yes", "1", "True", "true"]:
            self.save(show, save)
            os.system(f"git clone {self.url}")
        else:
            pass

if __name__ == "__main__":
    
    default = "no"
    parser = argparse.ArgumentParser(description='Git Clone Info')
    parser.add_argument('--url', type=str, help='The URL', required=True)
    parser.add_argument('--show', type=str, help='Show All', default=default)
    parser.add_argument('--save', type=str, help='Save to JSON', default=default)
    parser.add_argument('--clone', type=str, help='Cloning the Repository', default=default)

    args = parser.parse_args()

    git = GitClone(args.url)

    git.shows(args.show, args.save, args.clone)
