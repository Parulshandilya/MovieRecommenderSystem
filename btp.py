import numpy as np
import scipy
import pylab as pl
import matplotlib
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
import sys
 
 # Load in text from .dat file
import csv

s="<Overall Rating>4
<Avg. Price>$173
<URL>http://www.tripadvisor.com/ShowUserReviews-g60878-d72572-r23327047-Best_Western_Pioneer_Square_Hotel-Seattle_Washington.html

<Author>everywhereman2
<Content>Old seattle getaway This was Old World Excellence at it's best.THIS is the place to stay at when visiting the historical area of Seattle. Your right on the water front near the ferry's and great sea food restraunts,and still with'in walking distance for great blues and jazz music. The staff for this hotel are excellent,they make you feel right at home. The breakfast was great.We did'nt have to travel far to have a good cup of JOE and a light meal to start our adventurous day off into one of the most beautifull city's in america. This hotel is in an area that makes it easy to get to any place you want to go and still find your way back, I highly recomend this hotel for your next visit to seattle. 
<Date>Jan 6, 2009
<img src="http://cdn.tripadvisor.com/img2/new.gif" alt="New"/>
<No. Reader>-1
<No. Helpful>-1
<Overall>5
<Value>5
<Rooms>5
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>5

<Author>RW53
<Content>Location! Location?       view from room of nearby freeway 
<Date>Dec 26, 2008
<No. Reader>-1
<No. Helpful>-1
<Overall>3
<Value>4
<Rooms>3
<Location>2
<Cleanliness>4
<Check in / front desk>3
<Service>-1
<Business service>-1

<Author>KGBT
<Content>Wow, what charm! As a Travel Agent, I've stayed at quite a few hotel, but this is the only Historic hotel so far...  I loved it! Had to go back for a personal stay. The decor is beautiful, the lobby furniture fits the time period  is still comfy. The city view rooms are great - love the little balconies. Great breakfast, nice people, great location - The Seattle Underground Tours is a 1/2 block away. I've aready sent my folk there for a stay  have told others. 
<Date>Dec 14, 2008
<No. Reader>-1
<No. Helpful>-1
<Overall>5
<Value>4
<Rooms>5
<Location>5
<Cleanliness>5
<Check in / front desk>4
<Service>-1
<Business service>4

<Author>Marilyn1949
<Content>Great location for sporting events We attend Seahawks and Mariners games and this hotel is within walking distance of both. It is 2 blocks from the Washington State Ferry terminal so we can walk across the ferry and walk directly to the hotel. The hotel staff is always friendly, rooms are very clean and the free breakfast is a real money saver. Much more variety than most and they just added a new waflfe station. Highly recommend this hotel.Marilyn J. 
<Date>Dec 1, 2008
<No. Reader>-1
<No. Helpful>-1
<Overall>4
<Value>4
<Rooms>4
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>5

<Author>MissViolet105
<Content>Pioneer Square BW Fine Choice We chose BW Pioneer Square in Seattle because it was the closest to the Amtrak station and we had a one night layover between trains. Turns out it was a fine choice for other reasons, too. It's a charming old building at the epicenter of old Seattle, as the name implies. My morning walk took me to Pioneer Square itself and to the Seattle city hall, both within three blocks. The docks and Puget Sound are a block away, and it's an easy walk to Pike Street Market. Rooms are big and nicely renovated. Ours had a balcony on the street with a lovely view of a full moon, though I know they can't always provide that. The staff was friendly and knowledgable, the free breakfast and free bowl of fruit welcome and good. Fine place.Mac Nelson/Joyce Haines 
<Date>Nov 28, 2008
<No. Reader>-1
<No. Helpful>-1
<Overall>4
<Value>5
<Rooms>5
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>2

<Author>fallriverma
<Content>Quality hotel at great price Very clean. Free breakfast with good selections. Staff friendly and most helpful. A grat stay! 
<Date>Nov 25, 2008
<No. Reader>-1
<No. Helpful>-1
<Overall>5
<Value>5
<Rooms>5
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>5

<Author>simmotours
<Content>comfortable, good value, convenient location The Pioneer Square is a pleasant smallish hotel in an interesting corner of Seattle. Comfortable rooms and bathroom, if oddly shaped and not very large, which were fine for a short stay. The breakfasts are limited but acceptable and the breakfast room is enlivened by the sight of fellow guests attempting to work out the waffle maker. Pleasant staff and reception, apparantly family run and up to the usual Best Western standards, clean and well appointed.Several restaurants nearby but we suggest avoiding the closest, al Boccalino, a rather pretentious but unexceptional Italian 3 or 4 doors away. Expensive for what you get; we were told very offhandedly that they had no Washington wines. We are an Italian restaurant! At $60 to $100 for bottles one would pay no more than 拢10 for in a UK off licence- forget it. 
<Date>Nov 18, 2008
<No. Reader>-1
<No. Helpful>-1
<Overall>4
<Value>4
<Rooms>3
<Location>4
<Cleanliness>4
<Check in / front desk>4
<Service>4
<Business service>-1

<Author>SweetwaterMill
<Content>Warm hospitality on a rainy Seattle night We had just arrived in downtown Seattle after debarking from the Bremerton ferry during the evening rush hour. Negotiating traffic in the rain was somewhat nerve-racking, so when we entered the hotel lobby, we probably looked bedraggled. The desk clerk immediately assessed our mental state, giving us a warm welcome and attending to the details of checking us in efficient order. Our room was wonderful, combining modern amenities with Pioneer Square ambiance. We will definitely be coming back to the Pioneer Square Hotel! 
<Date>Nov 15, 2008
<No. Reader>-1
<No. Helpful>-1
<Overall>5
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1

<Author>AuntSusie006
<Content>Pleasant stay This is an old hotel in the original part of Seattle. Therefore, rooms are a little small. However, this also makes the location a great one for history and ambience. Above all, though, was the great personnel in the hotel - at the desk, in the breakfast room, at the concierge station. Extremely pleasant and helpful with accommodations and recommendations. The hotel is also across the street from the water and down two blocks from the underground bus station. Very convenient; very nice. 
<Date>Nov 13, 2008
<No. Reader>-1
<No. Helpful>-1
<Overall>4
<Value>3
<Rooms>3
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>5

<Author>RoadDawg77
<Content>Regular Guest - happy to recommend this one! For almost 2 years - almost on a weekly basis work takes me to downtown Seattle and I always stay at the Best Western Pioneer Square. Only a few blocks from Safeco and Quest field, Pikes Place Market; a block to the water and 6 blocks to the international district for an incredible selection of authentic Asian restaurants. The hotel itself is a wonderfully restored Victorian with a great selection of rooms and budgets. Having stayed here close to a 100 nights in 2 years - always met with a friendly and helpful staff (this is a big deal to me), clean and comfortable rooms and a great continental breakfast in the morning - I am happy to recommend this hotel. Bring your walking shoes and enjoy a couple of vacation days right here in the middle of everything - you'll be glad you did. Last note: If you're looking for a hotel with a pool, jacuzzi, exercise facilities and family entertainment within the hotel - this is not the place for you. 
<Date>Nov 12, 2008
<No. Reader>-1
<No. Helpful>-1
<Overall>5
<Value>5
<Rooms>5
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>-1

