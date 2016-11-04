# Finding eBird Targets

[Python eBird Wrapper gratiously forked from Carson McDonald](https://github.com/carsonmcdonald/python-ebird-wrapper)

I just moved to New England. There's lots of birds that I want to see! With so many targets, where can I go to find many/most of them at once?

We can use the eBird API to find out!

## Goals

* User provides a list of bird species, and a US state
* Script returns a list of locations where those bird species have been seen recently, within the given region
    * eBird API used to assess where each species has been seen recently
    * Location lists then compared within Python
* Could be implemented as a script, or even as a web-app down the line

## Current progress

* The `findtargets.py` file is now a script, where you input two species, and it returns a dict of which locations one or both have been seen at most often, in Massachusetts.

```
python findtargets.py
Species 1: 'Alca torda'
Species 2: 'Plectrophenax nivalis'
```
```
[(u'Race Point Beach, Provincetown', 2),
 (u'Parker River NWR', 2),
 (u'Race Point', 2),
 (u'Great Meadows NWR--Concord Unit', 2),
 (u"Andrew's Point, Rockport", 2),
 (u'Salem Wharf and Harbor', 1),
 (u'High Head, Pilgrim Heights', 1),
 (u'Quabbin Park', 1),
 (u'Indian Lake, Becket (restricted access)', 1),
 (u'US-Massachusetts-Salisbury-Z Street - 42.826x-70.82', 1),
 (u'Wachusett Reservoir - Gates 36 - 38', 1),
 ...
 ```

## Todo

* Should support 3+ species, probably using a `**kwargs` input
* Might want to shorten the output dict in some way
* Down the road, a webapp would be awesome

## Footnotes
* Roger Shaw
* Currently a fellow at Insight Health Data Science, transitioning from academia into a career in data science
* This is just a side project, for playing around with the eBird API, and the usage of `**kwargs`. Making a new webapp would be fun practice too.
* As can be inferred from this project's goals, I'm an avid birder in my spare time, and so this project was borne out of my own need for this tool!
