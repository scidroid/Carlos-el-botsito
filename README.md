# Carlos-el-botsito
Este es un Bot de Twitch Open Source basado en la utilidad TwitchIO de Python, esta hecha para el canal de Twitch de [@FreddyFalso](https://twitch.tv/freddyfalso).

## Guía de configuración.

### Hacer cuenta del Bot.

1. Crea una cuenta en [Twitch](https://twitch.tv/) para tu bot o usa la que usas para transmitir. por ejemplo puedes llamarla ***CarlosElBotsito***.

2. [Solicite un código Oauth](https://twitchapps.com/tmi/) . Deberá iniciar sesión y otorgar permisos a la aplicación para generarla por usted.

3. Registre su aplicación en [TwitchDev](https://dev.twitch.tv/console/apps/create) y solicite una identificación de cliente (para que pueda interactuar con la API de Twitch).

**Nunca publique esa información.**

### Poniendo el bot en marcha.

1. Instala Python en tu PC.

2. instala PipEnv con el comando de consola. 

```
pip install pipenv
```
3. En la consola navegue hasta el directorio de trabajo.

4. ejecute el comando

```
pipenv --python (Version actual de python en su PC)
```
5. Ejecute el comando

```
pipenv install twitchio
```
6. Crea un archivo ".env" (Solo la extension) copia el siguiente código metelo dentro y rellenalo con la información que obtuvimos antes.

```
# .env
TMI_TOKEN=oauth:
CLIENT_ID=
BOT_NICK=
BOT_PREFIX=!
CHANNEL=
```

7. Cuando ya tengas todo en la consolo ejecuta el comando 
```
pipenv run python bot.py
```

8. Listo ya deberia de estar funcionando.