<Author>EastFallser
<Content>"Like Grandma's house with Victorian overtones" This small hotel is one we have been to several times now and it feels almost like home. It is more comfortable and familiar than up-to-date and trendy. A little like going to Grandma's house, with Victorian overtones, and the capacity to accommodate all your family and friends and be there for all your needs, including the warmth that goes with it.The breakfast that is available in the hotel is certainly adequate and right there when you need it. The location is great for doing a little roaming around in the historic and sports districts and the parking is very convenient and reasonably priced. I would certainly go again. 
<Date>Nov 12, 2008
<No. Reader>-1
<No. Helpful>-1
<Overall>4
<Value>4
<Rooms>4
<Location>4
<Cleanliness>4
<Check in / front desk>4
<Service>4
<Business service>3

<Author>lesnpat
<Content>Location is just one feature here We had four great days here recently - location is fantastic given that there is so much within walking distance (including stadia and railway station), and if it rains (which is does here) transit is free in a large zone of downtown. Front desk staff could not have been more helpful and have a sense of humour, the concierge knew the answers to the questions we had, and the room was quiet and clean and comfortable. We will return.... 
<Date>Oct 29, 2008
<No. Reader>1
<No. Helpful>1
<Overall>5
<Value>4
<Rooms>5
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>-1

<Author>Traveler34NewJersey
<Content>wonderful restoration A restored hotel in the Pioneer Square section of Seattle, this little gem was delightful. Rooms are small, but clean and tasteful. The only thing better was the hotel staff! They were extremely helpful, professional and knowledgeable about the area. All their recommendations were on the mark!Would definitely return! 
<Date>Oct 17, 2008
<No. Reader>1
<No. Helpful>1
<Overall>5
<Value>5
<Rooms>3
<Location>4
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>-1

<Author>madmatriarch
<Content>Love the feeling of coming home We have called this hotel home for 3-4 nights once a year for the past five years. The staff is wonderful, the rooms are clean, and the breakfast is great. No views but we stay on the go so much that who cares. You can walk to Safeco for ballgames, walk to Pike Market, the Art Museum, the library, three book stores, and you are right on the waterfront. I recommend it highly and look forward to more stays. 
<Date>Oct 11, 2008
<No. Reader>1
<No. Helpful>1
<Overall>5
<Value>4
<Rooms>5
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>4

<Author>BonJean
<Content>Great Hotel, Prime Location My husband and I spent 3 nights at the Best Western Pioneer Square Hotel and it was great. The hotel is a very old one that has been completely remodeled and is just beautiful. The people who work there were very friendly and extremely helpful. The rooms were nice, large, clean and inviting. Every night the staff came by and offered more towels, turned down your bed and put candy on the pillows. The location, in Pioneer Square, was fantastic. You walk up half a block and catch a free bus to anywhere, walk down a block to the waterfront and catch the ferry to one of the islands. It was so easy to get around that we didn't bother to rent a car. We definitely enjoyed our stay and would stay there again and would recommend it to anyone. 
<Date>Oct 9, 2008
<No. Reader>1
<No. Helpful>1
<Overall>5
<Value>4
<Rooms>5
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>5

<Author>rjgacord
<Content>Great Experience My husband and I just returned from our first trip to Seattle and couldn't be more happy with our experience at this hotel. The location is perfect, walking distance to many areas of the city. Even though it is in the oldest part, many would call if one of the most colorful areas of Seattle, we loved it. The hotel has been completely renovated and you feel the history all around you from the decor to the architecture. Although you are very close to a main hiway running through the city, the noise level in our room was minimal and it was not a problem to us at all. You must remember this is a city not the burbs!! It is the only hotel in Pioneer Square and I can't wait to return someday. 
<Date>Oct 8, 2008
<No. Reader>1
<No. Helpful>1
<Overall>5
<Value>4
<Rooms>5
<Location>5
<Cleanliness>4
<Check in / front desk>4
<Service>4
<Business service>-1

<Author>owt_u
<Content>Great hotel for a low price and fantastic location I stayed at the Best Western Pioneer Square for two nights last month, and was very impressed. It was close to Safeco field and the other attractions in the area as well as the best continental breakfast I've ever had at a hotel. Great selection and quality items to select from. Staff was friendly and helpful with directions and bus routes (one of the stops for the bus to/from Sea-Tac is only a few blocks away). Rooms were very clean and comfortable. I didn't get any discounts on the room, but it was still a great deal compared to what other hotels in downtown were charging. 
<Date>Oct 8, 2008
<No. Reader>-1
<No. Helpful>-1
<Overall>5
<Value>5
<Rooms>5
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>3

<Author>CraignRuth
<Content>Immaculate, vintage hotel with personable staff--worth the price This impeccably-restored, 1880's era hotel is clean and quiet and wonderfully located in a popular historic district near the waterfront. Our train was delayed and the night desk clerk cheerfully greeted us at 3 AM and even held the door for us. The breakfast, including hard-boiled eggs, various cereals and fresh batter with waffle-maker, was delicious. It is a bit pricey but we would stay there again in a heartbeat and recommend it highly. 
<Date>Oct 7, 2008
<No. Reader>-1
<No. Helpful>-1
<Overall>5
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1

<Author>dw64
<Content>Noisey Hotel noisey. We complained  the front desk offered an upgrade for additional $50 a night. Room was suppose to be a queen, but was actually a full. We booked directly thru hotel, not priceline or hotels.com. Great location. Clean, but don't expect a good nights rest! 
<Date>Sep 20, 2008
<No. Reader>-1
<No. Helpful>-1
<Overall>2
<Value>2
<Rooms>1
<Location>4
<Cleanliness>4
<Check in / front desk>3
<Service>3
<Business service>3

<Author>BSNRN
<Content>great place to stay this hotel was a great place to stay. The rooms were very clean. and the staff very friendly and helpful. Its location is ideal to see seattle. The sports stadiums are a 10 walk or walking to Pikes market is a 15-20 walk or you can take the tram. I have stayed at this hotel several times and plan on staying there again. 
<Date>Sep 15, 2008
<No. Reader>-1
<No. Helpful>-1
<Overall>5
<Value>5
<Rooms>5
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>5

<Author>BettyNorregaard
<Content>Great Location Rooms were super clean with excellant mattress' and pillows. Quiet accomadations with a lovely shower/tub combination. The continental breakfast had an extremely large variety of options and everything was temperature correct. I would recommend this hotel to anyone traveling in the area. We stayed here because we were going on a cruise. This location was very close to all downtown Seattle sights and to the cruise line location. Parking garage was close by and well guarded. 
<Date>Sep 10, 2008
<No. Reader>-1
<No. Helpful>-1
<Overall>5
<Value>3
<Rooms>5
<Location>4
<Cleanliness>5
<Check in / front desk>3
<Service>4
<Business service>-1

<Author>mykidsmother4
<Content>Perfectly at peace in Seattle at Pioneer Square We stayed 3 days, 2 nights in August. The location was perfect. The room was spacious. The front desk clerks were exceptionally helpful and kind. I would love to go back to Seattle just to stay here again.KayCalifornia 
<Date>Sep 10, 2008
<No. Reader>-1
<No. Helpful>-1
<Overall>5
<Value>4
<Rooms>5
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>5

<Author>USCGAnnapolis
<Content>Perfect after an Alaskan Cruise The perfect stop after an Alaskan cruise on NCL. Took all the hassle out of getting home. They had a computer for pre-boarding on SWA. We got into our room early and were able to enjoy Seattle on foot before our flight out the next day. 
<Date>Sep 10, 2008
<No. Reader>-1
<No. Helpful>-1
<Overall>4
<Value>4
<Rooms>5
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>5

