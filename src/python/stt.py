import whisper

stt_modle = whisper.load_model('small')

def stt(audio):
    result = stt_modle.transcribe(audio)
    return result['test']
