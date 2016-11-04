#from ebird import AvianKnowledge
from ebird import EBird

#ak = AvianKnowledge()
ebird = EBird()

'''
The forked eBird API repo seems to only support 'subnational1', which is the state level
subnational2 is the county level
'''

#print ak.subnational1_list({'countryCode': 'US'})

spp1 = input('Species 1: ')
spp2 = input('Species 2: ')

def GetSites(spp1, spp2):

    recs1 = ebird.recent_species_observations_region('subnational1', 'US-MA', spp1)
    recs2 = ebird.recent_species_observations_region('subnational1', 'US-MA', spp2)

    locs1 = {}
    locs2 = {}
    for rec in recs1:
        locs1[rec['obsDt']] = rec['locName']
    for rec in recs2:
        locs2[rec['obsDt']] = rec['locName']

    '''
    ## This is where I evaluate the best sites
    * Could count how many times a location shows up amongst both lists
        * But one species could be super-reliable at one site and bias that
            * Maybe that's okay?
    * Purely check for intersection of sets, as before
        * Doesn't factor in reliability, but maybe that's okay?
    * What other metrics would make sense?
    * For now, let's go with the sheer count
    '''

    countloc = {}
    for rec in locs1.values():
        if rec in countloc:
            countloc[rec] += 1
        else:
            countloc[rec] = 1
    for rec in locs2.values():
        if rec in countloc:
            countloc[rec] += 1
        else:
            countloc[rec] = 1

    # How to sort countloc by highest value?
    bestloc = sorted(countloc.items(), key=lambda x: x[1], reverse=True)

    # 'Set' with an ampersand returns shared values!!!
    #both = set(laplandlocs) & set(snowlocs)
    # Analagous to:
    #both = set(laplandlocs).intersection(snowlocs)

    return bestloc

thesites = GetSites(spp1, spp2)
print thesites

'''
Need to extend inputs for 3+ species, using **kwargs
'''