<Author>atgmdog
<Content>Great Hotel The Rooms were on the large side , but unfortunately no view. It was a nice touch to have mints, apples and 2 bottles of water waiting in the room when we arrived, very nice touch. The breakfast room was to small and very crowded so we did not stay to have breakfast at the Hotel. Is centrally locacated and short walk to almost anywhere you want to be in downtown Seattle. 
<Date>Sep 10, 2008
<No. Reader>-1
<No. Helpful>-1
<Overall>4
<Value>4
<Rooms>5
<Location>3
<Cleanliness>4
<Check in / front desk>3
<Service>4
<Business service>3

<Author>KyGirl-Faye
<Content>Fabulous Hotel My husband and I just spent 6 nights in this hotel and loved every minute. The staff is friendly and efficient. We stayed for 4 nights, left to go to Victoria BC, then came back for 2 more nights. The hotel has old world charm. The room decor is very well done - down to the drapery, carpet and nice artwork on the walls. The bathrooms are modern and nicely sized. The beds were very comfortable. The rooms and bathrooms were spotless. The linens were fresh and spotless as well. The fresh fruit and free bottled water was a nice touch and very much appreciated. The breakfast room was clean and always stocked with the daily offerings. The coffee was good and the waffles were addicting. Even the elevator was fast and roomy. You don't realize how much you appreciate that until you go to another hotel where the elevators are sloooooow and tiny (as they were in our Victoria BC hotel). The Pioneer Square area is lively and exciting with lots of little shops and restaurants. We walked around the area at night and didn't feel unsafe. Other people mentioned street people as problematic. This is a fact of life in any large city, but none of the street people were aggressive or abusive. Just a block away, they offer a tour of Seattle Underground which was interesting. Pizza at Mario's was delicious. Dinner at Elliott's Oyster House at Pier 56 was wonderful. We found Seattle to be a great city with friendly people who are helpful and polite to tourists. We hope to visit again some day and when we do, we will again stay at the Best Western Pioneer Square Hotel. 
<Date>Aug 24, 2008
<No. Reader>1
<No. Helpful>1
<Overall>5
<Value>5
<Rooms>5
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>-1

<Author>Teresa_Bennet
<Content>Very Disapointed My first time to the west coast and I had to pick this property? Very average all the way the way! the noise level at night from my neighbors was way too loud. The service was slow and the room had a funny smell. The staff made me feel like an unwelcome visitor not a special guest. No wifi service although they advertise there is? This not a good Best Western - To bad Seatle is very nice.AB 
<Date>Jul 2, 2008
<No. Reader>-1
<No. Helpful>-1
<Overall>1
<Value>2
<Rooms>1
<Location>1
<Cleanliness>1
<Check in / front desk>1
<Service>1
<Business service>1

<Author>jltpeke
<Content>Perfect Location, Great Hotel We stayed at the Best Western Pioneer Square for 2 nights prior to our Alaskan cruise. This was a family reunion of sorts, and the hotel was wonderful in working with us to get 6 rooms with the set up needed for each family and all together on one floor of the hotel. Hotel staff VERY nice to work with.This is a perfect location for walking around downtown Seattle and the waterfront. Very easy walking to Pike Street Market, the waterfront, etc. Hotel very kindly arranged taxi van service for all of us on the morning we needed to get to the pier with all of our luggage.Rooms are small compared to some other hotels, but VERY clean and nice. Free continental breakfast was nice. There was juice, coffee, cereals, milk, danish, bagels, toast, boiled eggs, etc.Great price and great location, we will stay here on our next trip to Seattle. 
<Date>Jun 16, 2008
<No. Reader>2
<No. Helpful>2
<Overall>5
<Value>5
<Rooms>4
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>5

<Author>over1861
<Content>Great Hotel This is an old hotel but totally renovated. We reserved a small room with two single beds but were upgraded to a deluxe room. We were in a corner room with a view of the Puget sound. The rooms were clean and the desk personnel were great and very helpful for touring. It is very short walk to the water front area. There are several great restaurants within walking distance.A great place to stay in Seattle. 
<Date>May 16, 2008
<No. Reader>2
<No. Helpful>2
<Overall>5
<Value>4
<Rooms>5
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>-1

<Author>pamnfam
<Content>Great Location We stayed here for a girls' trip in a standard double double. The hotel is well located, across from the ferry docks, and within walking distance to public transportation. The rooms are small, and the view from our window was not great. But the staff was wonderful and the continental breakfast in the morning with eggs, yogurt, oatmeal, toast and muffins, fruit, etc. filled us up. We spent three nights here and had a wonderful time. I would not recommend this hotel for a big group or family, since the public spaces tend on the small side. Nice get away for singles or couples trips. 
<Date>Mar 29, 2008
<No. Reader>2
<No. Helpful>2
<Overall>4
<Value>4
<Rooms>2
<Location>5
<Cleanliness>4
<Check in / front desk>4
<Service>4
<Business service>-1

<Author>blueyedtraveler
<Content>This is definitely not a "Skid Row" hotel!!! This is a very old and colorful area. Yesler Way where this hotel is location is on the original skid row. This was orginally a muddy road that logs were dragged (skidded) up to get to Yesler's mill. Thus, the term skid row was was given to this area. Loggers and millworkers being lonely at times liked to frequent the business that sprung up around this area. They also got a bit thirsty!!! I previously lived in Seattle for about 15 years. I rode or walked by the hotel several times and never gave it a thought. Was looking for a hotel close to the train station, by the bus stop, and close to the waterfront. You step out the door of the hotel and turn left walk about a block and your at the ferry terminal on the waterfront. You walk out the hotel door and practically next door is the bus stop for FREE bus service within the Downtown core. The Klondike Gold Rush museum is also in the area. They sometimes offer free walking tours that include a trip to the top of the Smith Tower (originally the tallest building on the West Coast). If you walk north up 1st Ave about 6-7 blocks  at the Seattle Art Museum (SAM) and the Pike Place Market. The rooms were small, but the hotel was built in the early 1900. The room was immaculate, and because of something we were given an upgrade to a deluxe room with city view. We got in about 9pm and walked to the waterfront. Ivars is open until late. We found a really good deal. They extend their Happy Hour on Fridays til closing. Well drinks, wine are $3.00. Limited menu but I got fried oysters for $4.95, can get Fish  chips also for 4.95 with view table looking out as the ferry terminal. We will definely recommend this hotel to anyone traveling to Seattle. The most beautiful city on the planet!!!!! 
<Date>Mar 9, 2008
<No. Reader>5
<No. Helpful>5
<Overall>5
<Value>4
<Rooms>5
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>-1

<Author>UKAdventureGirl
<Content>A bitter sweet experience! Great location, though as already mentioned, pioneer square attracts some dodgy looking characters, although I must say they never intimidated us. A gentle 'sorry, can't help' to any beggars was enough. Our first room smelt fusty and unclean, the second room smelt like a brewery! Needless to say we had the windows open constantly. Bed lumpy and uncomfortable. Bathroom nice and clean but small. Staff friendly and helpful. Good complimentary, continental breakfast. Quaint with lots of character, but not the best Best Western i've stayed in. 
<Date>Jan 7, 2008
<No. Reader>5
<No. Helpful>4
<Overall>2
<Value>2
<Rooms>2
<Location>3
<Cleanliness>3
<Check in / front desk>3
<Service>3
<Business service>3

<Author>yondaime1845
<Content>Its the best of the best for a reason One of the more affordable and better hotels in the city of seattle. I had a great time during my stay because of great service and friendly employees. The location is convenient and parking is cheap. I give this hotel an A+ 
<Date>Jan 2, 2008
<No. Reader>5
<No. Helpful>5
<Overall>5
<Value>5
<Rooms>5
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>5

