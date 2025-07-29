markdown
# Weather by API-Ninjas MCP Server

## Overview

Welcome to the Weather by API-Ninjas MCP Server! This server provides access to the latest weather information for any city or geographic location worldwide. With its robust features, users can retrieve real-time weather data effortlessly.

### Features

- **Global Coverage**: Access weather data for any region around the globe.
- **Multiple Input Options**: Retrieve weather information using latitude and longitude, ZIP code (US only), city name, state (US only), and country name.

### Tools

The MCP server offers a range of tools designed to provide comprehensive weather data. Below is a detailed list of the available tools and their functionalities:

#### `/v1/weather` Endpoint

- **Function**: `v1_weather`
  - **Description**: This endpoint allows users to access the latest weather information.
  - **Parameters**:
    - **lat**: Latitude of the desired location. When used, the `lon` parameter must also be supplied. *(Type: Number, Default: 0)*
    - **lon**: Longitude of the desired location. When used, the `lat` parameter must also be supplied. *(Type: String)*
    - **zip**: 5-digit ZIP code (United States only). *(Type: Number, Default: 0)*
    - **city**: Name of the city. *(Type: String)*
    - **state**: US state (United States only). *(Type: String)*
    - **country**: Name of the country. *(Type: String)*

### Subscription Plans

The MCP server offers various subscription plans to suit different needs, ranging from basic to mega plans. Each plan is designed to provide optimal service levels and latency to ensure seamless access to weather data.

Explore the features of Weather by API-Ninjas and experience the ease of retrieving accurate weather information tailored to your requirements!