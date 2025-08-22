from deep_translator import GoogleTranslator

def traduzir_para_espanhol(texto):
    translator = GoogleTranslator(source='pt', target='es')
    return translator.translate(texto)
