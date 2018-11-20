# Get citations for wikipedia pages
Generate a citations page from a list of given links to wikipedia pages.

## Usage
1. download repo `$ git clone https://github.com/momotofu/grab-citations-for-wikipedia-pages.git`
2. Using the terminal change into repo directory `$ cd <repo path>`
3. Make sure you have [pipenv installed](https://pipenv.readthedocs.io/en/latest/)
4. Install dependencies using `$ pipenv install`
5. Run the python script using `$ python <[name of links file].txt "<string of target format tags>"`
* An example run script: `$ python main.py pages_links.txt "MLA_Style_Manual Chicago_style"`
* Make sure your pages_links.txt file is in the same directory as the
  repo.
* String of target format tags are the acutal HTML ID tags on the citation
  page
6. Once the script has ran, links will be written to a citedLinks.md
   file.
