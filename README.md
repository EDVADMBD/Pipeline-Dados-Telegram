# Pipeline-Dados-Telegram
## Contexto : 
O objetivo deste projeto foi implementar um pipeline dados para analisar mensagens em um grupo do telegram. 
O pipeline foi implementado utilizado serviços da Amzon Web Services (AWS). 
Além disso ele e Projeto de conclusão do Curso Analista de dados pela EBAC.

## Descrição

1. Telegram:
 >Grupo: Representa um grupo no Telegram.

 >Bot: Refere-se a um bot no Telegram.

2. AWS:

  2.1 Ingestão:
 > API Gateway: Recebe entrada do usuário e se conecta a uma função Lambda.

 >Essa função Lambda aponta para um bucket S3.

  2.2 ETL (Extract, Transform, Load):

  >Event Bridge: Recebe dados do bucket S3 na seção de Ingestão.
  
  >Outra função Lambda também aponta para um segundo bucket S3.
3. Apresentação:

> Apenas um elemento chamado “Athena” conectado ao segundo bucket S3 na seção ETL.



## Links Relacionados 

[Colab parte 1](https://colab.research.google.com/drive/1vvOWMZjFemcMAU44P0cZb2TTAgdbqxkq?usp=sharing)

[Colab Parte 2](https://colab.research.google.com/drive/1GGP7tA5BCyfRvMQrHM3YyWmxS3OCbUsZ?usp=sharing) 

[Kaggle](https://www.kaggle.com/code/ricardofilgueiras/telegram-pipeline)