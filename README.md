[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/jmontejr/tecnicas-preditivas-para-auxilio-no-diagnostico-de-melanomas-via-images/blob/main/README.en.md)

# Técnicas preditivas para auxílio no diagnóstico de melanomas via imagens

Este repositório contém o código fonte das implementações dos experimentos utilizados para o projeto apresentado na Monografia apresentada ao Curso de Bacharelado em Sistemas de Informação da Universidade Federal Rural de Pernambuco, como requisito parcial para obtenção do título de Bacharel em Sistemas de Informação.

## Tabela de Conteúdos

- [Detalhes do projeto](#detalhes-do-projeto)
- [Resumo](#resumo)
  - [Palavras-chave](#palavras-chave)
- [Conjunto de dados](#conjunto-de-dados)
  - [Como encontrar e utilizar os dados para reproduzir este trabalho](#como-encontrar-e-utilizar-os-dados-para-reproduzir-este-trabalho)

## Detalhes do projeto

**Autor:** José Carlos Monte Silva Júnior  
**Orientador:** Prof. Dr. Rodrigo Gabriel Ferreira Soares  
**Instituição:** Universidade Federal Rural de Pernambuco - UFRPE  
**Departamento:** Departamento de Estatística e Informática - DEINFO  
**Curso:** Curso de Bacharelado em Sistemas de Informação  
**Local e data de publicação:** Recife, 2024  
**Defendido e aprovado em:** 02/10/2024  
**URI**: [https://repository.ufrpe.br/handle/123456789/6372](https://repository.ufrpe.br/handle/123456789/6372)

## Resumo

O câncer de pele é o tipo mais comum de câncer no mundo, dividido em dois tipos principais: melanoma e não melanoma. Embora mais raro, o melanoma é o mais letal devido ao seu potencial de causar metástase. Métodos não invasivos, como a dermatoscopia e a regra ABCDE, têm sido utilizados para evitar procedimentos cirúrgicos desnecessários e têm ajudado na identificação de lesões, contribuindo para diagnósticos mais rápidos. Com o avanço da tecnologia, a Inteligência Artificial (IA) ganhou destaque, mostrando-se uma solução promissora para a análise de dados médicos, especialmente com o uso de Redes Neurais Convolucionais (RNCs), que podem reconhecer padrões em imagens dermatoscópicas e ajudar na classificação de lesões como melanoma ou não melanoma de forma automatizada. Este projeto propõe um comitê de classificadores baseado em Redes Neurais Convolucionais para classificar imagens dermatoscópicas como melanoma ou não melanoma, comparando seu desempenho com arquiteturas validadas, como AlexNet e VGG-16, utilizando técnicas de Transfer Learning. As análises de Precisão, Revocação e Pontuação F1 mostraram que o comitê de Redes Neurais Convolucionais superou os modelos que utilizam técnicas de Transfer Learning, com a AlexNet apresentando desempenho superior à VGG-16. O comitê de Redes Neurais Convolucionais demonstrou uma maior capacidade de generalização, mostrando-se promissor ao capturar as características relevantes das imagens, revelando potencial para aplicações médicas, embora ainda precise ser refinado para atingir padrões clínicos.

### Palavras-chave

Câncer de Pele, Aprendizado de Máquina, Técnicas de Comitês, Redes Neurais Convolucionais, Aprendizado por Transferência.

## Conjunto de dados

Para o experimento, foram escolhidas as imagens do arquivo do [ISIC Challenge](https://challenge.isic-archive.com/). Foram utilizadas as 2.5331 imagens do conjunto de treinamento do desafio [ISIC Challenge 2019](https://challenge.isic-archive.com/data/#2019), pois possuem a Ground Truth, que é essencial para garantir a precisão e confiabilidade dos dados.

### Como encontrar e utilizar os dados para reproduzir este trabalho?

Devido ao tamanho do conjunto de dados, os arquivos contendo as imagens das lesões dermatoscópicas não foram incluídos neste repositório. No entanto, esses arquivos podem ser encontrados na página oficial do desafio: [ISIC Challenge 2019 - Training Data](https://isic-challenge-data.s3.amazonaws.com/2019/ISIC_2019_Training_Input.zip). O arquivo com a Ground Truth de treinamento está disponível em `src/data/ISIC_2019_Training_GroundTruth.csv`, além de poder ser acessado na página oficial do desafio, assim como as imagens.

Ao baixar os arquivos, as imagens devem ser colocadas na pasta `src/data/images` para que os experimentos possam ser reproduzidos.