<Author>Johnphil29
<Content>Great hotel, wonderful experience       The hotel sign on the building 
<Date>Dec 17, 2007
<No. Reader>6
<No. Helpful>6
<Overall>4
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1

<Author>Quantum1
<Content>Ok hotel in a bad location The hotel is not terrible in itself, but the looming and noisy I-5 viaduct is nearby. Also, the King Co. courthouse is not far, and there are a lot of people who hang out around there and around this whole area who are not the greatest. There are some nice tourist destinations near this hotel, but you're much better off staying nearer the convention center and only visiting the Pioneer Square area in daylight if there are specific things there you want to see. Near the convention center puts you closer to other places in the downtown area like the Pike St. Market. 
<Date>Dec 8, 2007
<No. Reader>6
<No. Helpful>4
<Overall>2
<Value>2
<Rooms>2
<Location>1
<Cleanliness>3
<Check in / front desk>2
<Service>2
<Business service>2

<Author>MoniqueMontreal
<Content>Excellent location to visit Seattle       Hotel elegantly restored inside, Romanesque-Victorian style. Stayed in Sept.: perfect! 
<Date>Nov 8, 2007
<No. Reader>7
<No. Helpful>7
<Overall>4
<Value>5
<Rooms>4
<Location>5
<Cleanliness>5
<Check in / front desk>4
<Service>5
<Business service>5

<Author>mmob100
<Content>Very Good Stay We spent the first night of our Pacific Northwest/Northern CA trip at the Pioneer Square and were very happy. The first room we were shown had a slightly odd arrangement where the TV was to the side of the bed and not easily viewable. Being from Boston and on the road for the first night of the World Series, being able to view the TV was important to us. At the front desk my request was easily and politely accomodated and we were given a more TV viewable room.We found the location of the hotel, particularly with the free public transport offered by Seattle to be great. The staff was very professional and helpful. The only slight negative was the breakfast which we found to be pretty mediocre. Overall, we were very happy with our hotel selection. 
<Date>Nov 6, 2007
<No. Reader>5
<No. Helpful>5
<Overall>4
<Value>3
<Rooms>3
<Location>3
<Cleanliness>4
<Check in / front desk>4
<Service>4
<Business service>-1

<Author>patclatts
<Content>Location, Location, Location... Hospitality....Your hotel has it all! Dear Jo, We wanted to thank you and let you now how much we enjoyed our stay at your beautiful hotel. Your rooms are very nicely decorated and extremely comfortable. We traveled with Russ and Rosemarie Regn. Thank you for also including us a bottle of champagne and basket of goodies. They sharedtheir bottle with us the first night. We shared ours with them the second night. Thank you for your hospitality. The extra courtesy you extended to us as well made our stay very memorable. It was a pleasure meeting you. There is so much to see and do in Seattle. Much more than I was awareof. Loved the Pike Place Market! The tour of Seattle is definitely worth it! We will certainly recommend your place to others. Greetingsfrom Delaware! Russ and Pat Clatts 
<Date>Oct 30, 2007
<No. Reader>4
<No. Helpful>3
<Overall>5
<Value>5
<Rooms>5
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>5

<Author>eebm
<Content>We'd stay again       excellent location -- a short walk to everything 
<Date>Oct 24, 2007
<No. Reader>4
<No. Helpful>3
<Overall>4
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1

<Author>cjt9t9
<Content>Good hotel Stayed here for 2 nights at the start of our West Coast Adventure. Really nice hotel with great (and cheap) chinese next door. Clean, big room and free internet. Only complaint was the tiny bathroom - nowhere to lay anything. 
<Date>Sep 27, 2007
<No. Reader>3
<No. Helpful>3
<Overall>4
<Value>4
<Rooms>4
<Location>5
<Cleanliness>4
<Check in / front desk>5
<Service>4
<Business service>5

<Author>BDM22
<Content>Very convenient location; highly recommend. My husband and I spent a week in Seattle, basically did a sightseeing/pub crawl tour of the city. This hotel is the only one in Pioneer Square, and it is within walking distance of everything. In fact, it's across the street from the waterfront, which is a popular place to go walking and sightseeing. We never rented a car or taxi; didn't need one. Granted, we walked about 3-5 miles a day, but stopped anywhere we wanted along the way. You don't need a car in the city, and you have to call for taxis anyway...why not walk?The room was always clean, and a decent size for the two of us. It had a weird smell though, but it wasn't something we couldn't tolerate, though. It is very charming and cozy, and is within a few yards of great restaurants and bars. In fact, out of all the meals we ate, the restaurant next door, Al Boccalino's, was the best. They provide room service for the hotel, and they have some of the best Italian food I've ever had. Somewhat pricey, but it was SO good. Hotel staff were friendly, but not the most knowledgeable of all the questions I asked (such as, can they help with reservations for the Victoria Clipper, what bus # do we take to go to Ballard, etc.). But, they were very nice and always tried to help.The hotel was quiet when we were there, even though it seemed to be very crowded. I would recommend it to anyone. With our AAA membership, we paid $161 a night, except for Friday night, which was more expensive. 
<Date>Sep 2, 2007
<No. Reader>3
<No. Helpful>3
<Overall>4
<Value>4
<Rooms>4
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>4
<Business service>5

<Author>Mardie
<Content>One night was not enough Trust me, you will not be disappointed if you stay at this hotel. What can I say about the Best Western Pioneer Square Hotel that hasn't already been said? From the Welcome to Seattle from the girls at reception to the Have a good trip from the Bell Captain, this hotel gets my vote for being the best.At the end of a long tiring day having travelled by plane and boat to reach Seattle, all my cares disappeared as soon as I opened the door to my hotel room. The large room was beautifully decorated with the king size bed taking pride of place. It looked so peaceful and welcoming with the period furniture and matching appointments that I couldn't wait to unpack and relax with a cup of tea. The lighting was excellent with not a 40 watt bulb evident. The towels were plentiful and fluffy and there was loads of room in the bathroom to lay out my toiletries. I thought the framed picture on the wall was a nice homey touch. The room was quiet and there was no noise to disturb a dreamless sleep that night. In fact, I was glad the next morning I had set my alarm the night before.I enjoyed my Continental breakfast the next morning of toast, jam, yoghurt, fruit and coffee. There was also cold cereals, Danish and muffins on offer. I learned that bus transportation is free in the Pioneer Square area and the bus stop is just steps away from the hotel entrance on Yesler. However, since I wanted to explore on foot it was an easy walk to the Uwajimaya shopping complex in Chinatown - a delightful place. Although my room rate was a little more than I normally pay, in retrospect my one night's stay was worth every cent and I fully intend to make a return visit in the future. 
<Date>Jul 6, 2007
<No. Reader>2
<No. Helpful>2
<Overall>5
<Value>5
<Rooms>5
<Location>5
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>5

<Author>OberonSacramento
<Content>Great Location but Noisy We stayed at this Hotel while in Seattle on Business. Check in was very complicated they had no parking available when we arrived and the front desk staff was not helpful at all with the parking situation. Our company was paying for the stay but when we arrived we had to wait 45 minutes for someone in the office to figure out what was going on. When we arrived in our room we were plesantly surprised it was large very clean and comfortable. The wireless internet left a lot to be desired very slow and constant drop offs. In the evening the noise from the freeway nearby was constant.. For the money that this establishment cost we could have stayed in a Sheraton or Hilton and been a lot happier 
<Date>May 15, 2007
<No. Reader>4
<No. Helpful>4
<Overall>2
<Value>1
<Rooms>4
<Location>4
<Cleanliness>5
<Check in / front desk>1
<Service>1
<Business service>1

