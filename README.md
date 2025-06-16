# 🍫 Site Fake "Promoção Cacau Show" – Flask + SQLite + Engenharia Social (de mentirinha)  
**Projeto de Desenvolvimento Web — Técnico em Informática - 3º Ano IFC**  

## 📚 Sobre o Projeto  
Este é um projeto acadêmico que simula um site de promoção falsa inspirado na estética de grandes marcas do varejo, como a Cacau Show. O objetivo pedagógico é explorar conceitos de back-end com Flask, persistência de dados com SQLite, uso de formulários HTML e interação entre front-end e banco de dados.  

O site foi propositalmente desenvolvido com um visual de "golpe virtual", simulando práticas comuns de engenharia social, com foco em UX manipulativa, formulários invasivos e chamadas de ação duvidosas — tudo isso para gerar reflexão sobre segurança da informação, design persuasivo e boas práticas de desenvolvimento web.  

## 🚀 Tecnologias Utilizadas  

| Ferramenta/Tech       | Finalidade                              |
|-----------------------|-----------------------------------------|
| Python 3              | Linguagem principal                    |
| Flask                 | Framework Web                          |
| SQLite (via Pony ORM) | Banco de Dados                         |
| HTML5 + Jinja2        | Templates dinâmicos                    |
| CSS3                  | Estilização                            |
## 🎯 Funcionalidades Principais  

| Página                | Descrição                                                                 |
|-----------------------|---------------------------------------------------------------------------|
| Home                  | Página inicial com uma apresentação atrativa e chamativa (estilo fake promocional). |
| Sobre                 | Explicação sobre o projeto (no contexto da brincadeira).                 |
| Cadastro              | Formulário coletando dados excessivos (exatamente como sites maliciosos fazem). |
| Listagem de Pessoas   | Exibe as "vítimas" já cadastradas (dados armazenados no SQLite).         |
| Promoção Especial     | Nova página criada com design ainda mais duvidoso, usando o mesmo layout base (com ajustes específicos de CSS e conteúdo). |

## 🛠️ Alterações Estruturais no Projeto  
Para que a nova página de **Promoção Especial** funcione corretamente, foram feitas as seguintes modificações nos documentos existentes:  

| Arquivo                        | Alterações                                                                 |
|--------------------------------|----------------------------------------------------------------------------|
| `app.py`                       | Adicionado um novo endpoint (`/promocao`) e sua respectiva função de renderização. |
| `templates/main_template.html` | Atualização do menu de navegação para incluir link para a nova página.    |
| `templates/promocao.html`      | Novo arquivo template criado com conteúdo próprio da promoção.            |
| `static/css/mycss.css`         | Pequenas customizações para dar identidade visual à nova página (sem quebrar o resto do site). |

## 🛠️ Como Rodar o Projeto Localmente  

1. Clone o repositório:  
   ```bash
   git clone https://github.com/seuusuario/seurepositorio.git

2. Instale as dependências:
   ```bash
   pip install flask pony
   
3. Execute o projeto:
   ```bash
   python app.py

4. Acesse no navegador:
   ```bash
   http://localhost:5000

## 🎓 Créditos
Projeto desenvolvido por Clarice Malaquias Vieira e Isabella Mondini, estudantes do curso técnico integrado em informática pelo **Instituto Federal Catarinense (IFC)**.

Inspirado nas piores práticas de UX (de propósito 😈), com foco em:
- Práticas de back-end
- Estruturação de banco de dados
- Integração front-end/back-end
- Reflexão sobre segurança da informação e engenharia social

## 💡 Observações Importantes
- Projeto **100% educativo**. Nenhuma coleta real de dados sensíveis.
- Todo conteúdo e design foram pensados para estimular o olhar crítico sobre golpes digitais.
- Nenhuma afiliação real com a marca **Cacau Show**.

## 🌟 Contato
Se quiser trocar ideias sobre UX, back-end ou até sobre como **NÃO** construir um site de promoção… só chamar!

> "Saber fazer é bom. Saber o que não fazer é melhor ainda."
