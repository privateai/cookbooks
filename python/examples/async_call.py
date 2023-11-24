# Example script to illustrate how to make API calls to the Private AI Docker
# container to deidentify text.
#
# To use this script with the Cloud API, please request an API key https://www.private-ai.com/start/
#
# To use this script with a local container, simply replace the url 'https://api.private-ai.com/deid' with your 
# local url ( such as 'http://localhost:8080' ). See instructions at https://private-ai.com/docs/installation
# for setting up containers.
#
# In order to use the API key issued by Private AI< you can run the script as
# `PRIVATEAI_API_KEY=<your key here> python async_call.py` or you can define a `.env` file
# which has the line `PRIVATEAI_API_KEY=<your key here>`.
#
#


import os
import pprint
import asyncio
from typing import Dict

import aiohttp
import requests
import dotenv


# Define an asynchronous function using the aiohttp library.
async def async_aiohttp_call() -> None:

    headers = {"Content-Type": "application/json", "x-api-key": os.environ["PRIVATEAI_API_KEY"] }

    # create an asynchronous aiohttp client session
    async with aiohttp.ClientSession(headers=headers) as session:

        # create an asynchronous aiohttp post call
        async with session.post(
            url="https://api.private-ai.com/deid/v3/process/text",
            json={
                "text": ["My name is John and my friend is Grace."],
               
            }
        ) as response:

            # print the deidentified text
            pprint.pprint(await response.json())


# Turn synchronous post call from the requests library to an asynchronous call.
async def async_post(
    url: str,
    json: Dict[str, str],
    headers: str
) -> requests.Response:
    return requests.post(
        url=url,
        json=json,
        headers=headers
    )


async def async_requests_call() -> None:
    response = await async_post(
        url="https://api.private-ai.com/deid/v3/process/text",
        json={
            "text": ["My name is John and my friend is Grace."],
           
        },
        headers = {"Content-Type": "application/json", "x-api-key": os.environ["PRIVATEAI_API_KEY"] }

    )

    # check if the request was successful
    response.raise_for_status()

    # print the result in a readable way
    pprint.pprint(response.json())


if __name__ == "__main__":
    
    # Use to load the API key for authentication
    dotenv.load_dotenv()
    
    # Check if the API_KEY environment variable is set
    if "PRIVATEAI_API_KEY" not in os.environ:
        raise KeyError("PRIVATEAI_API_KEY must be defined in order to run the examples with the Cloud API.")

    # Run the examples
    asyncio.run(async_aiohttp_call())
    asyncio.run(async_requests_call())
