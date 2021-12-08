# Getting Started

Click this button [![Binder](https://mybinder.org/badge_logo.svg)](${BINDER_URL}) to run this project!

You'll find everything you need in `examples/ena.ipynb`!

# Files in this Project

- TODO

# Making Edits

Changes that you make on binder are temporary. You can download your files from binder, or you can make your own repo that lives on github.

To make your own repo copy of this project that you can edit:

1. Create a [copy of this template](${GENERATE_URL}). It will need to be a public repo, but you can name it whatever you want
2. Create a [github personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). It will need the `repo` and `workflow` scopes
3. Open your project on binder (the binder button in your README will automatically update to link to your project!)
4. Make edits to your project on binder like you normally would
5. Open a terminal on binder and run:
```sh
git pull
git add --all
git commit -m "some friendly message here"
git push
```
When prompted to enter your password, enter your personal access token instead.

# Model Card

Last updated: ${DATE_STRING}

Inspired by [Model Cards for Model Reporting (Mitchell et al.)](https://arxiv.org/abs/1810.03993).

## Model Details

TODO: Intro paragraph about the model, the model type, the researchers, the data, the training, and the uses

## Papers

TODO: Link papers about/using the model

## Model Use

TODO: Paragraph about the intended/valid uses of the model

TODO: Paragraph about example *non*-intended/*invalid* uses of the model

## Data

TODO: Exact details on the data, how it was obtained, how it was cleaned, and what population(s) it does and does not represent

## Performance

TODO: Exact details on how the model was trained and evaluated, and the statistical results of those tests

## Limitations

TODO: Reiterate limitations mentioned above and fully elaborate the "so what" of those limitations

## Contact

If you have questions or comments about this model, please contact:

- TODO

# enapy 

<center>
  
![alt text](https://github.com/thiagorfrf1/ENAPY/blob/master/ena.png)

</center>

Epistemic Network Analysis (ENA) <br>

(ENA) é um método para identificar e quantificar conexões entre elementos em dados codificados e representá-los em modelos dinâmicos de rede. Uma característica fundamental da ferramenta ENA é que ela permite que os pesquisadores comparem redes diferentes, visualmente e por meio de estatísticas resumidas que refletem a estrutura ponderada das conexões. A interface também permite que os usuários vejam os dados originais que contribuíram para cada uma das conexões na representação de rede. Assim, a ENA pode ser usada para abordar uma ampla gama de questões de pesquisa qualitativa e quantitativa.

Os pesquisadores usaram a ENA para analisar e visualizar uma ampla gama de fenômenos, incluindo: conexões cognitivas que os alunos fazem enquanto resolvem problemas complexos; interações entre diferentes regiões do cérebro em dados de RMf; coordenação do olhar social; integração de habilidades operatórias durante procedimentos cirúrgicos; e muitos outros.

https://cran.r-project.org/web/packages/rENA/rENA.pdf

# Por que usar a biblioteca?
Uma outra vantagem é que a biblioteca rena original está sendo usada como motor, todas as atualizações e futuras novas funções poderão ser utilizadas com a biblioteca

# Instalando

## Pip:

## pip install enapy

# Usando o enapy
O exemplo continos na pasta example mostam como usar a biblioteca. Todas as bibliotecas do python podem ser usadas para mnipular e arrumar os dados para serem plotados.

Todas as funçoes da biblioteca podem ser chamadas usando a interface rENA, um outro detalhe ,e que os pontos (.) devem ser substituidos por underscore (_).
## Exemplo: 
A função ena.plot() pode ser chamada usando rENA.ena_plot() <br>
A função ena.plot.points() pode ser chamada usando rENA.ena_plot_points().

# Requisitos:
## Python 3.6

rpy2


## R 

data.table

rENA

## Bibliotecas necessárias:
Devem ser instaladas as bibliotecas R rENA e data.table usando os comandos abaixo:
## install.packages("rENA")
## install.packages("data.table")

No python devemos instalar a biblioteca rpy2 usando o seguinte comando:
pip install rpy2

## Exemplos
Exemplos estão disponíveis no arquivo ena.ipynb na pasta “examples”.


# Referências:
 
http://www.epistemicnetwork.org/


https://brieger.esalq.usp.br/CRAN/web/packages/rENA/vignettes/getting-started.html


https://github.com/cran/rENA
