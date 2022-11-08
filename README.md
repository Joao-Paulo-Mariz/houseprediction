# Previsão de preços de compra ou venda de imóveis da cidade de Belo Horizonte
    
Esse projeto visa demonstrar meu conhecimento sobre as etapas de um projeto de data science com a utilização de importantes frameworks para essa tarefa.
![imovel](https://cdn.pixabay.com/photo/2021/10/07/15/23/real-estate-6688945_960_720.jpg)
## Contexto
    
O setor imobiliário é de extrema importância para a economia nacional, tendo em vista que gera riquezas não apenas para sua área mas também em outros setores como construção civil e finanças. Isso tudo pode ser evidenciado com seus números. Segundo a associação de dirigentes de empresas do mercado imobiliário, o setor gerou quase R$ 100 bilhões no ano de 2021 e a tendência é de crescimento para os próximos anos em um mundo sem pandemia.
     
## Problema de negócio
     
Uma empresa hipotética do setor imobiliário trabalha com compra e venda de imóveis. Como regra de negócio, a empresa trabalha com ofertas inicias de 12% menor que o preço "justo" de mercado para atividade de compra e 7% maior para vendas.
       
## Entrega do projeto
     
A entrega do projeto será por meio de um WEB APP hibrido, tanto para compras com vendas, com a previsão do preço e do valor de compra ou venda.
    
## Fluxo prático do projeto
    
## Fase 1 - Obtenção dos dados
    
A primeira fase foi caracterizada pelo processo de obtenção dos dados por meio de web scraping em um site de imobiliária, bem como o tratamento desses dados e seu armazenamento em um banco de dados MongoDB dos dados já limpos para análise posterior.

## Fase 2 - Análise exploratória de dados, criação do modelo e sua avaliação
    
Essa fase do projeto é constituída por análise exploratória de dados, pré-processamento, construção do modelo preditivo e sua avaliação. Na primeira etapa será realizada uma análise estatística e visual das observações obtidas na fase 1, web scraping de dados imobiliários. A partir dessa primeira análise terá início o pré-processamento, ou seja, os dados serão preparados de acordo com suas características observadas anteriormente para criação do modelo de machine learning. Essa terceira etapa começará com a comparação de diversos algoritimos de machine learning, depois o melhor modelo passará por um turning de hiperparâmetros visando refinar seu resultado e, por fim, será treinado, avaliado e salvo para a próxima etapa, deploy.

## [Fase 3 - Deploy do modelo preditivo](https://joao-paulo-mariz-houseprediction-fase3-deployapp-esnydl.streamlit.app/)
        
A terceira fase compreendeu a construção de um APP em Streamlit para o deploy do modelo preditivo. Com o APP o usuário poderá colocar informações de imóveis e terá como retorno o valor previsto, valor de compra ou venda e gráficos que permitirá o usuário entender qual dado foi mais importante para o valor do imóvel e assim poder explicar a terceiros.
