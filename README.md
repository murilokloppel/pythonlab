PythonLab Sistema de Coleta de Dados

Este ecossistema de dados está sendo projetado para monitoramento inteligente de e-commerce 
com pequeno foco em Mercado Livre e com prévia expansão para outras plataformas como Shopee e Tiktok. 
O sistema utiliza uma abordagem híbrida, combinando integrações oficiais (APIs) com automação
resiliente (crawlers) para garantir a captura contínua de variações de preços, superando 
limitações de acesso convencionais.

 Tecnologias utilizadas
- **Python**: Linguagem principal de desenvolvimento.
- **Requests**: Para fazer as requisições à API pública do Mercado Livre.
- **SQLite**: Banco de dados para salvar e persistir os preços coletados.

Arquitetura do Sistema

A estrutura do projeto, conciste  em garantir desacoplamento, escalabilidade e manutenibilidade:

core/: Camada de infraestrutura e persistência (Single Source of Truth).

crawlers/: Módulos de ingestão via automação de navegação (resiliência).

api_pack/: Camada de integração para consumo de dados estruturados.


