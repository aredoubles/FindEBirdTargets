from ebird import AvianKnowledge
from ebird import EBird

ak = AvianKnowledge()
ebird = EBird()

'''
The forked eBird API repo seems to only support 'subnational1', which is the state level
subnational2 is the county level
'''

#print ak.subnational1_list({'countryCode': 'US'})
lapland = ebird.recent_species_observations_region('subnational1', 'US-MA', 'Calcarius lapponicus')

laplandrecs = {}
for rec in lapland:
    laplandrecs[rec['obsDt']] = rec['locName']

laplandlocs = list(laplandrecs.values())


snowbun = ebird.recent_species_observations_region('subnational1', 'US-MA', 'Plectrophenax nivalis')

snowrecs = {}
for rec in snowbun:
    snowrecs[rec['obsDt']] = rec['locName']

snowlocs = list(snowrecs.values())

# 'Set' with an ampersand returns shared values!!!
both = set(laplandlocs) & set(snowlocs)

# What if I give 3+ species, and the best location only has no greater than 2 of them?
