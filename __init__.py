# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
from time import sleep
import json
import requests


"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

"""
    Resuelvo catpcha tipo reCaptchav2
"""

def ocr_space_file(filename, overlay=False, api_key='helloworld', engine=1, scale=False, isTable=False, language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param engine: OCR engine to use.
                    Defaults to 1. 
    :param scale: Apply internal upscaling.
                    Defaults to False.
    :param isTable: Read a table.
                    Defaults to False.                                               
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """
    try:
        payload = {'isOverlayRequired': overlay,
                'apikey': api_key,
                'language': language,
                'scale': scale,
                'isTable': isTable,
                'OCREngine': engine,
                }
        with open(filename, 'rb') as f:
            r = requests.post('https://api.ocr.space/parse/image',
                            files={filename: f},
                            data=payload,
                            verify=False
                            )
        return r.json()
    except Exception as e:
        PrintException()
        raise e
def extract_line_text(json_data, res):
    """Extrae datos específicos del JSON según el valor de 'res'.
    :param json_data: The JSON data as a Python dictionary
    :param res: A string indicating which type of data to extract
    :return: A list containing the extracted data.        
    """
    try:
        data = []
        if res == "LineText":
            for parsed_result in json_data['ParsedResults']:
                for line in parsed_result['TextOverlay']['Lines']:
                    data.append(line['LineText'])
        elif res == "WordText":
            for parsed_result in json_data['ParsedResults']:
                for line in parsed_result['TextOverlay']['Lines']:
                    for word in line['Words']:
                        data.append(word['WordText'])
        elif res == "ParsedText":
            for parsed_result in json_data['ParsedResults']:
                 #parsed_result.replace('\t', '').replace('\r\n', '')
                 data.append(parsed_result['ParsedText'].replace('\t', '').replace('\r\n', '').replace('\n', ''))
        return data
    except Exception as e:
        PrintException()
        raise e

    
if module == "GetOCR":
    File = GetParams("File")
    Key = GetParams("key")
    var_ = GetParams("result")
    ocr = GetParams("engine")
    lang = GetParams("lang")
    xScale = GetParams("scale")
    xTable = GetParams("table")
    res = GetParams("res")
    if ocr:
  
        data = ocr_space_file(File,overlay=True, api_key=Key, engine=ocr, scale=xScale, isTable=xTable, language=lang)
        
    else:

        data = ocr_space_file(File,overlay=True, api_key=Key)
    if res:
         data = extract_line_text(data, res)
    try:
        SetVar( var_,  data)
    except Exception as e:
        raise Exception(e)