<Author>seekwa
<Content>Lots of charm Not your normal Best Western, this is a charming hotel in a great location. High ceilings and warm appointments, room quality is excellent and spacious, particularly considering the architectural restrictions of an older building. Use the tiny elevators, or what the heck... climb the wide staircases... it's good for your heart.Step outside into the fun of day or night life in Seattle. You are one block from the waterfront and trolley, and one block from tons of buses. On the opposite end of town from the Space Needle, there are loads of stores, shops and eateries nearby. Bring comfy walking shoes. Down an alley next to the hotel, i.e., one block directly behind the hotel is a wonderful diner, complete with quaint vinyl booths, where you can get a tasty, filling and affordable breakfast.Get a good rate, and this hotel is a sure winner. 
<Date>Apr 23, 2007
<No. Reader>6
<No. Helpful>6
<Overall>4
<Value>4
<Rooms>4
<Location>4
<Cleanliness>4
<Check in / front desk>3
<Service>3
<Business service>3

<Author>Sailoranne79
<Content>Great customer service but lacking in other areas... Stayed at this place because I had a business meeting in downtown Seattle. This hotel is right in Downtown seattle but is in the Pioneer square area. To me, this area was pretty bad and I would walk around there alone (I am a woman). I would not feel safe there. Anyway, the hotel is pretty nice and the customer service is first rate. The room was very large but the bed was extremely uncomfortable. Great pillows but my body ached from sleeping in the very hard bed. The shower was the best part! Big and plenty of hot water!! I loved that part!Luckily I didn't have to pay for the room but it was pretty expensive - not worth the money to me. And, parking is a mess there - you have to park about 2 blocks away in this parking garage that is not run by the hotel. It is very inconveinant..... 
<Date>Apr 16, 2007
<No. Reader>4
<No. Helpful>4
<Overall>3
<Value>3
<Rooms>3
<Location>2
<Cleanliness>3
<Check in / front desk>5
<Service>5
<Business service>3

<Author>Traveling4BiznFun
<Content>Great for Games or Access to Pioneer Squares "Culture" This hotel is great if you are looking for a nice, boutique-ish hotel in downtown Seattle, as long as you don't mind the culture of Pioneer Square. There are definitely better hotels, but this is just a few blocks from the two stadiums and in the middle of a district with great shopping. Pioneer Square does have a bit of a homeless problem, but I've never seen that spill into the hotel. The rooms as fairly small, but nicely appointed. Free breakfast is okay. 
<Date>Mar 3, 2007
<No. Reader>8
<No. Helpful>8
<Overall>3
<Value>3
<Rooms>4
<Location>3
<Cleanliness>3
<Check in / front desk>4
<Service>4
<Business service>3

<Author>ohzonejoe
<Content>An Okay Stay in Seattle When Every Other Hotel is Booked This historic hotel has been remodeled with the budget traveller in mind. We had a corner room, right next to the BIG outdoor HOTEL neon sign. Luckily, it did not blink all night; a couple of paper clips on the blackout curtains took care of that problem. The room was big and clean. The heating unit was a bit quirky with its remote control, and maintaining a comfortable temperature was a challenge. It was cycled between either a bit too cool and a bit too hot. But the room and bath were clean and the bathroom fixtures were all new and flawless. Bring a 100 watt bulb if you want to read in bed (or open the curtain if you don't mind a pink hue). The biggest downside was the thin wall to the next room and some loud guests. For the price, its about the quality you would expect. 
<Date>Dec 3, 2006
<No. Reader>7
<No. Helpful>7
<Overall>3
<Value>3
<Rooms>3
<Location>3
<Cleanliness>4
<Check in / front desk>3
<Service>3
<Business service>-1

<Author>JJTrouble
<Content>No Security in Pioneer Square We had a nice stay in Seattle for two days in this hotel, until the moment we were checking out. We had noticed what appeared to be vagrants sitting in the unattended lobby a couple of times, including the early morning were checking out. My wife left our bags for a moment to get a muffin at the continental breakfast and when she came back to the bags, her handbag was gone, and so was the fellow who was sitting across from her. I was at the counter checking out and didn't see anything, but I did see the suspicious fellow sitting in the lobby as I move our bags. The manager was not there, as it was a Sunday, and they have treated us like we're trying to pull a scam. They claim no liability for baggage untended, but they should at least take responsibility for making sure their lobby is clear of derelicts waiting to prey on their customers. From about 9 a.m. to 6 p.m. there is supposed to be someone at the front door, but outside those hours they have nobody there, and the clerks are unable to see who is coming in or leaving. The manager says they have security cameras, but I think she was bluffing to see if I backed off of our claims. None of the other employees there that morning knew of any cameras. Furthermore, the manager NEVER returned any of my calls as promised.We feel we've been treated disrespectfully, and none of our suggestions have been taken seriously (ie the need for full-time front-door concierge/security). That part of Seattle has really become full of vagrants. BEWARE!! 
<Date>Nov 13, 2006
<No. Reader>19
<No. Helpful>15
<Overall>1
<Value>3
<Rooms>3
<Location>3
<Cleanliness>3
<Check in / front desk>3
<Service>3
<Business service>3

<Author>Veek
<Content>Old reliable - clean, comfortable, quiet, well-located Location, location, location. Leave the car at home, take the train to Seattle: PSH is within walking distance from King Street train station. Located in the heart of historic Pioneer Square, it's convenient to waterfront, antiques, art galleries, designer-furniture, fine restaurants and pubs, clubs and theaters, the International District, Pike Place Market, downtown ferries and Alaska Marine Hwy. I've stayed there in 2004, 2005, and recommend it to all my friends. 
<Date>Oct 30, 2006
<No. Reader>10
<No. Helpful>9
<Overall>4
<Value>4
<Rooms>4
<Location>5
<Cleanliness>3
<Check in / front desk>4
<Service>3
<Business service>-1

<Author>javainhand
<Content>Such a great place! I love this hotel! The staff was amazing, we had never been to Seattle before and were probably terribly annoying with our endless questions and need for directions, but the staff was extremely patient and every person we talked to was just great! I can't say enough good things about the Best Western Pioneer Square, we chose it for the location, but the room was spotless and we had such a great time, we will definitely be back! 
<Date>Oct 6, 2006
<No. Reader>8
<No. Helpful>8
<Overall>5
<Value>5
<Rooms>5
<Location>4
<Cleanliness>5
<Check in / front desk>5
<Service>5
<Business service>5

<Author>brenchley
<Content>Game On We were booked to stay here for two nights from the 31st of august , we arrived at about 7PM only to be told that thay had no parking. We were given directions to some public parking but they did not tell us that there was a match on in the stadium. we could not find anywhere to park so we drove to the best western executive inn by the space needle to see if they had any rooms..We were very impressed with the service. they phoned back to the pioneer square to see if we could transfer our booking, which they did at no extra charge.{well done Best Western}.so remember to book a parking space when booking your room if you are driving. 
<Date>Sep 21, 2006
<No. Reader>10
<No. Helpful>6
<Overall>2
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1

<Author>jackandjan
<Content>Nice hotel but..... Very nice hotel, well remodelled and tasteful accommodations. Staff was helpful, polite and unobtrusive. The major problem is the number and outright in your face quality of the derelicts that inhabit every street corner, bench, and doorway of the Pioneer Square area. To be forced to watch so that you dont step in someones urine trail, to have to turn your back so as to not have to watch a derelict urinate in broad daylight on the biulding on a main street, to have to PUSH one of them away from me when he kept circling back closer and closer to me, is TOO MUCH.I will never stay in downtown Seattle again. Well over a hundred dollars and you are a prisoner in your hotel. The derelicts have taken over Pioneer Square. They own their benches, doorways, and covered areas. They own Pioneer Square.Wake up Seattle and take your city back.Guess I will be staying at the airport nextime. Lots of good restaurants and shops that are loosing customers due to the prevalence of these derelicts. 
<Date>Sep 20, 2006
<No. Reader>12
<No. Helpful>10
<Overall>2
<Value>3
<Rooms>3
<Location>1
<Cleanliness>4
<Check in / front desk>3
<Service>4
<Business service>4

<Author>Janko
<Content>Nice hotel for the Pioneer Square Area We stayed here in late August. This hotel is a decent stay for a decent price for this time of year. The service is awesome. They would clean our room in the morning and again in the late afternoon with candy on the pillow. It is in such a historic area and right across the street from Pier, underground tour and waterfront walk. The area is in a positive transistion for such an older area of town. Lots to see and do and easy to catch the bus to other areas of town. Hotel is totally redone and refurbished with great service. If you don't care about having a room with a view, much cheaper rates. It is however in the older area of town and the panhandlers are everywhere. Panhandlers are quite polite, but aggresive. 
<Date>Sep 4, 2006
<No. Reader>4
<No. Helpful>4
<Overall>4
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1

<Author>adnaw
<Content>Great hotel in an historic area.       Hotel from up the block. 
<Date>Sep 3, 2006
<No. Reader>6
<No. Helpful>6
<Overall>5
<Value>4
<Rooms>4
<Location>4
<Cleanliness>5
<Check in / front desk>5
<Service>4
<Business service>4

<Author>scice
<Content>Great Location       Safeco Field 
<Date>Aug 29, 2006
<No. Reader>6
<No. Helpful>6
<Overall>4
<Value>4
<Rooms>4
<Location>5
<Cleanliness>4
<Check in / front desk>5
<Service>4
<Business service>5

<Author>AJH
<Content>One night to catch Clipper This hotel is a century hotel located in the Pioneer District. I feel they have great rooms for the location/price but if you have a family beware they are DOUBLE beds not QUEEN beds. Parking is really only 1 block, if that. For a few nights in the historical district it is worth it. YES, most of the homeless seem to be in this area due to the missions. We need to send a response to the city about this. Otherwise, don't fault the hotel...they are great!!! The city needs to respond and do something w/ the homeless. The ENTIRE city has a probelm and I travel internationally a lot. Our USA has some serious issues. They beg and are hostile about it. Only Seattle showed me this!! UGH 
<Date>Jun 30, 2006
<No. Reader>4
<No. Helpful>3
<Overall>4
<Value>4
<Rooms>4
<Location>-1
<Cleanliness>4
<Check in / front desk>-1
<Service>4
<Business service>-1

<Author>Babymooner2
<Content>Just fine. This hotel is located in Pioneer Square, though just a quick walk to the water front/Pike's Market. However, the immediate location is a bit rough around the edges and there is a very apparent homeless population. Once you've walked several blocks away towards the market, it gets noticeably better. The hotel is very nice -- our room was spacious and nicely decorated. There was a very toxic cleaning agent odor that required us to open the windows and leave them open. Otherwise, it was a nice big room with a good sized bathroom. Breakfast was great. It is served in an adjoining breakfast room/cafe to the hotel and includes cereal, pastries, bagels and then some. Above and beyond most continental included breakfasts. The parking is about 1 1/2 blocks away and costs $18 a day. It's relatively convenient, though when we returned back to the lot around 9 or 10 PM after attending a wedding, it was sketchy. There were a few shady characters lingering around the garage (it's locked and requires access, but once your key card opens the door, anyone can cruise in after you.) All in all, it's a convenient decent place for a reasonable price. If you're looking for luxury, this isn't it, but it's more than adequate. 
<Date>Mar 21, 2006
<No. Reader>13
<No. Helpful>12
<Overall>4
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1

