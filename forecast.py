from lxml import html
import requests

page = requests.get('https://magicseaweed.com/Narragansett-Beach-Surf-Report/1103/')
tree = html.fromstring(page.content)


#This will create master list containing SwellSize, SwellInterval, & Airtemp
intervals = tree.xpath('//*[@class="nomargin font-sans-serif heavy"]/text()')
#Navigating through master list, breaking down 3 data categories into variables
swellsizeft = intervals[0::5]
swellintervalsec = intervals[2::5]
airtempdegrees = intervals[4::5]

# Next we will need to iterate through our per category lists, and add to DB!

# ['A', 'B', 'C', 'D']
# ['Swell Size', 'Junk', 'SwellInterval', 'Junk', 'Airtemp']
# ['  2', '  ', '  11', '  ', '38', ]


print(airtempdegrees)