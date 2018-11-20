# Get citations for wikipedia pages
Generate a citations page from a list of given links to wikipedia pages.

## Usage
1. download repo `https://github.com/momotofu/grab-citations-for-wikipedia-pages.git`
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

## Example output
```markdown
# Citations For Links

### [Jesus](https://en.wikipedia.org/wiki/Jesus)
#### Mla Style Manual
Wikipedia contributors. "Jesus." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 12 Nov. 2018. Web. 20 Nov. 2018.

#### Chicago Style
Wikipedia contributors, "Jesus,"  Wikipedia, The Free Encyclopedia, https://en.wikipedia.org/w/index.php?title=Jesus&oldid=868480365 (accessed November 20, 2018).


### [Metacognition](https://en.wikipedia.org/wiki/Metacognition)
#### Mla Style Manual
Wikipedia contributors. "Metacognition." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 7 Nov. 2018. Web. 20 Nov. 2018.

#### Chicago Style
Wikipedia contributors, "Metacognition,"  Wikipedia, The Free Encyclopedia, https://en.wikipedia.org/w/index.php?title=Metacognition&oldid=867685268 (accessed November 20, 2018).


### [Meditation](https://en.wikipedia.org/wiki/Meditation)
#### Mla Style Manual
Wikipedia contributors. "Meditation." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 19 Nov. 2018. Web. 20 Nov. 2018.

#### Chicago Style
Wikipedia contributors, "Meditation,"  Wikipedia, The Free Encyclopedia, https://en.wikipedia.org/w/index.php?title=Meditation&oldid=869525893 (accessed November 20, 2018).


### [Love](https://en.wikipedia.org/wiki/Love)
#### Mla Style Manual
Wikipedia contributors. "Love." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 4 Nov. 2018. Web. 20 Nov. 2018.

#### Chicago Style
Wikipedia contributors, "Love,"  Wikipedia, The Free Encyclopedia, https://en.wikipedia.org/w/index.php?title=Love&oldid=867218604 (accessed November 20, 2018).


### [Time](https://en.wikipedia.org/wiki/Time)
#### Mla Style Manual
Wikipedia contributors. "Time." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 19 Nov. 2018. Web. 20 Nov. 2018.

#### Chicago Style
Wikipedia contributors, "Time,"  Wikipedia, The Free Encyclopedia, https://en.wikipedia.org/w/index.php?title=Time&oldid=869529675 (accessed November 20, 2018).


### [Semantics](https://en.wikipedia.org/wiki/Semantics)
#### Mla Style Manual
Wikipedia contributors. "Semantics." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 6 Nov. 2018. Web. 20 Nov. 2018.

#### Chicago Style
Wikipedia contributors, "Semantics,"  Wikipedia, The Free Encyclopedia, https://en.wikipedia.org/w/index.php?title=Semantics&oldid=867600764 (accessed November 20, 2018).


### [Science](https://en.wikipedia.org/wiki/Science)
#### Mla Style Manual
Wikipedia contributors. "Science." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 9 Nov. 2018. Web. 20 Nov. 2018.

#### Chicago Style
Wikipedia contributors, "Science,"  Wikipedia, The Free Encyclopedia, https://en.wikipedia.org/w/index.php?title=Science&oldid=868046874 (accessed November 20, 2018).


### [Mathematics](https://en.wikipedia.org/wiki/Mathematics)
#### Mla Style Manual
Wikipedia contributors. "Mathematics." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 13 Nov. 2018. Web. 20 Nov. 2018.

#### Chicago Style
Wikipedia contributors, "Mathematics,"  Wikipedia, The Free Encyclopedia, https://en.wikipedia.org/w/index.php?title=Mathematics&oldid=868648850 (accessed November 20, 2018).


### [Computer programming](https://en.wikipedia.org/wiki/Computer_programming)
#### Mla Style Manual
Wikipedia contributors. "Computer programming." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 16 Nov. 2018. Web. 20 Nov. 2018.

#### Chicago Style
Wikipedia contributors, "Computer programming,"  Wikipedia, The Free Encyclopedia, https://en.wikipedia.org/w/index.php?title=Computer_programming&oldid=869069376 (accessed November 20, 2018).
```
