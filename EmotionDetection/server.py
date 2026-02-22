# Launch python
python3

# Import the function from the package
from EmotionDetection.emotion_detection import emotion_detector

# Test with a sample string
result = emotion_detector("I am so happy that I am learning how to package Python apps!")

# Print the result to verify the dominant_emotion is present
print(result)
