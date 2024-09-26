# doghouse/designer.py

from openai import OpenAI
import requests
import logging
from .models import *

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize OpenAI client
client = OpenAI()

def get_user_ip(request):
    # Get user ip from request
    # if request.headers.get("X-Forwarded-For"):
    #     user_ip = request.headers.get('X-Forwarded-For').split(',')[0]
    # else:
    #     user_ip = request.remote_addr
    # return user_ip
    user_ip = '188.180.95.94' # since we run the app locally, our IP is always 127.0.0.1, so for simplicity we just return a hardcoded value
    return user_ip

# Tool: Detect city by IP
def detect_city_by_ip(ip_address):
    """
    Detects the city based on the provided IP address.
    """
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json', timeout=5)
        data = response.json()
        city = data.get('city', 'Unknown');
        return city
    except Exception as e:
        print(f"Error detecting city for IP {ip_address}: {e}")
        return "Unknown"

# Task: Generate user prompt
def compose_user_prompt(style, size, color):
    """
    Composes a prompt for the user based on provided parameters.
    """
    user_prompt = f"Suggest a doghouse based on these preferences: style: {style}, size: {size}, color: {color}."
    return user_prompt

# RAG Step: Retrieve additional information
def retrieve_additional_info(climate):
    """
    Retrieves additional information from the models based on user preferences.
    """
    # Example: Fetching similar products as additional context
    recommendations = climate_recommendations.get(climate, climate_recommendations['temperate'])
    return recommendations

def detect_climate_by_city(city):
    """
    Returns the climate description based on the city name.
    Defaults to 'temperate' if the city is not in the mapping.
    """
    # Get the climate zone for the city
    climate = city_climate_mapping.get(city, 'default')
    return climate

# Workflow: Generate doghouse suggestion
def generate_doghouse_suggestion_workflow(style, size, color, user_ip):
    # Detect city from IP
    city = detect_city_by_ip(user_ip)

    climate = detect_climate_by_city(city)
    
    # Compose user prompt
    user_prompt = compose_user_prompt(style, size, color)
    
    # Retrieve additional information
    additional_info = retrieve_additional_info(climate)
    
    # Create system prompt with additional context
    system_prompt = (
        f"Create a short but detailed visual description of a doghouse for an image generation, based on the following details:\n"
        f"1. It has a small flag of the country where {city} is located, on top of the roof.\n"
        f"2. Location: {city}.\n"
        f"3. Climate: {additional_info} (describe how the climate influences the design).\n"
        f"4. Include specific design features that fit the location and climate.\n"
        f"Ensure the description is vivid and focused on visual elements."
    )    

    house_suggestion = generate_suggestion(user_prompt, system_prompt)
    image_url = generate_image(house_suggestion)
    return house_suggestion, image_url


# Generate doghouse suggestion
def generate_suggestion(user_prompt, system_prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=100
    )
    return response.choices[0].message.content.strip()
    
# Generate image for the suggested doghouse
def generate_image(house_suggestion):
    response = client.images.generate(
        model="dall-e-3",
        prompt=house_suggestion,
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url
    return image_url
    

def generate_doghouse_suggestion(request):
    """
    Main function to handle the generation of a doghouse suggestion.
    """
    style = request.form['style']
    size = request.form['size']
    color = request.form['color']
    # location = request.form['location']
    user_ip = get_user_ip(request)
    house_suggestion, image_url = generate_doghouse_suggestion_workflow(style, size, color, user_ip)
    return house_suggestion, image_url
