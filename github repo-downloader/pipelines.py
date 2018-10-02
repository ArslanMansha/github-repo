"""Pipelines for downloading and saving details."""
import urllib.request
import json

class GithubCodePipeline(object):
    def open_spider(self, spider):
        """opens json file to write."""
        self.file = open('github_repositaries.jl', 'w')

    def close_spider(self, spider):
        """Closes json file after execution."""
        self.file.close()

    def process_item(self, item, spider):
        """Downloads repos and save them"""
        file_path = '/home/arslan/Documents/github_repo/git_repos_zip_files/{}.zip'.format(item['name'])
        download_status = urllib.request.urlretrieve(item['repo_download_link'], file_path)
        item['repo_download_status'] = {"Path": download_status[0]}
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


