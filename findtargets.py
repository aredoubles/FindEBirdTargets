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

# print ak.subnational1_list({'countryCode': 'US'})

spp1 = input('Species 1: ')
spp2 = input('Species 2: ')
state = input('US State: ')


def GetSites(spp1, spp2):
    encstate = 'US-' + state
    recs1 = ebird.recent_species_observations_region(
        'subnational1', encstate, spp1)
    recs2 = ebird.recent_species_observations_region(
        'subnational1', encstate, spp2)

    locs1 = {}
    locs2 = {}
    for rec in recs1:
        SiteDupes(rec)
        locs1[rec['obsDt']] = rec['locName']
    for rec in recs2:
        SiteDupes(rec)
        locs2[rec['obsDt']] = rec['locName']
    com1 = recs1[0]['comName']
    com2 = recs2[0]['comName']

    countloc1 = pd.DataFrame(itemfreq(locs1.values()))
    countloc2 = pd.DataFrame(itemfreq(locs2.values()))

    countloc1.columns = ['Location', com1]
    countloc2.columns = ['Location', com2]

    # countloc1.sort_values(by='Snow Bunting', ascending=0)

    ''''''
    # Figure out how to merge these two tables
    # http://pandas.pydata.org/pandas-docs/stable/merging.html
    bestloc = pd.merge(countloc1, countloc2, on='Location',
                       how='outer', copy=True)
    # Need to change NAs to zeros
    bestloc = bestloc.fillna(0)
    # Make sure the sightings counts are numeric
    bestloc[[com1, com2]] = bestloc[[com1, com2]].apply(pd.to_numeric)
    bestloc['Total Sightings'] = bestloc[com1] + bestloc[com2]
    bestloc = bestloc.sort_values(by='Total Sightings', ascending=0)

    bestloc = bestloc.set_index('Location')

    return bestloc


def SiteDupes(rec):
    if (rec['locName'].startswith('Parker River N')) or (rec['locName'].startswith('Plum Island')) or (rec['locName'].startswith('Sandy Point State')):
        rec['locName'] = 'Parker River NWR'
    if rec['locName'].startswith('Wachusett Res'):
        rec['locName'] = 'Wachusett Reservoir'
    if rec['locName'].startswith('Quabbin'):
        rec['locName'] = 'Quabbin Area'
    if rec['locName'].startswith('Halibut Point'):
        rec['locName'] = 'Halibut Point'
    '''
    Any way to make this checking more generalizable, rather than rely on local MA knowledge?
    Check for general 'startswith' patterns?
    Has to be consistent across species
    '''

thesites = GetSites(spp1, spp2)
pprint.pprint(thesites.head(6))

'''
Need to extend inputs for 3+ species, using **kwargs
'''
