



# OCR Space
  
Este módulo permite extrair texto de imagens ou arquivos PDF usando a API OCR.space.  

*Read this in other languages: [English](Manual_OCRSpace.md), [Português](Manual_OCRSpace.pr.md), [Español](Manual_OCRSpace.es.md)*
  
![banner](imgs/Banner_OCRSpace.png o jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Como usar este módulo

Para usar este módulo, siga os passos abaixo:

1. Acesse a página do OCRSpace (https://ocr.space/OCRAPI) para obter uma API Key.
2. Se deseja obter uma API Key Gratuita, você deve se registrar em https://ocr.space/ocrapi/freekey.
3. No formulário de registro, você deve fornecer seu email, nome, sobrenome e o propósito da solicitação.
4. Após enviar o formulário, você receberá um email de confirmação.
5. Por fim, você receberá um segundo email com a API Key gerada que deverá ser utilizada no módulo na seção Key OCR Space.

## Novas Funcionalidades

1. Seleção do Motor OCR: Foi adicionada a opção de selecionar o motor OCR que você deseja utilizar. Visite a página https://ocr.space/OCRAPI#ocrengine para mais detalhes. Ao selecionar o Motor 1, você deverá selecionar a linguagem, enquanto que com o Motor 2 não é necessário.
2. Formatação dos Resultados: Foi adicionada a opção de selecionar a forma como os resultados serão apresentados, como lista de palavras, 
lista de linhas ou texto plano.
3. Aplicar Escala: Ao marcar esta opção, uma escala interna será aplicada ao documento.
4. Interpretar Tabela: Ao marcar esta opção, a tabela será lida linha por linha. Para mais informações, visite https://ocr.space/tablerecognition.
## Descrição do comando

### OCR Space converter arquivo
  
Extrair texto de um arquivo.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Arquivo||arquivo.pdf|
|Key do OCR.Space||12345678|
|OCR Engine||Engine 1|
|Linguagem||Portuguese|
|Resultado||Variável|
|Apresentação dos resultados||Default|
|Aplicar escala|Se esta caixa estiver marcada, realiza um aumento de escala interno.|True|
|Detecção de tabelas|Se esta caixa estiver marcada, O resultado é classificado linha por linha.|True|
