# fastapi-dummy-classifier
The task is to write FastAPI app with '/predict' endpoint. The app does the following:
a) loads a dummy classifier
b) Accepts POST requests with JSON with 4 fields e.g.: {"features": [5.1, 3.5, 1.4, 0.2]}
c) Return a prediction in JSON format e.g.: {"prediction": "class A"}

## Overview
1. Classifier used is dummy classifier. It takes the 1st feature i.e. in the features array only 1st element, feature[0]
   is considered. A rule based approach is used to classify the value into classes A, B, C, D<br>
   if features[0] < 1.0 => class A<br>
   if 1.0 <= features[0] < 2.0 => class B<br>
   ...
3. Response is returned in JSON format

## Usage
1. Build the docker image using the command:
   docker build -t fastapi-dummy-classifier .<br>
   This will build the image 'fastapi-dummy-classifier'
3. Start the server at the port 8000:
   docker run -p 8000:8000 -it fastapi-dummy-classifier<br>
5. Test the app using the following command:
   curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"features": [3.1, 3.5, 1.4, 0.2]}'
7. Response recieved would be in the format:
   {"prediction":"class D"}
