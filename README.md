PythonLab em Desenvolvimento.

Data Monitor - Mercado Livre

Este é um projeto de estudo para coleta e análise de dados do e-commerce através de 
API's oficiais e também de bibliotecas Playwright. 
O objetivo é monitorar a variação de preços de produtos selecionados ao longo do tempo.

 Tecnologias utilizadas
- **Python**: Linguagem principal de desenvolvimento.
- **Requests**: Para fazer as requisições à API pública do Mercado Livre.
- **SQLite**: Banco de dados para salvar e persistir os preços coletados.
- **Pandas**: Para tratamento e análise dos dados.

#img05_playwright_profile.png

Estrutura do projeto após a implementação de um perfil persistente do Playwright.
O diretório `.playwright_profile/` e suas subpastas são gerados automaticamente e
armazenam informações de sessão e preferências do navegador, tornando a automação 
mais estável.
Por questões de segurança, o diretório `.playwright_profile/` 
foi adicionado ao `.gitignore`, evitando a exposição de dados locais e
informações de sessão no repositório.


