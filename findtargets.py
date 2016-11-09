#from ebird import AvianKnowledge
from ebird import EBird
import pprint
import pandas as pd
from scipy.stats import itemfreq

#ak = AvianKnowledge()
ebird = EBird()

'''
The forked eBird API repo seems to only support 'subnational1', which is the state level
subnational2 is the county level
'''

#print ak.subnational1_list({'countryCode': 'US'})

spp1 = input('Species 1: ')
spp2 = input('Species 2: ')
state = input('US State: ')

def GetSites(spp1, spp2):
    encstate = 'US-' + state
    recs1 = ebird.recent_species_observations_region('subnational1', encstate, spp1)
    recs2 = ebird.recent_species_observations_region('subnational1', encstate, spp2)

    locs1 = {}
    locs2 = {}
    for rec in recs1:
        locs1[rec['obsDt']] = rec['locName']
    for rec in recs2:
        locs2[rec['obsDt']] = rec['locName']

    countloc1 = pd.DataFrame(itemfreq(locs1.values()))
    countloc2 = pd.DataFrame(itemfreq(locs2.values()))

    countloc1.columns = ['Location', spp1]
    countloc2.columns = ['Location', spp2]

    ''''''
    # Figure out how to merge these two tables
    # http://pandas.pydata.org/pandas-docs/stable/merging.html
    bestloc = pd.merge(countloc1, countloc2, on='Location', how='outer', copy=True)
    # Need to change NAs to zeros
    bestloc = bestloc.fillna(0)
    # Make sure the sightings counts are numeric
    bestloc[[spp1, spp2]] = bestloc[[spp1, spp2]].apply(pd.to_numeric)
    bestloc['Total Sightings'] = bestloc[spp1] + bestloc[spp2]
    bestloc = bestloc.sort_values(by='Total Sightings', ascending=0)

    bestloc = bestloc.set_index('Location')

    return bestloc

thesites = GetSites(spp1, spp2)
pprint.pprint(thesites.head(6))

'''
Need to extend inputs for 3+ species, using **kwargs
'''
