<h1 align='center' >github alerts issues slack bot :robot: </h1>


## O que é isso? :mag: 
Um bot simples que envia notificações para o slack sempre que um PR é fechado e existe uma issue relacionada a ele

<br>

## Como funciona :factory_worker: 
- O GitHub envia uma requisição via webhook sempre que ocorre um evento com Pull Request
- O bot verifica se existe uma issue relacionada ao PR mergeado
  - uma issue é considerada relacionada sempre que eu seu corpo houver menção ao PR com o formato #ID_DO_PR (exemplo: #1234) e também contiver o label "ajuste pr"
- Se tiver issue relacionada, envia uma mensagem para o slack cadastrado

<br>

## Configuração :gear:
### Criar o token de acesso do github
Navegue para **Settings** > **Developer Settings** > **Personal access tokens** > **Generate new token**

A permissão `repo` é necessária apenas para acessar os dados dos seus repositórios (nesse caso das issues):
![image](https://user-images.githubusercontent.com/40877357/149664862-d9247ea9-17d3-4f70-8dbc-7b936cd05be7.png)

Salve o token de acesso depois de criar ele.

### Crie um workflow no slack
O workflow é o ponto utilizado para enviar mensagens para o [Slack e aqui tem um tutorial para criar um](https://slack.com/help/articles/360035692513-Guide-to-Workflow-Builder).

As variáveis necessárias são essas:
- `issue_id`: ID da issue
- `user_login`: Username do usuário responsável pelo pull request
- `pr_id`: ID do pull request

Após criar, salve a url do webhook do workflow.

### Deploy the bot
First, create your fork of this project to can perform the deploy.

The our bot is configured to deploy in [Heroku](https://www.heroku.com/). 
Heroku is a cloud platform to deploy your simple projects, they have a free plan that will be enough for us.
You can also choose another cloud platform to do this.

**Create a new app** > **Select the deploy on GitHub** > **Choose your fork of this project**

Greate! If everything is ok, you can see this message:

<div align='center'>
  <img src='https://user-images.githubusercontent.com/40877357/149665992-a61d9617-3c3e-44f4-bbdf-68e3efb011b1.png' alt='success deploy'>
</div>

### Create GitHub webhook
**Your repository to track** > **Settings** > **Webhooks** > **add webhook**

In the `Payload URL`, past the URL of your Heroku project and the endpoint `check_conflicts`. Like this: `https://my-heroku-app.herokuapp.com/check_conflicts`

The `Content type` is `application/json`.

I recommend using a [UUID](https://www.uuidgenerator.net/) in the `Secret`. This will ensure the security of the requests. 
Save this secret to use in virtual environments of the project

In the events, select `Let me select individual events.` and select `Pull requests` in the list of events.

Now just save.

### Setting envs
Finally, the last step is set the virtual environments in the Heroku project.

**Heroku project** > **Settings** > **Reveal Config vars**.

Now set this envs:
- SECRET_ACCESS: secret used in GitHub webhook
- ACCESS_TOKEN: your access token of GitHub
- PROJECT_TO_TRACK: project of the GitHub webhook. Example: `jackson541/github-alerts-slack-bot`
- BRANCH_TO_TRACK: the branch of the project that you want to track. Example: `master`
- SLACK_WEBHOOK_LINK: the URL of the workflow created in Slack
- REDIS_URL: the URL created with the datas of Redis. example: `http://rediscloud:cofe6kWpNnsdlfkçlç3441kj2l@redis-0000.c11.en-east-1-3.ec2.cloud.redislabs.com:1234`

You can stop and have your coffee, everything is set up!

<br>

## Contribute :heavy_plus_sign: 
Contribute is always well received! Feel free to open Pull Requests or Issues. :smile: 



