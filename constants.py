import json

with open('config.json', 'r') as config_file:
    CONFIG = json.load(config_file)

OPENAI_CONFIG = CONFIG['openai']
OLLAMA_CONFIG = CONFIG['ollama']
AGENT_CONFIG = CONFIG['agent']
HOUSE_DATA_CONFIG = CONFIG['house_data']
GEOLOCATOR_CONFIG = CONFIG['geolocator']

US_STATE_ABBREV = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
    'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
    'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
    'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO',
    'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
    'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH',
    'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
    'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
}

ABBREV_TO_US_STATE = {v: k for k, v in US_STATE_ABBREV.items()}

NEIGHBORING_STATES = {
    'AL': ['FL', 'GA', 'MS', 'TN'], 'AK': [], 'AZ': ['CA', 'NM', 'NV', 'UT'],
    'AR': ['LA', 'MO', 'MS', 'OK', 'TN', 'TX'], 'CA': ['AZ', 'NV', 'OR'],
    'CO': ['KS', 'NE', 'NM', 'OK', 'UT', 'WY'], 'CT': ['MA', 'NY', 'RI'],
    'DE': ['MD', 'NJ', 'PA'], 'FL': ['AL', 'GA'], 'GA': ['AL', 'FL', 'NC', 'SC', 'TN'],
    'HI': [], 'ID': ['MT', 'NV', 'OR', 'UT', 'WA', 'WY'], 'IL': ['IN', 'IA', 'KY', 'MO', 'WI'],
    'IN': ['IL', 'KY', 'MI', 'OH'], 'IA': ['IL', 'MN', 'MO', 'NE', 'SD', 'WI'],
    'KS': ['CO', 'MO', 'NE', 'OK'], 'KY': ['IL', 'IN', 'MO', 'OH', 'TN', 'VA', 'WV'],
    'LA': ['AR', 'MS', 'TX'], 'ME': ['NH'], 'MD': ['DE', 'PA', 'VA', 'WV'],
    'MA': ['CT', 'NH', 'NY', 'RI', 'VT'], 'MI': ['IN', 'OH', 'WI'],
    'MN': ['IA', 'ND', 'SD', 'WI'], 'MS': ['AL', 'AR', 'LA', 'TN'],
    'MO': ['AR', 'IL', 'IA', 'KS', 'KY', 'NE', 'OK', 'TN'],
    'MT': ['ID', 'ND', 'SD', 'WY'], 'NE': ['CO', 'IA', 'KS', 'MO', 'SD', 'WY'],
    'NV': ['AZ', 'CA', 'ID', 'OR', 'UT'], 'NH': ['ME', 'MA', 'VT'],
    'NJ': ['DE', 'NY', 'PA'], 'NM': ['AZ', 'CO', 'OK', 'TX', 'UT'],
    'NY': ['CT', 'MA', 'NJ', 'PA', 'VT'], 'NC': ['GA', 'SC', 'TN', 'VA'],
    'ND': ['MN', 'MT', 'SD'], 'OH': ['IN', 'KY', 'MI', 'PA', 'WV'],
    'OK': ['AR', 'CO', 'KS', 'MO', 'NM', 'TX'], 'OR': ['CA', 'ID', 'NV', 'WA'],
    'PA': ['DE', 'MD', 'NJ', 'NY', 'OH', 'WV'], 'RI': ['CT', 'MA'],
    'SC': ['GA', 'NC'], 'SD': ['IA', 'MN', 'MT', 'NE', 'ND', 'WY'],
    'TN': ['AL', 'AR', 'GA', 'KY', 'MS', 'MO', 'NC', 'VA'],
    'TX': ['AR', 'LA', 'NM', 'OK'], 'UT': ['AZ', 'CO', 'ID', 'NM', 'NV', 'WY'],
    'VT': ['MA', 'NH', 'NY'], 'VA': ['KY', 'MD', 'NC', 'TN', 'WV'],
    'WA': ['ID', 'OR'], 'WV': ['KY', 'MD', 'OH', 'PA', 'VA'],
    'WI': ['IL', 'IA', 'MI', 'MN'], 'WY': ['CO', 'ID', 'MT', 'NE', 'SD', 'UT']
}