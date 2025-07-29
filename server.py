import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/apininjas/api/weather-by-api-ninjas'

mcp = FastMCP('weather-by-api-ninjas')

@mcp.tool()
def v1_weather(lat: Annotated[Union[int, float, None], Field(description='Latitude of desired location. If used, lon parameter must also be supplied. Default: 0')] = None,
               lon: Annotated[Union[str, None], Field(description='Longitude of desired location. If used, lat parameter must also be supplied.')] = None,
               zip: Annotated[Union[int, float, None], Field(description='5-digit Zip code (United States only). Default: 0')] = None,
               city: Annotated[Union[str, None], Field(description='City name.')] = None,
               state: Annotated[Union[str, None], Field(description='US state (United States only).')] = None,
               country: Annotated[Union[str, None], Field(description='Country name.')] = None) -> dict: 
    '''API Ninjas Weather API endpoint.'''
    url = 'https://weather-by-api-ninjas.p.rapidapi.com/v1/weather'
    headers = {'x-rapidapi-host': 'weather-by-api-ninjas.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'lat': lat,
        'lon': lon,
        'zip': zip,
        'city': city,
        'state': state,
        'country': country,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
