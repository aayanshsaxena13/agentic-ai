from googletrans import Translator

async def translate(text, src, dest):
    helper = Translator()
    translation = await helper.translate(text=text, src=src, dest=dest)
    return translation.text
