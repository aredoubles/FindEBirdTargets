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

* The `findtargets.py` file is now a script, where you input two species and US state, and it returns a table of which locations they have been seen at in the past 30 days, sorted by the number of total sightings.

```
> python findtargets.py
Species 1: 'Plectrophenax nivalis'
Species 2: 'Spizelloides arborea'
US State: 'MA'
```
```
                                   Plectrophenax nivalis    Spizelloides arborea    Total Sightings
Location
Great Meadows NWR--Concord Unit                        2                       1                  3
UMass Marine Station                                   1                       1                  2
Parker River NWR                                       1                       1                  2
Salisbury Beach State Reservation                      1                       1                  2
Sandy Neck                                             1                       1                  2
Scusset Beach State Reservation                        1                       1                  2
 ```

## Todo

* Should support 3+ species, probably using a `**kwargs` input
* Would be great to support other geographic scales, but the API makes that slightly tricky, not high priority
* Down the road, a webapp would be awesome

## Footnotes
* Roger Shaw
* Currently a fellow at Insight Health Data Science, transitioning from academia into a career in data science
* This is just a side project, for playing around with the eBird API, and the usage of `**kwargs`. Making a new webapp would be fun practice too.
* As can be inferred from this project's goals, I'm an avid birder in my spare time, and so this project was borne out of my own need for this tool!
