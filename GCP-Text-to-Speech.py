from google.cloud import texttospeech
#fi=''
#fo=''
def s(v,g='f'):
    v=v.upper()
    """Synthesizes speech from the input file of ssml.
    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/
    """
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()
    with open(fi, "r") as f:
        ssml = f.read()
        input_text = texttospeech.SynthesisInput(ssml=ssml)
    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    if g=='m':
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US", 
            name="en-US-Wavenet-"+v,
            ssml_gender=texttospeech.SsmlVoiceGender.MALE,
        )
    else:
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US", 
            name="en-US-Wavenet-"+v,
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )
    # The response's audio_content is binary.
    with open(fo, "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
