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


def WhatWhere():
    print '''Enter the names of species that you're interested in, separated by commas \n(ex: Snow Bunting, American Tree Sparrow, Horned Lark)'''
    inp1 = raw_input('Species: ')
    print 'What state are you searching in?'
    state = raw_input('US State: ')

    # Split the input string into each different species to lookup
    inps = inp1.split(', ')

    # Import Clements/eBird checklist
    specieslist = pd.read_csv('eBird_Taxonomy_v2016_9Aug2016.csv')
    specieslist = specieslist.set_index('PRIMARY_COM_NAME')

    # Look up scientific name of each species
    inputs = {}
    for entry in inps:
        inputs[entry] = specieslist.ix[entry]['SCI_NAME']

    # Include 'State' in the input, needs to get passed along with everything else
    inputs['State'] = state

    return inputs


def GetSites(inputs):
    encstate = 'US-' + inputs['State']  # eBird format for states
    bigdf = pd.DataFrame()
    for entry in inputs:
        if entry != 'State':
            try:
                recs1 = ebird.recent_species_observations_region(
                    'subnational1', encstate, inputs[entry])
            except:
                raise Exception(entry + 'not found in eBird!')
            # Get complete record of sightings for this species
            locs = {}
            for rec in recs1:
                SiteDupes(rec)
                locs[rec['obsDt']] = rec['locName']
            # Tabulate frequency of each location in the corpus
            countloc1 = pd.DataFrame(itemfreq(locs.values()))
            countloc1.columns = ['Location', entry]     # Set column names
            countloc1[entry] = countloc1[entry].apply(int)      # Convert to integers (not working?)

            # Merge each species into previous species' tables
            if bigdf.empty: bigdf = countloc1.copy()
            else:
                bigdf = pd.merge(bigdf, countloc1, on='Location',
                                   how='outer', copy=True)

    bigdf = bigdf.fillna(0)        # Replace NAs with zeroes
    bigdf = bigdf.set_index('Location')
    bigdf['Total Sightings'] = bigdf.sum(axis=1)    # 'Total sightings' column sums across all species, that's our metric for 'best'
    bigdf = bigdf.sort_values(by='Total Sightings', ascending=0)

    bestloc = bigdf

    return bestloc


def SiteDupes(rec):
    # Some hotspots could be grouped together, for stronger signals
    if (rec['locName'].startswith('Parker River N')) or (rec['locName'].startswith('Plum Island')) or (rec['locName'].startswith('Sandy Point State')):
        rec['locName'] = 'Parker River NWR'
    if rec['locName'].startswith('Wachusett Res'):
        rec['locName'] = 'Wachusett Reservoir'
    if rec['locName'].startswith('Quabbin'):
        rec['locName'] = 'Quabbin Area'
    if rec['locName'].startswith('Halibut Point'):
        rec['locName'] = 'Halibut Point'
    if rec['locName'].startswith('Race Point'):
        rec['locName'] = 'Race Point'
    if rec['locName'].startswith('Stellwagen'):
        rec['locName'] = 'Stellwagen Bank'
    '''
    Any way to make this checking more generalizable, rather than rely on local MA knowledge?
    Check for general 'startswith' patterns?
    Has to be consistent across species
    Some 'startswith' SHOULDN'T be joined though, like large national parks, etc.
    '''


def main():
    inputs = WhatWhere()
    thesites = GetSites(inputs)
    print '''Here's where these species have been seen in the past 30 days:\n'''
    pprint.pprint(thesites.head(7))
    #thesites.to_csv('output.csv')


main()
