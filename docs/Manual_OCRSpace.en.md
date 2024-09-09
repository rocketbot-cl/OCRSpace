



# OCR Space
  
This module allows you to extract text from images or PDF files using the OCR.space API.  

*Read this in other languages: [English](Manual_OCRSpace.md), [Português](Manual_OCRSpace.pr.md), [Español](Manual_OCRSpace.es.md)*
  
![banner](imgs/Banner_OCRSpace.png o jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## How to use this module

To use this module, follow the steps below:

1. Go to the OCRSpace page (https://ocr.space/OCRAPI) to get an API Key.
2. If you want to get a Free API Key, you must register at https://ocr.space/ocrapi/freekey.
3. In the registration form, you must provide your email, first name, last name, and the purpose of the request.
4. After submitting the form, you will receive a confirmation email.
5. Finally, you will receive a second email with the generated API Key that you must use in the module in the OCR Space Key section.

## New Features

1. OCR Engine Selection: The option to select the desired OCR engine has been added. Visit https://ocr.space/OCRAPI#ocrengine for more details. When selecting Engine 1, you must select the language, while with Engine 2 it is not necessary.
2. Result Presentation: The option to select how the results will be presented has been added, such as word list, line list, or plain text.
3. Apply Scale: When this option is checked, an 
internal scale will be applied to the document.
4. Read Table: When this option is checked, the table will be read line by line. For more information, visit https://ocr.space/tablerecognition.

## Description of the commands

### OCR Space convert file
  
Extract text from file.
|Parameters|Description|example|
| --- | --- | --- |
|File||file.pdf|
|Key OCR.Space||12345678|
|OCR Engine||Engine 1|
|Language||English|
|Result||Variable|
|Results presentation||Default|
|Apply scale|If this box is checked, does some internal upscaling|True|
|Read a table|If this box is checked, result text is sorted line by line.|True|
