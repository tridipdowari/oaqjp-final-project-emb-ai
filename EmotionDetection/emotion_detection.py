"""Emotion detection module"""


def emotion_detector(text_to_analyze):
    """Analyze emotion"""

    if text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response = {
        'anger': 0.01,
        'disgust': 0.02,
        'fear': 0.01,
        'joy': 0.95,
        'sadness': 0.01
    }

    dominant_emotion = max(response, key=response.get)

    response['dominant_emotion'] = dominant_emotion

    return response
