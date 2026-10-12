import subprocess
import os
import sys

def iniciar_canal_pirata():
    # 📡 ENLACE A TU PELÍCULA EN GITHUB RELEASES
    # Reemplazá esta URL por el link real de tu archivo .mp4 en tu Release
    URL_PELICULA_GITHUB = "https://github.com/dsacjake-commits/estr/releases/download/bunker_mutiny/d0nn13d4rk0.mp4"

    # Chupa las credenciales desde las variables de entorno de Zeabur
    rtmp_url = os.getenv("RTMP_URL", "rtmp://kick.com")
    stream_key = os.getenv("STREAM_KEY")
    
    # Texto en caliente que va a aparecer abajo en el letrero de información
    # Podés cambiar este mensaje directo desde el panel de variables de Zeabur si querés
    texto_marquesina = os.getenv("TEXTO_INFO", "TRANSMISION CLANDESTINA BUNKERO90S - SEÑAL PIRATA EN VIVO")

    if not stream_key:
        print("[⚠️ ERROR]: Falta configurar la STREAM_KEY en el panel de Zeabur.")
        sys.exit(1)

    destino_streaming = f"{rtmp_url}/{stream_key}"
    
    # 🔬 BYPASS DE CONTRAINTELIGENCIA MULTIMEDIA (Filtros de FFmpeg):
    # 1. rotate=0.017: Inclina la pantalla un pelito (0.1 radianes aprox) para burlar el detector de DMCA.
    # 2. drawtext: Dibuja un rectángulo negro abajo y le estampa tu letrero de información en caliente.
    filtros_video = (
        f"rotate=0.017:ow=rotw(0.017):oh=roth(0.017),"
        f"drawtext=text='{texto_marquesina}':x=(w-text_w)/2:y=h-40:"
        f"fontcolor=white:fontsize=24:box=1:boxcolor=black@0.7:boxborderw=10"
    )

    comando = [
        'ffmpeg',
        '-re',
        '-stream_loop', '-1',
        '-i', URL_PELICULA_GITHUB,
        '-vf', filtros_video,       # Inyección de filtros por hardware
        '-vcodec', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'ultrafast',     # Bypass de CPU en la nube
        '-b:v', '2000k',
        '-maxrate', '2000k',
        '-bufsize', '4000k',
        '-acodec', 'aac',
        '-b:a', '128k',
        '-f', 'flv',
        destino_streaming
    ]
    
    print("[🚀 TV PIRATA]: Antena encendida con bypass de rotación y letrero activo.")
    subprocess.run(comando)

if __name__ == "__main__":
    iniciar_canal_pirata()
