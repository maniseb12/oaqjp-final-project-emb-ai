import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.p.cloud.ibm.com/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=headers)
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # Extracting the emotion scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Logic to find the dominant emotion
    # Use max() to find the key with the highest value
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Formatting the output as required by the project
    emotions['dominant_emotion'] = dominant_emotion
    
    return emotions
