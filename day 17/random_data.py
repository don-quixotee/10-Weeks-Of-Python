''' module to create basic random data '''
import random

first_names = [ 'ananya' , 'ankit' , 'anuj', 'arti' , 'akash', 'pranay', 'rishav' , 'rama' , 'shiva' , 'saumya' , 'shivani' , 'shivay', 'suraj' , 'swapnil' , 'neeraj', 'amod' , 'ajay' , 'rakesh', 'karan', 'sujay', 'vijay', 'anajan', 'noor', 'nweda', 'naina', 'meena', 'deepthi', 'neha', 'manuj', 'shrishti', 'swati', 'prerna', 'anjana', 'shavita', 'dheeraj', 'arun']

last_names = ['singh', 'mehta', 'kumar', 'malhotra', 'baneerjee', 'panday', 'chauhan', 'bains', 'upadhayay', 'gowda', 'jha', 'thakur', 'phagot', 'shrivastava', 'kaur', 'gill', 'rathor', 'sharma', 'varma', 'modi', 'sindhiya', 'yadava', 'prashad', 'arora', 'gahlot', 'chaudhary', 'prakash', 'dube', 'chadda', 'khan', 'aryan', 'roy', 'ranaut', 'shukla', 'mitra', 'kashyap', 'desai', 'kakkar', 'singh']

street_names = ['1st cross ', '2nd cross', '100 main', '13th cross', 'lake street', 'old town', 'main bajar', 'new district', 'mall road', 'jail road', '7th cross', '10th main']

fake_cities = ['bandra', 'sundarnagar', 'vijaynagar', 'alpha' , 'beeta', 'faketown', 'bigtown', 'goldtown', 'naturetown', 'indara vihar', 'lake city ', 'rivertown', 'anam vihar', 'vidyanagar', 'alpha nagar', 'beetanagar']

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

for num in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)

    phone = f'{random.randint(100, 999)}-555-{random.randint(1000,9999)}'

    street_num = random.randint(100, 999)
    street = random.choice(street_names)
    city = random.choice(fake_cities)
    state = random.choice(states)
    zip_code = random.randint(10000, 99999)
    address = f'{street_num} {street} St., {city} {state} {zip_code}'

    email = first.lower() + last.lower() + '@bogusemail.com'

    print(f'{first} {last}\n{phone}\n{address}\n{email}\n')
