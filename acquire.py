"""
A module for obtaining repo readme and language data from the github API.
Before using this module, read through it, and follow the instructions marked
TODO.
After doing so, run it like this:
    python acquire.py
To create the `data.json` file that contains the data.
"""
import os
import json
from typing import Dict, List, Optional, Union, cast
from bs4 import BeautifulSoup
import requests

from env import github_token, github_username

# TODO: Make a github personal access token.
#     1. Go here and generate a personal access token https://github.com/settings/tokens
#        You do _not_ need select any scopes, i.e. leave all the checkboxes unchecked
#     2. Save it in your env.py file under the variable `github_token`
# TODO: Add your github username to your env.py file under the variable `github_username`
# TODO: Add more repositories to the `REPOS` list below.

#  'enormego/EGOImageLoading',
REPOS = ['DroidPluginTeam/DroidPlugin',
 'angular-app/angular-app',
 'doctrine/event-manager',
 'huluoyang/freecodecamp.cn',
 'spolu/breach_core',
 'doodlewind/jshistory-cn',
 'qunitjs/qunit',
 'facebookarchive/scribe',
 'mcxiaoke/RxDocs',
 'ming1016/study',
 'shu223/iOS-9-Sampler',
 'tckmn/mkcast',
 'boctor/idev-recipes',
 'rsms/fb-mac-messenger',
 'yubo725/flutter-osc',
 'nryoung/algorithms',
 'Boris-Em/BEMCheckBox',
 'rnpm/rnpm',
 'lloyd/node-memwatch',
 'android-cn/android-dev-com',
 'astaxie/build-web-application-with-golang',
 'xtekky/gpt4free',
 'NationalSecurityAgency/ghidra',
 'GitSquared/edex-ui',
 'laurent22/joplin',
 'chubin/cheat.sh',
 'rust-unofficial/awesome-rust',
 'tabler/tabler',
 'nodejs/node-v0.x-archive',
 'koajs/koa',
 'tencentyun/wafer',
 'tj/dox',
 'zcweng/ToggleButton',
 'AnderWeb/discreteSeekBar',
 'mislav/git-deploy',
 'zk00006/OpenTLD',
 'davidkpiano/react-redux-form',
 'jorgebastida/gordon',
 'codestergit/SweetAlert-iOS',
 'remi/her',
 'dchelimsky/rspec-rails',
 'ptmt/react-native-touchbar',
 'datamapper/dm-core',
 'kevingibbon/KGStatusBar',
 'shawnbot/aight',
 'andrewroycarter/TimeScroller',
 'raycmorgan/Mu',
 'peterc/pismo',
 'lobianco/ALMoviePlayerController',
 'steipete/PSTAlertController',
 'heygrady/scss-blend-modes',
 'sinatra/rack-protection',
 'Seldaek/slippy',
 'JakeWharton/retrofit2-rxjava2-adapter',
 'achiurizo/consular',
 'bither/bither-android-lib',
 'dwyl/book',

 'timjansen/minified.js',
 'meiwin/NgKeyboardTracker',
 'microsoftarchive/android-sliding-layer-lib',
 'KieranLafferty/KLNoteViewController',
 'matryer/silk',
 #
 'thingdom/node-neo4j',
 'Freelander/Elephant',
 'adnan-SM/TimelyTextView',
 'eslint/typescript-eslint-parser',
 'Schachte/Mermrender',
 'radicle-dev/radicle-alpha',
 'at-import/toolkit',
 'hiravgandhi/angularjs-rails',
 'inkling/Subliminal',
 'eanplatter/enclave',
 'dchelimsky/rspec-rails',
 'eastee/rebreakcaptcha',
 'ptmt/react-native-touchbar',
 'datamapper/dm-core',
 'kevingibbon/KGStatusBar',
 'etsy/opsweekly',
 'shawnbot/aight',
 'fulcrum-agile/fulcrum',
 'callumboddy/CBZSplashView',
 'Zewo/Venice',
 'Yalantis/JellyToolbar',
 'csswizardry/csswizardry-grids',
 'vuikit/vuikit',
 'vramana/awesome-reasonml',
 'TonicArtos/StickyGridHeaders',
 'younatics/MotionBook',
 'asfktz/autodll-webpack-plugin',
 'FriendsOfSymfony/FOSJsRoutingBundle',
 'contentful-labs/Concorde',
 'race604/WaveLoading',
 'jamesob/tinychain',
 'openexchangerates/money.js',
 'zipmark/rspec_api_documentation',
 'helm/monocular',
 'ptshih/PSCollectionView',
 'zhangxinxu/mobilebone',
 'sporkrb/spork',
 'shehabic/Droppy',
 'AppianZ/multi-picker',
 'xyfeng/XYOrigami',
 'fergiemcdowall/norch',
 'idoco/map-chat',
 'Cleveroad/CRNetworkButton',
 'hons82/THCalendarDatePicker',
 'mamaral/Organic',
 'DrewML/GifHub',
 'csurfer/gitsuggest',
 'inamiy/RxAutomaton',
 'gaugesapp/gauges-android',
 'jieyou/lazyload',
 'ericclemmons/grunt-angular-templates',
 'wardrobecms/wardrobe-archived',
 'shadowhand/git-encrypt',
 'gophercon/2016-talks',
 'postmates/PMKVObserver',
 'laoqiren/web-performance',
 'jtrussell/angular-snap.js']
ex = []




headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        return repo_info.get("language", None)
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_contents = requests.get(get_readme_download_url(contents)).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data2.json", "w"), indent=1)