<Author>LVinWA
<Content>Charming hotel --brace for Seattle parking, but good to go! Having read this site's reviews, I braced for additional parking fees and stayed here anyway. Glad I did. Seattle, like SFO  NYC, has joined ranks of big city parking headaches so if you drive be prepared to hand over parking rates. Staff very gracious in allowing us to check-in early (12Noon) and were upfront about the $18/day parking deal up the street. We saw plenty of parking tickets under windshield wipers downtown  around Pike's so take it into consideration. Very centrally located; can walk to Pike's, restaurants on First, Pioneer Square boutiques  artisian storefronts, downtown shopping. Service was pretty darned friendly to say nothing of professional. As long as you know what you're in for with downtown Seattle parking (you pay, you pay, you pay) you'll be good to go. Clean, full of character, and breakfast was BW standard fare --not bad. I'd recommend it if you want a little old world charm to round out your stay. 
<Date>Mar 14, 2006
<No. Reader>7
<No. Helpful>7
<Overall>4
<Value>4
<Rooms>4
<Location>-1
<Cleanliness>4
<Check in / front desk>-1
<Service>4
<Business service>-1

<Author>RustyGull
<Content>Almost Perfect, But... We wanted to love the Best Western at Pioneer Square, and for the most part we did. Excellent location, very nicely appointed rooms, and great continental breakfast. Kudos to Best Western for this fine hotel.Our biggest beef from our stay there was a front-desk person who was quite rude and unbecoming for a hospitality professional. His conduct was inappropriate and distasteful - when we walked in, he was slouching over the desk, and looked at my father and I as if we were unwelcome. He was then surly to us over a number of subjects. This got things off to a rotten start. However, we found the rest of the staff to be quite helpful and friendly, so in the end, we were happy that we stayed here. 
<Date>Jan 2, 2006
<No. Reader>16
<No. Helpful>15
<Overall>4
<Value>3
<Rooms>5
<Location>-1
<Cleanliness>4
<Check in / front desk>-1
<Service>2
<Business service>-1

<Author>A TripAdvisor Member
<Content>Perfect Location for a walking tour of Seattle! Excellent accomodation... perfect for a tourist's experience. The complimentary breakfast and coffee (Seattle's Best) was a welcome accomodation--allowing us to begin sightseeing earlier with plenty of caffeinated!!!Rooms were clean and the Victorian era building had loads of character. Quiet, convienent and a good buy. Close to the Pioneer Square and waterfront areas... good choice. 
<Date>Dec 13, 2005
<No. Reader>15
<No. Helpful>13
<Overall>4
<Value>4
<Rooms>4
<Location>-1
<Cleanliness>4
<Check in / front desk>-1
<Service>4
<Business service>-1

<Author>A TripAdvisor Member
<Content>Best Hotel! My husband and I have stayed in the hotel numerous times in the last couple of years and would never stay anywhere else. We have recommended the hotel to family and friends who have also loved staying there!I have to say that from the moment you walk into the hotel you feel like someone cares for your needs and the staff is very courteous and friendly. The rooms were very well taken care of and extremly clean. The rates were excellant especially if you are there in downtown Seattle for just a overnight visit. My sister and I stayed at the hotel while we had a three day shopping trip in Seattle and everday the room was cleaned with special goodies left in the room for us! It was great because transportation was right there so we didn't have to use our vehicle to drive places and have the terrible time trying to find parking...everything was RIGHT THERE!We loved our stay and being pampered that we did not want to go home!This is a WONDERFUL hotel with FANTASTIC staff that make you feel at home! I would never stay anywhere else! 
<Date>Nov 4, 2005
<No. Reader>24
<No. Helpful>20
<Overall>5
<Value>5
<Rooms>5
<Location>-1
<Cleanliness>5
<Check in / front desk>-1
<Service>5
<Business service>-1

