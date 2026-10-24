import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')
django.setup()

from dealership.models import Dealer

existing = Dealer.objects.count()
if existing >= 50:
    print(f"Already {existing} dealers, nothing to do")
else:
    extra = [
        ('Willow Creek Auto', 'WCA', 'Willow Creek Auto Group', 'Overland Park', 'Kansas', '12 Willow Ln', '66211', 38.9822, -94.6731),
        ('Sunflower Motors', 'SM', 'Sunflower Motors Inc', 'Lawrence', 'Kansas', '88 Sunflower Dr', '66044', 38.9717, -95.2353),
        ('Prairie Star Cars', 'PSC', 'Prairie Star Cars LLC', 'Salina', 'Kansas', '404 Prairie Ave', '67401', 38.8403, -97.6114),
        ('Flint Hills Ford', 'FHF', 'Flint Hills Ford Sales', 'Manhattan', 'Kansas', '900 Flint Hills Blvd', '66502', 39.1836, -96.5717),
        ('Jayhawk Auto Plaza', 'JAP', 'Jayhawk Auto Plaza', 'Topeka', 'Kansas', '1500 Jayhawk Way', '66604', 39.0473, -95.6752),
        ('Lone Star Motors', 'LSM', 'Lone Star Motors Inc', 'Houston', 'Texas', '700 Lone Star Rd', '77001', 29.7604, -95.3698),
        ('Alamo Auto Group', 'AAG', 'Alamo Auto Group', 'San Antonio', 'Texas', '55 Alamo Plaza', '78201', 29.4241, -98.4936),
        ('Bluebonnet BMW', 'BBB', 'Bluebonnet BMW Dealership', 'Fort Worth', 'Texas', '321 Bluebonnet St', '76102', 32.7555, -97.3308),
        ('Gulf Coast Cars', 'GCC', 'Gulf Coast Cars LLC', 'Corpus Christi', 'Texas', '88 Gulf Shore Dr', '78401', 27.8006, -97.3964),
        ('Capitol City Motors', 'CCM', 'Capitol City Motors', 'Austin', 'Texas', '100 Congress Ave', '78701', 30.2672, -97.7431),
        ('Hudson Valley Motors', 'HVM', 'Hudson Valley Motors Inc', 'Albany', 'New York', '45 Hudson Ave', '12207', 42.6526, -73.7562),
        ('Empire Auto Sales', 'EAS', 'Empire Auto Sales', 'Buffalo', 'New York', '22 Empire Blvd', '14201', 42.8864, -78.8784),
        ('Adirondack Motors', 'ADM', 'Adirondack Motors LLC', 'Syracuse', 'New York', '900 Adirondack Way', '13201', 43.0481, -76.1474),
        ('Niagara Auto Plaza', 'NAP', 'Niagara Auto Plaza', 'Niagara Falls', 'New York', '17 Niagara St', '14303', 43.0962, -79.0377),
        ('Liberty City Cars', 'LCC', 'Liberty City Cars', 'New York', 'New York', '350 5th Ave', '10118', 40.7128, -74.0060),
        ('Golden Gate Motors', 'GGM', 'Golden Gate Motors', 'San Francisco', 'California', '34 Golden Gate Ave', '94102', 37.7749, -122.4194),
        ('Sunset Auto Group', 'SAG', 'Sunset Auto Group', 'Los Angeles', 'California', '9020 Sunset Blvd', '90069', 34.0928, -118.3287),
        ('Pacific Coast Cars', 'PCC', 'Pacific Coast Cars Inc', 'San Diego', 'California', '120 Pacific Coast Hwy', '92101', 32.7157, -117.1611),
        ('Silicon Valley Motors', 'SVM', 'Silicon Valley Motors', 'San Jose', 'California', '450 Silicon Valley Dr', '95110', 37.3382, -121.8863),
        ('Yosemite Auto Sales', 'YAS', 'Yosemite Auto Sales', 'Fresno', 'California', '77 Yosemite Pkwy', '93701', 36.7378, -119.7871),
        ('Emerald City Motors', 'ECM', 'Emerald City Motors', 'Seattle', 'Washington', '600 Emerald St', '98101', 47.6062, -122.3321),
        ('Cascade Auto Group', 'CAG', 'Cascade Auto Group', 'Portland', 'Oregon', '12 Cascade Ave', '97201', 45.5152, -122.6784),
        ('Rocky Mountain Motors', 'RMM', 'Rocky Mountain Motors', 'Denver', 'Colorado', '555 Rocky Mtn Blvd', '80201', 39.7392, -104.9903),
        ('Mile High Auto Sales', 'MHAS', 'Mile High Auto Sales', 'Aurora', 'Colorado', '1400 Mile High Dr', '80012', 39.7294, -104.8319),
        ('Great Lakes Motors', 'GLM', 'Great Lakes Motors', 'Chicago', 'Illinois', '200 Lakeshore Dr', '60601', 41.8781, -87.6298),
        ('Windy City Auto', 'WCA2', 'Windy City Auto Inc', 'Naperville', 'Illinois', '88 Windy Ln', '60540', 41.7725, -88.1479),
        ('Buckeye Motors', 'BKM', 'Buckeye Motors', 'Columbus', 'Ohio', '350 High St', '43215', 39.9612, -82.9988),
        ('Queen City Cars', 'QCC', 'Queen City Cars', 'Cincinnati', 'Ohio', '900 Queen City Ave', '45202', 39.1031, -84.5120),
        ('Coral Reef Auto', 'CRA', 'Coral Reef Auto Sales', 'Miami', 'Florida', '150 Ocean Dr', '33139', 25.7907, -80.1300),
        ('Orange Blossom Motors', 'OBM', 'Orange Blossom Motors', 'Orlando', 'Florida', '400 Orange Blossom Trl', '32801', 28.5383, -81.3792),
        ('Gulf Breeze Auto', 'GBA', 'Gulf Breeze Auto Group', 'Tampa', 'Florida', '77 Gulf Breeze Blvd', '33602', 27.9506, -82.4572),
        ('Everglade Cars', 'EGC', 'Everglade Cars LLC', 'Fort Lauderdale', 'Florida', '1800 Everglade Rd', '33301', 26.1224, -80.1373),
        ('Sunshine State Motors', 'SSM', 'Sunshine State Motors', 'Jacksonville', 'Florida', '501 Sunshine Ave', '32202', 30.3322, -81.6557),
        ('Peachtree Auto Plaza', 'PAP', 'Peachtree Auto Plaza', 'Atlanta', 'Georgia', '600 Peachtree St', '30308', 33.7490, -84.3880),
        ('Savannah Motors', 'SVN', 'Savannah Motors Inc', 'Savannah', 'Georgia', '20 River St', '31401', 32.0809, -81.0912),
        ('Music City Auto', 'MCA', 'Music City Auto', 'Nashville', 'Tennessee', '410 Broadway', '37203', 36.1627, -86.7816),
        ('Smoky Mountain Motors', 'SMM', 'Smoky Mountain Motors', 'Knoxville', 'Tennessee', '88 Smoky Mtn Rd', '37902', 35.9606, -83.9207),
        ('Delta Auto Sales', 'DAS', 'Delta Auto Sales', 'Memphis', 'Tennessee', '120 Beale St', '38103', 35.1495, -90.0490),
        ('Motor City Motors', 'MCM2', 'Motor City Motors', 'Detroit', 'Michigan', '700 Woodward Ave', '48226', 42.3314, -83.0458),
        ('Great Lakes Auto Sales', 'GLAS', 'Great Lakes Auto Sales', 'Grand Rapids', 'Michigan', '55 Lake Shore Dr', '49503', 42.9634, -85.6681),
        ('Badger State Motors', 'BSM', 'Badger State Motors', 'Milwaukee', 'Wisconsin', '300 Wisconsin Ave', '53203', 43.0389, -87.9065),
        ('Cheese Country Auto', 'CCA', 'Cheese Country Auto', 'Madison', 'Wisconsin', '22 State St', '53703', 43.0731, -89.4012),
        ('Liberty Bell Motors', 'LBM', 'Liberty Bell Motors', 'Philadelphia', 'Pennsylvania', '100 Liberty Bell Way', '19106', 39.9526, -75.1652),
        ('Steel City Auto Sales', 'SCAS', 'Steel City Auto Sales', 'Pittsburgh', 'Pennsylvania', '601 Steel St', '15222', 40.4406, -79.9959),
        ('Independence Motors', 'IDM', 'Independence Motors', 'Kansas City', 'Missouri', '1776 Independence Ave', '64108', 39.0997, -94.5786),
        ('Gateway Auto Plaza', 'GAP', 'Gateway Auto Plaza', 'St. Louis', 'Missouri', '900 Gateway Arch Blvd', '63101', 38.6270, -90.1994),
    ]
    created = 0
    for i, (name, short, full, city, state, address, zc, lat, lng) in enumerate(extra, start=6):
        if Dealer.objects.filter(id=i).exists():
            continue
        Dealer.objects.create(id=i, name=name, short_name=short, full_name=full,
                              city=city, state=state, address=address, zip=zc,
                              lat=lat, long=lng, phone=f'555-0{i:03d}',
                              email=f'info{i}@autodealer.com', website=f'https://auto{i}.example.com')
        created += 1
    print(f"Created {created} new dealers; total now {Dealer.objects.count()}")
