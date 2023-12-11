import os
import warnings
from typing import Dict

from openfabric_pysdk.utility import SchemaUtil

from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import Ray, State
from openfabric_pysdk.loader import ConfigClass

from flanbot.flanbot import init_model, generate

# initialize the model
model = init_model()

############################################################
# Callback function called on update config
############################################################
def config(configuration: Dict[str, ConfigClass], state: State):
    # log configuration and state changes
    print(configuration)
    print(state)


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: Ray, state: State) -> SimpleText:
    output = []

    for text in request.text:
        try:
            # TODO Add code here
            # adding prompt prefix to the question
            text = "Please answer the following question: " + text
            # generating the response from flanbot
            response = generate(model, text)
            output.append(response)

        except Exception as e:
            # logging the exception
            print("Error: ",e)
            output.append("Whoops! A small hiccup occurred. No worries, please give it another try when you're ready. We appreciate your patience!")


    return SchemaUtil.create(SimpleText(), dict(text=output))
