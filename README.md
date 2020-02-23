# emoji-encoding
Strings of emoji are easier to read than strings of hexadecimal.
Instead of displaying hexadecimal characters 00 to FF, we can define a
set of emoji from 😀 to 🏁.

Hexadecimal | Emoji
--- | ---
08:21:5B:CC | 😎🐶🍕🎥

The subset of emoji has been selected to reduce the number of emoji
that are similar to each other. The goal is to make it easier to
understand the emoji with a quick glance, or with a short description
in English.

* CSV: [`Unicode-v13.0-2020-02-22.csv`](../master/Unicode-v13.0-2020-02-22.csv)
* JavaScript: [`emoji-encoder.js`](../master/javascript/emoji-encoder.js)

# Emoji Encoding Table

Selected Unicode characters and descriptions downloaded from https://unicode.org/emoji/charts/full-emoji-list.html.

Dec|Hex|Bin|Code|Emoji|Description
--- | --- | --- | --- | --- | ---
0|00|00000000|U+1F600|😀|grinning face
1|01|00000001|U+1F607|😇|smiling face with halo
2|02|00000010|U+1F60D|😍|smiling face with heart-eyes
3|03|00000011|U+1F61B|😛|face with tongue
4|04|00000100|U+1F911|🤑|money-mouth face
5|05|00000101|U+1F634|😴|sleeping face
6|06|00000110|U+1F920|🤠|cowboy hat face
7|07|00000111|U+1F973|🥳|partying face
8|08|00001000|U+1F60E|😎|smiling face with sunglasses
9|09|00001001|U+1F921|🤡|clown face
10|0A|00001010|U+1F47B|👻|ghost
11|0B|00001011|U+1F47D|👽|alien
12|0C|00001100|U+1F916|🤖|robot
13|0D|00001101|U+1F648|🙈|see-no-evil monkey
14|0E|00001110|U+1F596|🖖|vulcan salute
15|0F|00001111|U+1F44D|👍|thumbs up
16|10|00010000|U+1F933|🤳|selfie
17|11|00010001|U+1F4AA|💪|flexed biceps
18|12|00010010|U+1F442|👂|ear
19|13|00010011|U+1F9E0|🧠|brain
20|14|00010100|U+1F9B7|🦷|tooth
21|15|00010101|U+1F440|👀|eyes
22|16|00010110|U+1F445|👅|tongue
23|17|00010111|U+26F7|⛷|skier
24|18|00011000|U+1F3C2|🏂|snowboarder
25|19|00011001|U+1F3CC|🏌|person golfing
26|1A|00011010|U+1F3C4|🏄|person surfing
27|1B|00011011|U+1F6A3|🚣|person rowing boat
28|1C|00011100|U+1F3CA|🏊|person swimming
29|1D|00011101|U+26F9|⛹|person bouncing ball
30|1E|00011110|U+1F6B4|🚴|person biking
31|1F|00011111|U+1F938|🤸|person cartwheeling
32|20|00100000|U+1F939|🤹|person juggling
33|21|00100001|U+1F436|🐶|dog face
34|22|00100010|U+1F98A|🦊|fox
35|23|00100011|U+1F99D|🦝|raccoon
36|24|00100100|U+1F431|🐱|cat face
37|25|00100101|U+1F434|🐴|horse face
38|26|00100110|U+1F984|🦄|unicorn
39|27|00100111|U+1F42E|🐮|cow face
40|28|00101000|U+1F437|🐷|pig face
41|29|00101001|U+1F40F|🐏|ram
42|2A|00101010|U+1F42A|🐪|camel
43|2B|00101011|U+1F999|🦙|llama
44|2C|00101100|U+1F992|🦒|giraffe
45|2D|00101101|U+1F418|🐘|elephant
46|2E|00101110|U+1F42D|🐭|mouse face
47|2F|00101111|U+1F407|🐇|rabbit
48|30|00110000|U+1F994|🦔|hedgehog
49|31|00110001|U+1F987|🦇|bat
50|32|00110010|U+1F43B|🐻|bear
51|33|00110011|U+1F998|🦘|kangaroo
52|34|00110100|U+1F983|🦃|turkey
53|35|00110101|U+1F413|🐓|rooster
54|36|00110110|U+1F54A|🕊|dove
55|37|00110111|U+1F986|🦆|duck
56|38|00111000|U+1F989|🦉|owl
57|39|00111001|U+1F438|🐸|frog
58|3A|00111010|U+1F422|🐢|turtle
59|3B|00111011|U+1F432|🐲|dragon face
60|3C|00111100|U+1F996|🦖|T-Rex
61|3D|00111101|U+1F433|🐳|spouting whale
62|3E|00111110|U+1F988|🦈|shark
63|3F|00111111|U+1F419|🐙|octopus
64|40|01000000|U+1F41A|🐚|spiral shell
65|41|01000001|U+1F98B|🦋|butterfly
66|42|01000010|U+1F41D|🐝|honeybee
67|43|01000011|U+1F578|🕸|spider web
68|44|01000100|U+1F339|🌹|rose
69|45|01000101|U+1F33B|🌻|sunflower
70|46|01000110|U+1F332|🌲|evergreen tree
71|47|01000111|U+1F335|🌵|cactus
72|48|01001000|U+1F347|🍇|grapes
73|49|01001001|U+1F349|🍉|watermelon
74|4A|01001010|U+1F34C|🍌|banana
75|4B|01001011|U+1F34D|🍍|pineapple
76|4C|01001100|U+1F352|🍒|cherries
77|4D|01001101|U+1F353|🍓|strawberry
78|4E|01001110|U+1F95D|🥝|kiwi fruit
79|4F|01001111|U+1F965|🥥|coconut
80|50|01010000|U+1F951|🥑|avocado
81|51|01010001|U+1F955|🥕|carrot
82|52|01010010|U+1F33D|🌽|ear of corn
83|53|01010011|U+1F336|🌶|hot pepper
84|54|01010100|U+1F344|🍄|mushroom
85|55|01010101|U+1F95C|🥜|peanuts
86|56|01010110|U+1F950|🥐|croissant
87|57|01010111|U+1F968|🥨|pretzel
88|58|01011000|U+1F9C0|🧀|cheese wedge
89|59|01011001|U+1F354|🍔|hamburger
90|5A|01011010|U+1F35F|🍟|french fries
91|5B|01011011|U+1F355|🍕|pizza
92|5C|01011100|U+1F32D|🌭|hot dog
93|5D|01011101|U+1F32E|🌮|taco
94|5E|01011110|U+1F37F|🍿|popcorn
95|5F|01011111|U+1F35C|🍜|steaming bowl
96|60|01100000|U+1F364|🍤|fried shrimp
97|61|01100001|U+1F980|🦀|crab
98|62|01100010|U+1F366|🍦|soft ice cream
99|63|01100011|U+1F369|🍩|doughnut
100|64|01100100|U+1F36D|🍭|lollipop
101|65|01100101|U+1F36F|🍯|honey pot
102|66|01100110|U+1F37C|🍼|baby bottle
103|67|01100111|U+2615|☕|hot beverage
104|68|01101000|U+1F378|🍸|cocktail glass
105|69|01101001|U+1F37A|🍺|beer mug
106|6A|01101010|U+1F962|🥢|chopsticks
107|6B|01101011|U+1F30E|🌎|globe showing Americas
108|6C|01101100|U+1F9ED|🧭|compass
109|6D|01101101|U+1F3D4|🏔|snow-capped mountain
110|6E|01101110|U+1F3E0|🏠|house
111|6F|01101111|U+1F3F0|🏰|castle
112|70|01110000|U+1F5FC|🗼|Tokyo tower
113|71|01110001|U+1F5FD|🗽|Statue of Liberty
114|72|01110010|U+26E9|⛩|shinto shrine
115|73|01110011|U+1F3A1|🎡|ferris wheel
116|74|01110100|U+1F3A2|🎢|roller coaster
117|75|01110101|U+1F682|🚂|locomotive
118|76|01110110|U+1F695|🚕|taxi
119|77|01110111|U+1F69C|🚜|tractor
120|78|01111000|U+1F3CD|🏍|motorcycle
121|79|01111001|U+1F6B2|🚲|bicycle
122|7A|01111010|U+1F6F4|🛴|kick scooter
123|7B|01111011|U+1F6F9|🛹|skateboard
124|7C|01111100|U+1F6A6|🚦|vertical traffic light
125|7D|01111101|U+1F6A7|🚧|construction
126|7E|01111110|U+2693|⚓|anchor
127|7F|01111111|U+26F5|⛵|sailboat
128|80|10000000|U+1F6F6|🛶|canoe
129|81|10000001|U+1F6E5|🛥|motor boat
130|82|10000010|U+2708|✈|airplane
131|83|10000011|U+1F681|🚁|helicopter
132|84|10000100|U+1F6F0|🛰|satellite
133|85|10000101|U+1F680|🚀|rocket
134|86|10000110|U+1F6F8|🛸|flying saucer
135|87|10000111|U+1F6CE|🛎|bellhop bell
136|88|10001000|U+231B|⌛|hourglass done
137|89|10001001|U+1F556|🕖|seven o’clock
138|8A|10001010|U+1F319|🌙|crescent moon
139|8B|10001011|U+1F321|🌡|thermometer
140|8C|10001100|U+26C5|⛅|sun behind cloud
141|8D|10001101|U+1F32A|🌪|tornado
142|8E|10001110|U+1F308|🌈|rainbow
143|8F|10001111|U+2602|☂|umbrella
144|90|10010000|U+26A1|⚡|high voltage
145|91|10010001|U+2744|❄|snowflake
146|92|10010010|U+2603|☃|snowman
147|93|10010011|U+1F525|🔥|fire
148|94|10010100|U+1F4A7|💧|droplet
149|95|10010101|U+1F30A|🌊|water wave
150|96|10010110|U+1F383|🎃|jack-o-lantern
151|97|10010111|U+1F386|🎆|fireworks
152|98|10011000|U+1F38E|🎎|Japanese dolls
153|99|10011001|U+1F381|🎁|wrapped gift
154|9A|10011010|U+1F39F|🎟|admission tickets
155|9B|10011011|U+1F3C6|🏆|trophy
156|9C|10011100|U+26BD|⚽|soccer ball
157|9D|10011101|U+26BE|⚾|baseball
158|9E|10011110|U+1F3C0|🏀|basketball
159|9F|10011111|U+1F3C8|🏈|american football
160|A0|10100000|U+1F3BE|🎾|tennis
161|A1|10100001|U+1F3B3|🎳|bowling
162|A2|10100010|U+1F3D3|🏓|ping pong
163|A3|10100011|U+1F94A|🥊|boxing glove
164|A4|10100100|U+1F94B|🥋|martial arts uniform
165|A5|10100101|U+26F8|⛸|ice skate
166|A6|10100110|U+1F3A3|🎣|fishing pole
167|A7|10100111|U+1F3B1|🎱|pool 8 ball
168|A8|10101000|U+1F3AE|🎮|video game
169|A9|10101001|U+1F3B0|🎰|slot machine
170|AA|10101010|U+1F3B2|🎲|game die
171|AB|10101011|U+265F|♟|chess pawn
172|AC|10101100|U+1F0CF|🃏|joker
173|AD|10101101|U+1F004|🀄|mahjong red dragon
174|AE|10101110|U+1F3AD|🎭|performing arts
175|AF|10101111|U+1F3A8|🎨|artist palette
176|B0|10110000|U+1F9F6|🧶|yarn
177|B1|10110001|U+1F454|👔|necktie
178|B2|10110010|U+1F9E6|🧦|socks
179|B3|10110011|U+1F458|👘|kimono
180|B4|10110100|U+1F45C|👜|handbag
181|B5|10110101|U+1F460|👠|high-heeled shoe
182|B6|10110110|U+1F451|👑|crown
183|B7|10110111|U+1F393|🎓|graduation cap
184|B8|10111000|U+1F484|💄|lipstick
185|B9|10111001|U+1F48E|💎|gem stone
186|BA|10111010|U+1F50A|🔊|speaker high volume
187|BB|10111011|U+1F4E2|📢|loudspeaker
188|BC|10111100|U+1F3BC|🎼|musical score
189|BD|10111101|U+1F3A4|🎤|microphone
190|BE|10111110|U+1F3A7|🎧|headphone
191|BF|10111111|U+1F4FB|📻|radio
192|C0|11000000|U+1F3B7|🎷|saxophone
193|C1|11000001|U+1F3B8|🎸|guitar
194|C2|11000010|U+1F3B9|🎹|musical keyboard
195|C3|11000011|U+1F3BB|🎻|violin
196|C4|11000100|U+1F941|🥁|drum
197|C5|11000101|U+1F4F1|📱|mobile phone
198|C6|11000110|U+1F4DE|📞|telephone receiver
199|C7|11000111|U+1F50B|🔋|battery
200|C8|11001000|U+1F50C|🔌|electric plug
201|C9|11001001|U+1F4BB|💻|laptop
202|CA|11001010|U+1F5A8|🖨|printer
203|CB|11001011|U+1F4BF|💿|optical disk
204|CC|11001100|U+1F3A5|🎥|movie camera
205|CD|11001101|U+1F3AC|🎬|clapper board
206|CE|11001110|U+1F4F8|📸|camera with flash
207|CF|11001111|U+1F50D|🔍|magnifying glass tilted left
208|D0|11010000|U+1F4A1|💡|light bulb
209|D1|11010001|U+1F526|🔦|flashlight
210|D2|11010010|U+1F4D3|📓|notebook
211|D3|11010011|U+1F5DE|🗞|rolled-up newspaper
212|D4|11010100|U+1F4B0|💰|money bag
213|D5|11010101|U+1F4E7|📧|e-mail
214|D6|11010110|U+270F|✏|pencil
215|D7|11010111|U+1F58A|🖊|pen
216|D8|11011000|U+1F4C5|📅|calendar
217|D9|11011001|U+1F4CC|📌|pushpin
218|DA|11011010|U+1F4CE|📎|paperclip
219|DB|11011011|U+1F4D0|📐|triangular ruler
220|DC|11011100|U+2702|✂|scissors
221|DD|11011101|U+1F5C4|🗄|file cabinet
222|DE|11011110|U+1F5D1|🗑|wastebasket
223|DF|11011111|U+1F513|🔓|unlocked
224|E0|11100000|U+1F511|🔑|key
225|E1|11100001|U+1F528|🔨|hammer
226|E2|11100010|U+2694|⚔|crossed swords
227|E3|11100011|U+1F3F9|🏹|bow and arrow
228|E4|11100100|U+1F6E1|🛡|shield
229|E5|11100101|U+1F527|🔧|wrench
230|E6|11100110|U+2699|⚙|gear
231|E7|11100111|U+2696|⚖|balance scale
232|E8|11101000|U+26D3|⛓|chains
233|E9|11101001|U+1F9F2|🧲|magnet
234|EA|11101010|U+1F9EA|🧪|test tube
235|EB|11101011|U+1F9EC|🧬|dna
236|EC|11101100|U+1F52D|🔭|telescope
237|ED|11101101|U+1F6AA|🚪|door
238|EE|11101110|U+1F6CF|🛏|bed
239|EF|11101111|U+1F6BD|🚽|toilet
240|F0|11110000|U+1F6BF|🚿|shower
241|F1|11110001|U+1F9F9|🧹|broom
242|F2|11110010|U+1F9FB|🧻|roll of paper
243|F3|11110011|U+1F9FC|🧼|soap
244|F4|11110100|U+1F9EF|🧯|fire extinguisher
245|F5|11110101|U+1F6D2|🛒|shopping cart
246|F6|11110110|U+1F6B8|🚸|children crossing
247|F7|11110111|U+1F6AB|🚫|prohibited
248|F8|11111000|U+2B06|⬆|up arrow
249|F9|11111001|U+1F504|🔄|counterclockwise arrows button
250|FA|11111010|U+23F8|⏸|pause button
251|FB|11111011|U+1F4F6|📶|antenna bars
252|FC|11111100|U+2797|➗|divide
253|FD|11111101|U+2753|❓|question mark
254|FE|11111110|U+2714|✔|check mark
255|FF|11111111|U+1F3C1|🏁|chequered flag
