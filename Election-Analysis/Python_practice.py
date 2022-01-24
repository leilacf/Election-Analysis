counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El paso are in the list of counties")
else:
    print("Arapahoe and El paso are not in the list of counties")

counties = ["Arapahoe", "Denver", "Jefferson"]
if "Arapahoe" in counties or "El paso" in counties:
    print("Arapahoe or el Paso is in the list of counties")
else:
    print("Arapahoe and El paso are not in the list of counties")

counties = ["Arapahoe", "Denver", "Jefferson"]
for county in counties:
    print(county)

counties = ["Arapahoe", "Denver", "Jefferson"]
for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)

for county in counties_dict:
    print(counties_dict[county])

for county, voters in counties_dict.items():
    print(county,voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i]['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")