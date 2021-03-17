import os
from pa import GenericAssistant

pa = GenericAssistant(os.path.join("data","intents.json"), model_name="test_model")
pa.train_model()
pa.save_model()

done = False

while not done:
    message = input("Enter a message: ")
    if message == "STOP":
        done = True
    else:
        pa.request(message)