<Author>A TripAdvisor Member
<Content>The Best Bachlorette Party My friend was getting married and wanted to do her bachlorette party in Seattle. I got two rooms for the group at Best Western Pioneer Square Hotel, and I can't tell you what a wonderful time we had there! The rooms were cozy and Victorian, the service was great and everyone just loved it. Staying in Pioneer Square was very convenient鈥攚e didn't have to drive anywhere! Thanks! 
<Date>Nov 3, 2005
<No. Reader>12
<No. Helpful>6
<Overall>5
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1

<Author>A TripAdvisor Member
<Content>Best Downtown Hotel Having frequent business in the downtown Seattle area I am always looking for good deals at better than average hotels, and I have found the best one yet at the Pioneer Square Hotel! Spotless property, great staff, and excellent location make this hotel a sure winner! It is close enough to everything that downtown Seattle has to offer from art to entertainment that I have NEVER needed to take a cab anywhere. The courteous and knowlegable staff gave me great and up-to-date instructions on where to go for world class Jazz - just around the corner. This hotel really made my recent trips to Seattle very special and enjoyable, and I gladly highly recommend it to one and all! 
<Date>Oct 14, 2005
<No. Reader>28
<No. Helpful>23
<Overall>5
<Value>5
<Rooms>5
<Location>-1
<Cleanliness>5
<Check in / front desk>-1
<Service>5
<Business service>-1

<Author>A TripAdvisor Member
<Content>Great Price and Excellent Location My wife and I decided to visit Seattle for the first time and booked the Pioneer Square Hotel online. When we arrived the staff was perfect; they noticed we were from out of town and offered to point out great spots to hit while we were here and even made us reservations for Salty's Seafood restaurant all at Check In!! The room was perfect overlooking the street and breakfast was great. We paid $143 per night and that was great compared to other hotels we looked at. I will definatley be sending my friends here. 
<Date>Oct 14, 2005
<No. Reader>19
<No. Helpful>13
<Overall>5
<Value>5
<Rooms>4
<Location>-1
<Cleanliness>5
<Check in / front desk>-1
<Service>5
<Business service>-1

