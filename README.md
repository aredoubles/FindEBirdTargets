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

* The `findtargets.py` file is more like a notebook, not a script
    * Shows locations in Massachusetts where both Lapland Longspurs and Snow Buntings have been seen in the past 30 days

## Todo

* Massage notebook-style code into an actual script, with inputs
    * Should support 3+ species, probably using a **kwargs input
* Figure out what to do when there are no 'ideal best' locations (find next best somehow)
* Down the road, a webapp would be awesome
