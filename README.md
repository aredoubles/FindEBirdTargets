# Finding eBird Targets

I just moved to New England. There's lots of birds that I want to see! With so many targets, where can I go to find many/most of them at once?

For finding a single species, the eBird website makes it easy with its [Species Maps](http://ebird.org/ebird/map/snobun?neg=true&env.minX=&env.minY=&env.maxX=&env.maxY=&zh=false&gp=false&ev=Z&mr=1-12&bmo=1&emo=12&yr=all&byr=1900&eyr=2016). But if there's multiple species you're interested in, it takes a lot of mental organizatation to keep everything straight.

So I built a tool to do it all for me!

## Goals

- User provides a list of bird species, and a US state
- Script returns a list of locations where those bird species have been seen recently, within the given region

  - eBird API used to assess where each species has been seen recently
  - Location lists then compared within Python

- Could be implemented as a script, or even as a web-app down the line

## Current progress

- The `findtargets.py` file is now a script, where you input as many species as you'd like, plus a US state, and it returns a table of which locations they have been seen at in the past 30 days, sorted by the number of total sightings.
- Allows for input of common names, but the API requires scientific names, so lookup is performed from the [eBird/Clements checklist](http://www.birds.cornell.edu/clementschecklist/download/).
- To run, clone/download this repository, then navigate to that folder from the command line.

```
> python findtargets.py
Enter the names of species that you're interested in, separated by commas
Species: Snow Bunting, American Tree Sparrow, Horned Lark
What state are you searching in?
US State: MA
```

```
Here's where these species have been seen in the past 30 days:

                                    Snow Bunting American Tree Sparrow  Horned Lark Total Sightings
Location
Parker River NWR                               9                     6            6              21
Wachusett Reservoir                            4                     0            5               9
Quabbin Area                                   6                     1            1               8
Race Point                                     2                     1            2               5
Great Meadows NWR--Concord Unit                2                     1            1               4
Salisbury Beach State Reservation              1                     1            1               3
```
Success! I found all three of these species together with the help of this script! Here's a photo I took of one of the Snow Buntings:
![Snow Bunting](https://c2.staticflickr.com/6/5639/30899543702_011276cc0b_z_d.jpg)


## Todo

- Making this into a web-app would be great! Much more user-friendly that way.
    - Would allow for the locations to be shown on a map, or at least links to the eBird hotspots (if applicable)
- Similar locations are being manually merged right now, based on local knowledge. Need to think about whether it's possible to automate in some way, or if it will always need to be curated.
    - Interactive merging would be even better, but beyond the scope of my current UI skills
- Would be great to support other geographic scales (counties, whole countries, etc.), but the API makes that slightly tricky, not high priority
    - Currently only works for the US, sorry! International support would probably be pretty simple, I just haven't looked into it yet
- Would be nice to support entry of scientific names as well, but generally not used by recreational birders, not high priority

## Footnotes

- Roger Shaw
- Currently a fellow at Insight Health Data Science, transitioning from academia into a career in data science
- This is just a side project, for playing around with the eBird API. Making a new webapp would be fun practice too.
- As can be inferred from this project's goals, I'm an avid birder in my spare time, and so this project was borne out of my own need for this tool!
- [Python eBird Wrapper gratiously forked from Carson McDonald](https://github.com/carsonmcdonald/python-ebird-wrapper)
