# Avaliação 2 – Entrega Atividade

## 👥 Grupo
- Bruno Oliveira  
- João Paulo  
- Samara Cardoso  
- Victor Miguel  

Este repositório demonstra a implementação de uma pipeline de CI/CD robusta e segura para uma aplicação web em Python com FastAPI. O objetivo principal é ir além da simples automação de build e deploy, integrando práticas de segurança em cada etapa do ciclo de vida do desenvolvimento de software (**DevSecOps**).

A filosofia adotada é a de **"Defesa em Profundidade"**, onde múltiplas camadas de verificação de segurança são aplicadas para garantir a integridade, qualidade e resiliência da aplicação.

---

## 🛡️ As Camadas de Segurança da Pipeline

Nossa pipeline é construída como um "portão de segurança" (`security gate`), onde cada Pull Request é submetido a uma série de validações rigorosas antes que o código possa ser mesclado à branch principal.

### 1. Análise Estática de Segurança (SAST) e Qualidade de Código

*Nesta fase, inspecionamos o código-fonte em busca de falhas de segurança e más práticas antes mesmo de executá-lo.*

-   **Detecção de Segredos (Secret Scanning):**
    -   **Ferramenta:** `GitLeaks`
    -   **Objetivo:** Varrer todo o histórico do repositório em busca de segredos e credenciais (chaves de API, senhas, tokens) que possam ter sido commitados acidentalmente. Isso previne o vazamento de informações sensíveis.

-   **Análise de Vulnerabilidades no Código (SAST):**
    -   **Ferramenta:** `GitHub CodeQL`
    -   **Objetivo:** Realizar uma análise profunda do código para identificar padrões de vulnerabilidades conhecidas, como SQL Injection, Cross-Site Scripting (XSS), e outras falhas de lógica que podem ser exploradas por atacantes.

-   **Análise de Estilo e Padrões (Lint):**
    -   **Ferramenta:** `Flake8`
    -   **Objetivo:** Garantir que o código siga as convenções de estilo do Python (PEP 8), prevenindo erros comuns e mantendo a legibilidade e a manutenibilidade do projeto.

### 2. Análise de Composição de Software (SCA)

*Softwares modernos são construídos sobre bibliotecas de terceiros. Esta camada garante que nossas dependências não sejam o nosso elo mais fraco.*

-   **Análise de Dependências Vulneráveis:**
    -   **Ferramenta:** `pip-audit`
    -   **Objetivo:** Escanear todas as bibliotecas listadas no `requirements.txt` e compará-las com um banco de dados de vulnerabilidades conhecidas (CVEs). Se uma dependência estiver comprometida, a pipeline falha, impedindo a introdução da falha.

-   **Automação de Atualizações de Dependência:**
    -   **Ferramenta:** `Dependabot`
    -   **Objetivo:** Monitorar continuamente as dependências do projeto e criar Pull Requests automaticamente para atualizá-las, seja para aplicar um patch de segurança ou para usar uma versão mais recente.

### 3. Testes Unitários

*Garantimos que a lógica de negócio da aplicação funciona como esperado.*

-   **Ferramenta:** `Pytest`
-   **Objetivo:** Executar uma suíte de testes automatizados que validam as funcionalidades centrais da aplicação em um ambiente isolado. Isso garante que novas alterações não quebrem funcionalidades existentes.

### 4. Análise Dinâmica de Segurança (DAST)

*Com a aplicação em execução, simulamos ataques básicos para encontrar vulnerabilidades que só aparecem em tempo de execução.*

-   **Ferramenta:** `OWASP ZAP (Zed Attack Proxy)`
-   **Objetivo:** Iniciar a aplicação FastAPI em um ambiente temporário e usar o ZAP para escanear ativamente por vulnerabilidades comuns em aplicações web, como falhas de configuração de segurança, cabeçalhos HTTP inseguros e outros.

---

## 🚀 Evidências da Pipeline em Ação

Aqui você pode visualizar como a pipeline se comporta em diferentes cenários, atuando como um verdadeiro guardião da qualidade e segurança do código.

### Cenário 1: Pipeline Executando com Sucesso
![cenario1](prints_evidencias/cenario1.png)


### Cenário 2: SAST (CodeQL) Bloqueando um Código Vulnerável
#### Gitleaks
![sast_gitleaks](prints_evidencias/sast_gitleaks.png)

#### CodeQL - Não foi possível realizar pois precisa habilitar uma função de segurança do repo que não está disponivel 
![sast_codeql](prints_evidencias/sast_codeql.png)

![indisponivel](prints_evidencias/indisponivel.png)


### Cenário 3: SCA (pip-audit) Impedindo uma Dependência Insegura
![cenario3](prints_evidencias/cenario3.png)

### Cenário 4: DAST (OWASP ZAP) Encontrando uma Falha em Execução
![cenario4](prints_evidencias/cenario4.png)

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

-   **Linguagem:** Python 3.10+
-   **Framework:** FastAPI
-   **CI/CD:** GitHub Actions
-   **IaC:** Terraform (para provisionamento da infraestrutura no Azure)
-   **Ferramentas de Segurança:**
    -   `GitLeaks`
    -   `GitHub CodeQL`
    -   `pip-audit`
    -   `Dependabot`
    -   `OWASP ZAP`
-   **Testes:** `Pytest`
-   **Linting:** `Flake8`
-   **Cloud:** Azure (via Azure Functions)# avalicacao2_grupo_c
