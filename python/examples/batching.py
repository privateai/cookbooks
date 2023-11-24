# Example script to illustrate how to make API calls to the Private AI cloud API
# to deidentify a text using the batching feature.
#
# To use this script with the Cloud API, please request an API key https://www.private-ai.com/start/
#
# To use this script with a local container, simply replace the url 'api.private-ai.com' with your 
# local url ( such as 'localhost:8080' ). See instructions at https://private-ai.com/docs/installation
# for setting up containers.
#
# In order to use the API key issued by Private AI< you can run the script as
# `PRIVATEAI_API_KEY=<your key here> python async_call.py` or you can define a `.env` file
# which has the line `PRIVATEAI_API_KEY=<your key here>`.

import os
import dotenv
from privateai_client import PAIClient, request_objects

# Use to load the API KEY for authentication
dotenv.load_dotenv()

# On initialization
client = PAIClient("https", "api.private-ai.com/deid", api_key=os.environ["PRIVATEAI_API_KEY"])

entity_detection_obj = request_objects.entity_detection_obj(
    accuracy="high", return_entity=True)
processed_text_obj = request_objects.processed_text_obj(type="MARKER")

process_text_request = request_objects.process_text_obj(
    text=["Hi, my name is Penelope, could you tell me your phone number please?",
          "Sure, x234",
          "and your DOB please?",
          "fourth of Feb nineteen 86"],
    link_batch=True,
    entity_detection=entity_detection_obj,
    processed_text=processed_text_obj
)

response = client.process_text(process_text_request)
print(response.processed_text)
