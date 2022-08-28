import requests, re
from os import system
from bs4 import BeautifulSoup as bs


class Package:
    def __init__(self, pip='pip'):
        self.pip = pip

    def search(self, query) -> dict | None:
        response = requests.get(f'https://pypi.org/project/{query}')
        soup = bs(response.content, 'html.parser')

        Navigation = soup.find('div', attrs={'class': 'vertical-tabs__panel'})
        ProjectDescription = Navigation.find('div', attrs={'id': 'description'}).get_text().strip()
        History = Navigation.find('div', attrs={'id': 'history'})
        ReleaseTimeLine = History.find('div', attrs={'class': 'release-timeline'})
        ReleaseTimeLineCurrent = ReleaseTimeLine.find('div', attrs={'class': 'release release--latest release--current'})
        ReleaseTimeLineCurrentVersion = ReleaseTimeLineCurrent.a.find('p', attrs={'class': 'release__version'}).text.strip()
        ReleaseTimeLineCurrentDate = ReleaseTimeLineCurrent.a.find('p', attrs={'class': 'release__version-date'}).time.text.strip()
        Release = ReleaseTimeLine.find_all('div', attrs={'class': 'release'})

        return {
            'name': query,
            'Project.Description': ProjectDescription,
            'Release.TimeLine': [[i.a.find('p', attrs={'class': 'release__version'}).text.strip(), i.a.find('p', attrs={'class': 'release__version-date'}).time.text.strip()] for i in Release],
            'Release.TimeLine.Current.Version': ReleaseTimeLineCurrentVersion,
            'Release.TimeLine.Current.Date': ReleaseTimeLineCurrentDate
        }
    def install(self, package_name) -> Exception | None | str:
        match self.pip:
            case "pip":
                system(f"{self.pip} install {package_name}")
            case "pip3":
                system(f"{self.pip} install {package_name}")
            case _:
                raise ValueError("pip command name not found")


    def include(self) -> Exception | None:
        return __import__(self.package_name)


if __name__ == "__main__":
    pkg = Package()
    print(pkg.search("flask")["Project.Description"])
    pkg.install("flask")