<Author>sfm132
<Content>Great hotel  I had planned a two-night stay for early October in the Best Western Pioneer Square Hotel after a train ride from LA to Seattle. After my first night (and seeing how much there was to do within walking distance), I added a third night.This is not your typical Best Western. It is in a beautiful c.1913 building. The hotel is modern inside with wireless internet access, while retaining the charm with huge doors, beautiful woodwork, and high ceilings. It was absolutely spotless, and the staff was very friendly and helpful. Having read many reviews, I know to expect no free parking (not an issue as I didn't have a rental); and that the rooms could have been on the smallish side. Mine was certainly adequate, with a larger-than-average bathroom. My window was on an airshaft, but as I chose the lowest priced room, I expected that too. As I use a hotel room to sleep in, not view scenery from, I had no issue with it. I did hear someone complaining one morning about highway noise as their room was on that side, so I was glad to have my quiet brick wall!They offer a continental breakfast that is above average. There is a separate room off of the lobby with numerous tables, complimentary newspapers, and a staff of two to keep things clean  filled. Seattle is a very PC city, and yes, there are a lot of homeless found on the streets. But not one bothered me, and I had no concerns about walking to restaurants at night, alone. The streets are filled with people until quite late, as it is a very vibrant area. But it is not rowdy by any means. I would recommend this hotel to any of my family or friends. You are a block from the waterfront  ferries; Pike Place Market and the Monorail station are within easy walking distance. Taxis in Seattle are very reasonably priced and easy to find, and there is free city bus transport. Within a few blocks of the hotel, you have every kind of restaurant you could desire, many antique and art shops. If I ever return to Seattle, I know I will stay at the Pioneer Square Hotel.S.MurphyNH 
<Date>Oct 10, 2005
<No. Reader>21
<No. Helpful>17
<Overall>5
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1

<Author>dvdcrow
<Content>What a Great Hotel! Don't understand the complaints on this website about this hotel. We stayed here for two nights in late August and loved everything about it. First, the location was great. It was within walking distance of both the waterfront and Pike Place Market, and we could easily take the monorail to the Space Needle. (There are hills in Seattle, so if you have someone with you who has trouble walking, you may want to consider taking a bus or taxi.) Both the lobby and the room were nicely decorated, and the staff was very helpful. Being on Pioneer Square meant that we could go next door or right across the street to get a drink and/or something to eat. Of course, we didn't walk through the square at night because of the street people who hung out there, but that's just common sense. We were never bothered by anyone, and because this hotel is so well located we were able to easily enjoy this great city. If you're worried about street noise, call the hotel directly and ask for an interior room. We had an interior king and it was very quiet. We plan to return to Seattle, and when we do, we'll stay at the Best Western Pioneer Square Hotel again. 
<Date>Sep 6, 2005
<No. Reader>22
<No. Helpful>17
<Overall>5
<Value>5
<Rooms>4
<Location>-1
<Cleanliness>5
<Check in / front desk>-1
<Service>5
<Business service>-1

<Author>A TripAdvisor Member
<Content>It was "OK" We stayed here Sunday, August 21st. Our reservation was made online, base rate of $158, directly with the hotel. Upon check-in, they indicated they were upgrading our room to a deluxe. We were on the 4th Floor with a small balcony. The room was clean and adequate; nothing special. This is an old hotel in a district that I would not feel comfortable walking in the late hours. Breakfast was Continental, apathetic staff. Probably would not stay there again. 
<Date>Aug 28, 2005
<No. Reader>27
<No. Helpful>18
<Overall>3
<Value>3
<Rooms>3
<Location>-1
<Cleanliness>3
<Check in / front desk>-1
<Service>3
<Business service>-1

<Author>lass=
<Content>lack of customer service skills and overpriced We found this place online and made a reservation through third party booking, like many. We were just staying one night and sharing the room with friends. When we arrived we were politely greeted. Our reservation was for 4 persons per our confirmation letter. When they asked how many guests, we told them 4 and they said that the extra guest cost was $20.00 for each person per night. Our rate was already over $150.00 for a room with 2 double beds. We told them that our reservation was for 4 persons and they said their system said 2 persons. We went ahead and took the room. At this time nobody told us anything about parking and we had to ask. We were then given a key for the garage and told it would be $50 if we lost the key and $100 on Sunday if we left it in the car because the garage is closed on Sundays. Nothing more was said about parking. We left and went to the ball game returning late in the evening. We received our keys and went to the extremely small room. We walked in and it had a view of the brick building next door. The room was very clean. When we checked out the next morning we asked again about the rate and produced the confirmation letter. We were told that we were getting the best rate available and that we would have to take it up with the third party booking company. We then questioned the charge for the parking. We were never told about the $18.00 to park in the garage. We told them such and were told he was the manager and insisted that the person checking us in told us. We told him that he had checked us in and that he only told us about the key charged for the garage and never the parking amount. He then told us that he always tells guests and that he was the manager. He would not work with us at all on the price even though we were never told about the parking fee or that our confirmation letter showed 4 persons. So in turn we ended up paying $240.00 for a room that you could find at any budget motel. The breakfast leaves something to be desired. The floor was filthy with food and the food was not well stocked, counters were dirty and the staff was sitting behind the counter talking. We walked up to the corner Tullys instead.I would never stay at this motel again. Having worked for hotels for the past 7 years, I do not know how they keep guests. If we treated a guest as they had we would be out of business. I would recommend customer service training.We will never stay there again and we will tell many people about our experience. This is definately not what we expected from a Best Western.We gave it a 2 because it was clean. 
<Date>Aug 25, 2005
<No. Reader>21
<No. Helpful>17
<Overall>2
<Value>1
<Rooms>2
<Location>-1
<Cleanliness>4
<Check in / front desk>-1
<Service>1
<Business service>-1

<Author>onthego2nowhere
<Content>The customer is NOT always right at the Pioneer Square It was a Sunday night in April, and we were in town for a concert, and after the evening crew gave a great effort, physically showing us a few of the different rooms (which were some of the smallest I've ever seen, with views of backend brick walls), they led us to believe when we asked about parking that we could either park on the street at no charge that night, or park in the garage a block up the road. When we were thinking about getting a parking pass to save hassle for later, they simply said, talk to the night shift when you get back and they will set you up. After coming back that night, a young man was working who claimed he was new, and got his manager when we asked about the parking. When we asked for the parking pass, he wanted $15 and we refused telling him we were led to believe by the conversation with the evening shift that it was free. The manager told us that that wasn't his policy as he pulled out his hotel policy book and that we either had to pay the $15 or park on the street which started on the meter at 7 am. This was great news coming at 1 am and exhausted. We felt cheated.  In an obvious bluff attempt he then proceeded to tell us that he would check the video tape (as he told us everything was recorded throughout the day) and if we weren't told about the charge he would give us our pass at no charge. When I accepted the offer staring him in the face, he then proceeded to go back on his offer and again refused to offer the pass running in circles, You mean they didn't give you the pass yet? Excuse me??? What? If I had the pass already, I would have been in a parking lot parking my car, and not in the middle of an argument about paying it. We had only been there checked in hours earlier and told the manager that we wanted our money back and would go find another hotel in that case. He refused. He would NOT refund us our money and we were forced to stay there that night. It was late, we were tired and he was running in circles with his lame arguments, we decided to wake up at 7 am, pay the meter for a couple more hours, and leave. I wasn't giving this place another dollar. The next day we found another hotel near the space needle and were treated with the utmost respect and in subsequent visits will never stay at that dive again. The only good thing, and the reason I gave a 2 and not a 1 was the one bellhop that showed us the small rooms and helped us with the door that would never swipe and really helped us out. The place is a nice location, but based on this experience, the lack of management skills, and others that I read that had the same parking problem, there are other hotels, and I would pass on the Pioneer Square Best Western. 
<Date>Jul 20, 2005
<No. Reader>31
<No. Helpful>17
<Overall>2
<Value>2
<Rooms>2
<Location>-1
<Cleanliness>2
<Check in / front desk>-1
<Service>2
<Business service>-1

<Author>ncwmallard
<Content>Location is Everything! If you are looking for the perfect location to stay at in Seattle, consider the Best Western Hotel in Pioneer Square. Also called the Pioneer Square Hotel, it's located just off of the square in downtown Seattle. It's only a block away from the waterfront and within easy walking distance of both Safeco field (for baseball fans), the new Seahawks Football Stadium and Pike Place Market.As far as downtown hotels go, the Best Western is a bargain compared to most hotels of this caliber. The rooms inside the hotel were of a decent size (not huge - but not tiny either) and clean. The staff was very friendly and helpful, and along with the location, they were the highlight of the hotel.The only negative things I can think of is the fact that you do have to pay for your parking and that the complemetary continental breakfast was lacking in terms of selection and quality.Having said that - a clean hotel room at a good price in the heart of Seattle is a heck of a bargain. I'll be back again! 
<Date>Apr 18, 2005
<No. Reader>31
<No. Helpful>22
<Overall>4
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1

<Author>A TripAdvisor Member
<Content>People ... people ... people People ... the Pioneer staff on the inside ... make this 'boutique' hotel (ie tastefully reburbished and refreshingly small) such a great place to stay for a night or two. The staff are polite, friendly and efficient. However, people ... the panhandling bums on the outside ... are likely to take the shine off your stay. Pioneer Square and the area immediately outside the hotel entrance is over-run with the down and outs of the Pacific Rim ... many of them are friendly but others can be aggressive and quite intimidating at night. 
<Date>Apr 16, 2004
<No. Reader>30
<No. Helpful>23
<Overall>2
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1

<Author>A TripAdvisor Member
<Content>Best Kept Secret in Seattle ! This is the best kept secret in Seattle. We were expecting the typical Best Western hotel. This is by far the best hotel we have stayed in for many years. The staff is marvelous ! 
<Date>Mar 10, 2004
<No. Reader>19
<No. Helpful>15
<Overall>5
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1

<Author>quietandloudatonce
<Content>Fabulous!! I'll Stay Here from Now On!   showReview(1687053, 'full');  
<Date>Mar 2, 2004
<No. Reader>17
<No. Helpful>14
<Overall>5
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1

<Author>A TripAdvisor Member
<Content>Best Western Pioneer Square a Gem in a Sea of Hotel Choices   showReview(1424593, 'full');  
<Date>Oct 28, 2003
<No. Reader>15
<No. Helpful>13
<Overall>5
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1

<Author>smed008
<Content>Pioneer Square....simply charming   showReview(1344251, 'full');  
<Date>Sep 17, 2003
<No. Reader>15
<No. Helpful>13
<Overall>5
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1

<Author>A TripAdvisor Member
<Content>Love This Hotel!   showReview(1273085, 'full');  
<Date>Sep 3, 2003
<No. Reader>12
<No. Helpful>10
<Overall>5
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1

<Author>A TripAdvisor Member
<Content>Pioneer Square Hotel   showReview(1270059, 'full');  
<Date>Aug 31, 2003
<No. Reader>6
<No. Helpful>4
<Overall>4
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1

<Author>A TripAdvisor Member
<Content>Reasonable lodgings in the older part of town   showReview(1260463, 'full');  
<Date>Aug 26, 2003
<No. Reader>12
<No. Helpful>11
<Overall>4
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1

<Author>A TripAdvisor Member
<Content>Worst $150 a Night I Ever Spent in Seattle   showReview(1257038, 'full');  
<Date>Aug 23, 2003
<No. Reader>24
<No. Helpful>16
<Overall>1
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1

<Author>A TripAdvisor Member
<Content>Great staff and location   showReview(1208867, 'full');  
<Date>Aug 4, 2003
<No. Reader>12
<No. Helpful>12
<Overall>5
<Value>4
<Rooms>3
<Location>-1
<Cleanliness>5
<Check in / front desk>-1
<Service>5
<Business service>-1

<Author>A TripAdvisor Member
<Content>A Diamond in the Ruff !   showReview(1107074, 'full');  
<Date>Jun 24, 2003
<No. Reader>7
<No. Helpful>7
<Overall>5
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1

<Author>A TripAdvisor Member
<Content>A Great Seattle Hotel Near Everything   showReview(1020542, 'full');  
<Date>May 17, 2003
<No. Reader>45
<No. Helpful>45
<Overall>5
<Value>-1
<Rooms>-1
<Location>-1
<Cleanliness>-1
<Check in / front desk>-1
<Service>-1
<Business service>-1
"

