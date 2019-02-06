from moviepy.editor import *
import moviepy.video.fx.all as vfx

video = VideoFileClip("seu_video_para_gif_animado.mp4").subclip(1, 3)

'''
para vídeo com menos tamanho para compartilhar fácil 
pode variar número de sua preferência ou omitar esse se quiser
'''

video = video.resize(0.4)

'''
pode cortar video se quiser
video_cortado = video.fx(vfx.crop, x1=115, x2=399, y1=0, y2=288) 
'''

'''
achar e savlar largura e altura de vídeo 
para texto que quiser em topo direito de vídeo
'''

w, h = video.size

'''
Esse é apenas exemplo, pode usar seu nome, marca etc 
em vez de www.steadylearner.com
'''

txt_steadylearner = TextClip("www.steadylearner.com", fontsize=16, color='white')
txt_steadylearner = txt_steadylearner.set_position((12, h - 20)).set_duration(video.duration - 0.1)

# Use imagem de sua marca em baixo direto para estilo de YouTube
sua_marca = (ImageClip("sua_marca.png")
          .set_duration(video.duration)
          .resize(height=50) # (opcional), Tamanho de imagem não é adequado para vídeo?
          .margin(right=2, bottom=1, opacity=0) # (opcional), teste para achar melhor resultado
          .set_position(("right","bottom")))

# mistruar componentes de vídeo que a gente fiz até agora
video = CompositeVideoClip([video, sua_marca, txt_steadylearner.crossfadein(1)])

# Para duração de GIF animado menos de 2 segundos 
short_video = video.speedx(final_duration=2)
# Para efeito de vídeo de ida e volta
reverse_video = short_video.fx(vfx.time_mirror)

final = concatenate_videoclips([short_video, reverse_video])
final.to_gif("seu_gif_animado.gif", fps=10) # menos de 10 talvez baixa qualidade de GIF

