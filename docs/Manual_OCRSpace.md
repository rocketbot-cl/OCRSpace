



# OCR Space
  
Este módulo permite extraer texto de imágenes o archivos PDF utilizando la API de OCR.space.  

*Read this in other languages: [English](Manual_OCRSpace.md), [Português](Manual_OCRSpace.pr.md), [Español](Manual_OCRSpace.es.md)*
  
![banner](imgs/Banner_OCRSpace.png o jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Como usar este modulo

Para usar este modulo sigue los pasos que se indican a continuación:

1. Dirígete a la página de OCRSpace (https://ocr.space/OCRAPI) para obtener una API Key.
2. Si desea obtener una API Key Gratuita debe registrarse https://ocr.space/ocrapi/freekey. 
3. En el formulario de registro, debe proporcionar email, nombre, apellido y el proposito de la solicitud.
4. Una vez enviado el formulario le llegara a su email  un correo de confirmacion.
5. Por ultimo le enviaran un segundo email con la  API Key generada que debera usar en el modulo en la seccion Key OCR Space.

## Nuevas Caracteristicas

1. Se añadio a este modulo la opcion de seleccionar eL OCR Engine que se desea usar, visite la pagina https://ocr.space/OCRAPI#ocrengine de esta forma si selecciona el Engine 1 debe seleccionar el lenguaje mientras que con el Engine 2 no es necesario.
2. Se añadio opcion para seleccionar la presentacion de los resultados, con esto los resultados podran ser presentados como, 
lista de palabras, lista de lineas o texto plano.
3. Checkbox Aplicar Escala: al seleccionar aplica un aumeto de escala interno al documento.
4. Checkbox Interpretar Tabla: al seleccionar se lee la tabla linea por linea https://ocr.space/tablerecognition. 


## Descripción de los comandos

### OCR Space convertir archivo
  
Extrae texto de un archivo.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Archivo||archivo.pdf|
|Key de OCR.Space||12345678|
|OCR Engine||Engine 1|
|Idioma||Español|
|Resultado||Variable|
|Presentacion Resultados||Default|
|Aplicar Escala|Si se marca esta casilla, realiza un aumento de escala interno|True|
|Interpretar tabla|Si se marca esta casilla, el resultado se ordena línea por línea.|True|
