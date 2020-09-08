# Carlos-el-botsito
![Lenguaje](https://img.shields.io/badge/Python-3.8-yellow?style=plastic&logo=python)
Este es un Bot de Twitch Open Source basado en la utilidad TwitchIO de Python, esta hecha para el canal de Twitch de [@FreddyFalso](https://twitch.tv/freddyfalso).

[![Logo](Logo "Logo")](https://i.pinimg.com/originals/f0/48/9c/f0489ceb101a4bb4f8fd6f6f2c9e2762.jpg "Logo")

## Guía de configuración.

### Hacer cuenta del Bot.

- [x] Crea una cuenta en [Twitch](https://twitch.tv/) para tu bot o usa la que usas para transmitir. por ejemplo puedes llamarla ***CarlosElBotsito***.

- [] [Solicite un código Oauth](https://twitchapps.com/tmi/) . Deberá iniciar sesión y otorgar permisos a la aplicación para generarla por usted.

- [] Registre su aplicación en [TwitchDev](https://dev.twitch.tv/console/apps/create) y solicite una identificación de cliente (para que pueda interactuar con la API de Twitch).

**Nunca publique esa información.**

### Poniendo el bot en marcha.

- [x] Instala Python en tu PC.

- [] instala PipEnv con el comando de consola `pip install pipenv`. 

- [] En la consola navegue hasta el directorio de trabajo.

- [] ejecute el comando `pipenv --python3.8`.

- [] Ejecute el comando `pipenv install twitchio`.

    - A este punto se tuvieron que crear unos archivos llamados `Pipfile` y `Pipfile.lock`.

- [] Crea un archivo ".env" (Solo la extension) copia el siguiente código metelo dentro y rellenalo con la información que obtuvimos antes.

```python
# .env
TMI_TOKEN=oauth:
CLIENT_ID=
BOT_NICK=
BOT_PREFIX=!
CHANNEL=
```

- [] Cuando ya tengas todo en la consola ejecuta el comando `pipenv run python bot.py`.

- [] Listo ya debería de estar funcionando.
