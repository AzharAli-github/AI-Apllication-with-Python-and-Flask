import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=data, timeout=10)

    if response.status_code != 200:
        return {"error": "API request failed"}

    emotions = response.json().get("document", {}).get("emotion", {})
    
    result = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
    }
    
    result['dominant_emotion'] = max(result, key=result.get)
    
    return result

# Example test
print(emotion_detector("I am so happy I am doing this."))
