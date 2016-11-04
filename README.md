# Finding eBird Targets

[Python eBird Wrapper gratiously forked from Carson McDonald](https://github.com/carsonmcdonald/python-ebird-wrapper)

I just moved to New England. There's lots of birds that I want to see! With so many targets, where can I go to find many/most of them at once?

We can use the eBird API to find out!

## Goals

* User provides a list of bird species, and a location
* Script returns a list of locations where those bird species have been seen recently, nearby/within the given location
    * eBird API used to assess where each species has been seen recently
    * Location lists then compared within Python (Pandas?)
* Could be implemented as a script, or even as a web-app down the line

## Current progress

* The `findtargets.py` file is now a script, where you input two species, and it returns a dict of which locations one or both have been seen at most often, in Massachusetts.

## Todo

* Should support 3+ species, probably using a `**kwargs` input
* Might want to shorten the output dict in some way
* Down the road, a webapp would be awesome

## Footnotes
* Roger Shaw
* Currently a fellow at Insight Health Data Science, transitioning from academia into a career in data science
* This is just a side project, for playing around with the eBird API, and possibly another webapp
* As can be inferred from this project's goals, I'm an avid birder in my spare time, and so this project was borne out of my own need for this tool!
