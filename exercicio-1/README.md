# Exercício 1

O arquivo [blog/post01.html](blog/post01.html) contém o HTML de uma das
páginas do site de cursos online da Computação@UFCG. O site está sendo
projetado para ter uma página semelhante à fornecida para cada um dos
cursos que serão disponibilizados (cada uma dessas páginas terá
estruturação interna semelhante).  Pede-se que você projete e escreva as
folhas de estilo CSS necessárias para renderizar e estilizar as páginas.

## Requisitos

Você não deve adicionar ou remover elementos do HTML (também não deve
mudar qualquer elemento de seu lugar na hierarquia). O único tipo de
mudança que você pode fazer é adicionar atributos aos elementos
existentes, de forma que venham a servir como _contrato_ entre o HTML e
o CSS (obviamente, mudanças equivalentes serão feitas nas demais
páginas).

Quanto à apresentação e estiização, o CSS produzido deve fazer com que a
renderização da página no browser se aproxime o máximo possível à
mostrada na imagem de [referência](referencia.png).

Por fim, você deve garantir que o 
CSS criado seja válido (e que o HTML continue sendo válido). Para
testar a validade do CSS use o [Validador Online de CSS do
W3C](http://jigsaw.w3.org/css-validator/). Para testar a validade
do HTML você pode usar o [Validador Online de HTML do W3C]() ou
usar os testes automáticos fornecidos com a questão (use o
Makefile para executá-los; basta digitar `make`).

> **Dica** O Makefile executa um teste automático para verificar
> se os elementos originais estão sendo mantidos no HTML (estude
> o código Python e a API do Beautiful Soup caso queira entender
> o teste; é uma ferramenta que pode ser muito útil em diversos
> projetos). O teste fornecido também verifica se o HTML é válido
> de acordo com o Validador Online do W3C. Para rodar os testes,
> use o comando `make`.
