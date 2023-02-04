import speech_recognition as sr

# Set up the speech recognition recognizer
r = sr.Recognizer()

# Create a list of known speakers and their voice samples
known_speakers = {
    "Speaker 1": "speaker1_sample.wav",
    "Speaker 2": "speaker2_sample.wav",
    "Speaker 3": "speaker3_sample.wav"
}

# Load the voice samples for each speaker
speaker_samples = {}
for speaker, sample_file in known_speakers.items():
    with sr.AudioFile(sample_file) as source:
        sample = r.record(source)
        speaker_samples[speaker] = sample

# Read in an unknown speaker's voice sample
with sr.AudioFile("unknown_speaker_sample.wav") as source:
    unknown_sample = r.record(source)

# Compare the unknown speaker's sample to the known speaker samples
scores = {}
for speaker, sample in speaker_samples.items():
    score = r.recognize_google(unknown_sample, sample=sample)
    scores[speaker] = score

# Identify the speaker with the highest score
best_match = max(scores, key=scores.get)
print(f"Best match: {best_match}")
