"""Spider for authenticating and downloading master branches of repos."""
import scrapy
from github_code.items import GithubCodeItem


class LoginSpider(scrapy.Spider):
    """Spider to download repos."""
    name = 'github'
    start_urls = ['https://github.com/login']
    username = 'chaudry.arslan.mansha@gmail.com'
    password = 'Astaghfirullah33'

    def parse(self, response):
        """Authenticates user credentials."""
        authenication_token = response.xpath('//input[@name="authenticity_token"]/@value').extract_first()
        form_data = {
            "commit": 'Sign in',
            "authenticity_token": authenication_token,
            "login": self.username,
            "password": self.password
        }
        yield scrapy.FormRequest("https://github.com/session", formdata=form_data, callback=self.after_login)

    def after_login(self, response):
        """Parses the link to repos."""
        item = GithubCodeItem()
        if response.url == "https://github.com/session":
            item["authentication_status"] = 'Failed'
            yield item
            return

        item["authentication_status"] = 'Successful'
        repos = response.xpath('//div[@class="width-full text-bold"]/a/@href').extract()
        for repo in repos:
            yield response.follow(repo, callback=self.parse_repo, meta={"item": item})

    def parse_repo(self, response):
        """Parses the repo details."""
        item = response.meta['item']
        name = response.xpath('//a[@data-pjax="#js-repo-pjax-container"]/text()').extract_first()
        download_link = "https://codeload.github.com/ArslanMansha/{}/zip/master".format(name)
        item['name'] = name
        item["repo_clone_url"] = response.xpath('//div[@class="input-group"]/input/@value').extract()[-1]
        item["repo_download_link"] = download_link
        yield item
