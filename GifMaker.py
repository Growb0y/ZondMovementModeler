import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

plt.style.use('dark_background')

fig = plt.figure()

ax = plt.axes(xlim=(-50, 50), ylim=(0, 100))
line, = ax.plot(0, 0, 's', lw=2, ms=10, mfc='c', mec='m')


# функция анимации
def animate(i, points_list):

    x = points_list[i][0]
    y = points_list[i][1]

    line.set_data(x, y)
    print(x, ' ', y)
    return line,


font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}
plt.title("Research zond modeling", fontdict=font1, loc='left')
plt.ylabel("Height", fontdict=font2)
plt.xlabel("Ground", fontdict=font2)


def make_gif(points_list, time, H, L):

    print(time)

    print(points_list)

    lim = max(H, L) * 1.2
    ax.set_xlim(-lim, lim)
    ax.set_ylim(0, lim)

    # Вызов анимации
    anim = animation.FuncAnimation(fig, animate, frames=len(points_list), fargs=(points_list,),
                                   interval=time/len(points_list), blit=True)

    # Сохраняем анимацию как gif файл
    anim.save('simulation.gif', writer='imagemagick')

    print('make_gif done')
