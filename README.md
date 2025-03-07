# nutrispine

## Passo a passo

1. Criar um diretório para o projeto (se não tiver):
   ```
    mkdir meu_projeto
    cd meu_projeto
    ```

2. Criar o ambiente virtual:
   ```
    virtualenv venv
    ```

3. Ativar o ambiente virtual:
   - No Linux use:
     ```
      source venv/bin/activate
      ```
   - No Windows use:
     ```
      venv\Scripts\activate
      ```
4. Instalar as dependências do projeto:
   ```
    pip install -r requirements.txt
    ```
    
5. Aplicar as migrações do banco de dados:
   ```
    python manage.py migrate
   ```
  
6. Iniciar o servidor de desenvolvimento:
      ```
    python manage.py runserver
   ```

Agora pode acessar a url: [http:localhost:](http://127.0.0.1:8000/api/) ou copie: `http://127.0.0.1:8000/api/`
