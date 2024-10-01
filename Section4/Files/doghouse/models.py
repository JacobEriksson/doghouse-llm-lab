products = [
    {'id': 1, 'name': 'Doghouse Classic', 'price': 49.99, 'description': 'A cozy place for your dog to rest.', 'image': 'classic_doghouse.png'},
    {'id': 2, 'name': 'Deluxe Doghouse', 'price': 89.99, 'description': 'A luxurious doghouse with extra space.', 'image': 'deluxe_doghouse.png'},
    {'id': 3, 'name': 'Portable Doghouse', 'price': 39.99, 'description': 'A lightweight doghouse perfect for travel.', 'image': 'portable_doghouse.png'},
]

# Climate data based on common cities or regions
city_climate_mapping = {
    'Miami': 'tropical',
    'Las Vegas': 'arid',
    'New York': 'temperate',
    'Toronto': 'cold',
    'London': 'temperate',
    'Tokyo': 'temperate',
    'Sydney': 'arid',
    'Dubai': 'arid',
    'Mumbai': 'tropical',
    'Copenhagen': 'cold',
    'Stockholm': 'cold', 
    'Amsterdam': 'temperate',
    # Default to temperate if the city is unknown
    'default': 'temperate'
}

# Descriptions of the climate zones for the system prompt
climate_recommendations = {
    'tropical': 'Hot and humid climate, suitable for ventilated and heat-resistant materials.',
    'arid': 'Dry and hot climate, ideal for insulated and durable materials.',
    'temperate': 'Mild climate with seasonal variations, suitable for all-weather materials.',
    'cold': 'Cold climate, best for insulated and heat-retaining materials.'
}