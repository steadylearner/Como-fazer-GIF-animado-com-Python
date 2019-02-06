# nome de documento pode sr seu_gif_animado.py
from moviepy.editor import *
import moviepy.video.fx.all as vfx

video = VideoFileClip("seu_video_para_gif_animado.mp4").subclip(1, 3)
video = video.resize(0.4) # 1, (1)
w, h = video.size # 2.

txt_steadylearner = TextClip("www.steadylearner.com", fontsize=16, color='white') # 3.
txt_steadylearner = txt_steadylearner.set_position((12, h - 20)).set_duration(video.duration - 0.1)

sua_marca = (ImageClip("sua_marca.png") # 4.
          .set_duration(video.duration)
          .resize(height=50) # (2).
          .margin(right=2, bottom=1, opacity=0) # (3)
          .set_position(("right","bottom")))

video = CompositeVideoClip([video, sua_marca, txt_steadylearner.crossfadein(1)]) # 5.

short_video = video.speedx(final_duration=2) # (4)
reverse_video = short_video.fx(vfx.time_mirror) # (5)

final = concatenate_videoclips([short_video, reverse_video])
final.to_gif("seu_gif_animado.gif", fps=10) # * menos de 10 talvez baixa qualidade de GIF

## Processo Principal ##

# 1. para vídeo com menos tamanho para compartilhar fácil, pode variar número e omitar também
# 2. achar e savlar largura e altura de víPdeo para texto que quiser em topo direito de vídeo
# 3. Esse é apenas exemplo, pode usar seu nome, marca etc em vez de www.steadylearner.com
# 4. Use imagem de sua marca em baixo direto para estilo de YouTube
# 5. Mistruar componentes de vídeo que a gente fiz até agora

## Opcional ##

# (1) pode cortar video se quiser video_cortado = video.fx(vfx.crop, x1=115, x2=399, y1=0, y2=288)
# (2) Tamanho de imagem não é adequado para vídeo?
# (3) Teste para achar melhor resultado
# (4) Para duração de GIF animado menos de 2 segundos
# (5) Para efeito de vídeo de ida e volta

