#!/usr/bin/python
#filename: pca.py
import numpy as np
from time import sleep, gmtime, strftime

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.cm import get_cmap
import matplotlib.patches as patches


#==============================================================================#
#											
#			This programe is the part of PCA MD. It writes the PCA plots in xmgrace formatted .agr file 
#
# 								Author : Bilal Nizami
# 						  	 Rhodes University, 2017
#==============================================================================#

## write plots
def write_plots(file_name, pca, out_dir):
	'function to write pca plots. takes name of the file to write and pca object name'
	my_time = strftime("%Y-%m-%d  %a  %H:%M:%S", gmtime())
	title = '\tcreated by pca.py\t'
	legends12 = '@    title "Projection of PC"\n\
	@    xaxis  label "PC1"\n\
	@    yaxis  label "PC2"\n'
	legends13 = '@    title "Projection of PC"\n\
	@    xaxis  label "PC1"\n\
	@    yaxis  label "PC3"\n'
	legends23 = '@    title "Projection of PC"\n\
	@    xaxis  label "PC2"\n\
	@    yaxis  label "PC3"\n'
	legends123 = '@    title "Projection of PC"\n\
	@    xaxis  label "PC1"\n\
	@    yaxis  label "PC2"\n\
	@    zaxis  label "PC3"\n'
	other='@	TYPE xy\n\
	@    s0 line type 0\n\
	@    s0 line linestyle 1\n\
	@    s0 line linewidth 1.0\n\
	@    s0 line color 1\n\
	@    s0 line pattern 1\n\
	@    s0 baseline type 0\n\
	@    s0 baseline off\n\
	@    s0 dropline off\n\
	@    s0 symbol 1\n\
	@    s0 symbol size 0.250000\n\
	@    s0 symbol color 1\n\
	@    s0 symbol pattern 1\n\
	@    s0 symbol fill color 1\n\
	@    s0 symbol fill pattern 1\n\
	@    s0 symbol linewidth 1.0\n\
	@    s0 symbol linestyle 1\n\
	@    s0 symbol char 25\n\
	@    s0 symbol char font 0\n\
	@    s0 symbol skip 0\n'
	
	fname = ''
	
	#=======================================
	# xmgrace formated plot
	#================================
	# plot 1 and 2 PC
	
	pca1=pca[:,[0,1]]
	fname = out_dir+'/'+file_name+'1_2'+'.agr'
	np.savetxt(fname, pca1)
	pf = open(fname, 'r')
	pf_cont = pf.read()
	pf.close()
	pf = open(fname, 'w')
	pf.write('#'+title+'\ton\t'+my_time+'\n'+legends12+other+'\n'+pf_cont)
	pf.close()
	
	# plot 1 and 3 PC
	pca1=pca[:,[0,2]]
	fname = out_dir+'/'+file_name+'1_3'+'.agr'
	np.savetxt(fname, pca1)
	pf = open(fname, 'r')
	pf_cont = pf.read()
	pf.close()
	pf = open(fname, 'w')
	pf.write('#'+title+'\ton\t'+my_time+'\n'+legends13+other+'\n'+pf_cont)
	pf.close()
	
	# plot 2 and 3 PC
	pca1=pca[:,[1,2]]
	fname = out_dir+'/'+file_name+'2_3'+'.agr'
	np.savetxt(fname, pca1)
	pf = open(fname, 'r')
	pf_cont = pf.read()
	pf.close()
	pf = open(fname, 'w')
	pf.write('#'+title+'\ton\t'+my_time+'\n'+legends23+other+'\n'+pf_cont)
	pf.close()
	
	# plot 1 2 and 3 PC
	pca1=pca[:,[0,1,2]]
	fname = out_dir+'/'+file_name+'1_2_3'+'.agr'
	np.savetxt(fname, pca1)
	pf = open(fname, 'r')
	pf_cont = pf.read()
	pf.close()
	pf = open(fname, 'w')
	pf.write('#'+title+'\ton\t'+my_time+'\n'+legends123+other+'\n'+pf_cont)
	pf.close()

	return;
              
def write_fig(file_name, pca, out_dir, title):
	#========================================
	# coloured png using matplotlib
	#=================================================
     # 设置图像大小
	figsize = (10, 8)  # 可以根据需要调整
	# 设置全局字体大小（可选）
#	plt.rcParams['font.size'] = 12  # 刻度标签字体大小
#	plt.rcParams['axes.labelsize'] = 15  # 轴标签字体大小
#	plt.rcParams['axes.titlesize'] = 22  # 轴标题字体大小
	
	## # plot 1 and 2 PC
	fname = out_dir+'/'+file_name+'1_2'+'.png'
	fig=plt.figure()
	col=range(1,len(pca[:,0])+1) # color map to the number of frames in trajectory 
	plt.scatter(pca[:,0], pca[:,1], marker='.', c=col)
	plt.xlabel('PC1', fontweight='semibold') # fontweight=700
	plt.ylabel('PC2', fontweight='semibold')
	plt.title(title)
	cbar = plt.colorbar()
	cbar.set_label('#Frame')

	fig.savefig(fname, dpi=400)
	
	## # plot 1 and 3 PC
	fname = out_dir+'/'+file_name+'1_3'+'.png'
	fig=plt.figure()
	plt.scatter(pca[:,0], pca[:,2], marker='.', c=col)
     # 添加折线
#	plt.plot(pca[:, 0], pca[:, 2], marker='', linestyle='-', color='k', linewidth=0.5, alpha=0.5)
	plt.xlabel('PC1', fontweight='semibold')
	plt.ylabel('PC3', fontweight='semibold')
	plt.title(title)
	cbar = plt.colorbar()
	cbar.set_label('#Frame')

	fig.savefig(fname, dpi=400)
	
	## # plot 2 and 3 PC
	fname = out_dir+'/'+file_name+'2_3'+'.png'
	fig=plt.figure()
	plt.scatter(pca[:,1], pca[:,2], marker='.', c=col)
     # 添加折线
#	plt.plot(pca[:, 1], pca[:, 2], marker='', linestyle='-', color='k', linewidth=0.5, alpha=0.5)
	plt.xlabel('PC2', fontweight='semibold')
	plt.ylabel('PC3', fontweight='semibold')
	plt.title(title)
	cbar = plt.colorbar()
	cbar.set_label('#Frame')

	fig.savefig(fname, dpi=400)

    ## # plot 1, 2, and 3 PC (3D scatter plot)
	fname = out_dir+'/'+file_name+'1_2_3_3D'+'.png'
	fig=plt.figure()
	ax=fig.add_subplot(111, projection='3d')
	col=range(1,len(pca[:,0])+1)
	col_normalized=(np.array(col)-np.min(col))/(np.max(col)-np.min(col)) # 归一化颜色值

	# 绘制3D散点图
	scatter = ax.scatter(pca[:,0], pca[:,1], pca[:,2], marker='.', s=20, c=col_normalized, cmap='viridis')
	
	# 设置标签和标题
	ax.set_xlabel('PC1', fontweight='semibold')
	ax.set_ylabel('PC2', fontweight='semibold')
	ax.set_zlabel('PC3', fontweight='semibold')
	ax.set_title(title+'\n(Color represents Frame Number)')
	
	# 添加颜色条
	cbar = fig.colorbar(scatter, ax=ax, label='#Frame Normalized', shrink=0.6, pad=0.1) # shrink和pad参数可以调整颜色条的大小和位置
	ax.view_init(elev=20., azim=30)
#	plt.tight_layout()  # 自动调整子图参数

	
	# 保存图形
	fig.savefig(fname, dpi=400)
	plt.close(fig)
	
	# plot 1 and 2 PC with color representing PC3 values  
	fname = out_dir+'/'+file_name+'1_2_color_by_PC3'+'.png'
	fig=plt.figure()
	
	# 归一化PC3值以便更好地应用颜色映射
	pc3_normalized = (pca[:,2] - np.min(pca[:,2]))/(np.max(pca[:,2])-np.min(pca[:,2]))
	
	# 使用颜色映射来表示PC3的值
	cmap = get_cmap('viridis') # 你可以选择任何你喜欢的颜色映射
	scatter = plt.scatter(pca[:,0], pca[:,1], marker='.', c=pc3_normalized, cmap=cmap)
	
	plt.xlabel('PC1')
	plt.ylabel('PC2')
	plt.title(title+'\n(Color represents PC3 values)')
	
	# 添加颜色条以显示PC3值的范围
	cbar=plt.colorbar(scatter, label='PC3 normalized value')
	
	fig.savefig(fname)
	plt.close(fig)

	# 3D散点图并附加2D投影
	fname = out_dir + '/' + file_name + '1_2_3_3D_with_2D' + '.png'
	fig = plt.figure(figsize=figsize)
	ax = fig.add_subplot(111, projection='3d')
	
	# 绘制3D散点图
	scatter_3d = ax.scatter(pca[:, 0], pca[:, 1], pca[:, 2], marker='.', c=range(len(pca)), cmap='viridis')
	
	# 设置3D图的标签和标题
	ax.set_xlabel('PC1')
	ax.set_ylabel('PC2')
	ax.set_zlabel('PC3')
	ax.set_title(title + '\n(Color represents Frame Number)')
	
	# 添加颜色条
	cbar = fig.colorbar(scatter_3d, ax=ax, label='#Frame')
	
	# 绘制2D投影（这里以边框形式绘制，但您可以根据需要调整样式）
	# 获取PC1和PC2的最小值和最大值，用于设置投影的边框
	xmin, xmax = np.min(pca[:, 0]), np.max(pca[:, 0])
	ymin, ymax = np.min(pca[:, 1]), np.max(pca[:, 1])
	
	# 创建一个矩形补丁来表示2D投影的边框（这里为了示例，我们设置了一个小的偏移量来避免与3D点重叠）
	# 实际上，您可能不需要这个偏移量，或者可以根据需要调整它
	offset_z = -0.1  # 在Z轴上的小偏移量，以避免与3D点重叠（这里设置为负值是因为我们的PC3值通常是正的）
	rect = patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, linewidth=1, edgecolor='r', facecolor='none', zorder=0)
	
	# 将矩形补丁添加到3D图中（注意：这里我们手动设置了z坐标，但这种方法可能不是最佳实践，因为Matplotlib的3D图对2D图形的支持有限）
	# 一种更好的方法可能是使用ax.plot或ax.scatter来绘制投影的边框点
	# 但为了简单起见，这里我们使用了一个矩形补丁作为示例
	# 注意：下面的代码可能不会按预期工作，因为Matplotlib的3D图不支持直接添加2D补丁
	# 如果您遇到问题，可以尝试使用ax.plot来手动绘制投影的边框
	# 例如：ax.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], [offset_z, offset_z, offset_z, offset_z, offset_z], 'r-')
	
	# 由于上面的方法可能不起作用，我们改用ax.plot来绘制投影的边框
	ax.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], [offset_z, offset_z, offset_z, offset_z, offset_z], 'r-', zorder=0)
	
	# 调整视图角度，以便更好地查看3D图和投影
	ax.view_init(elev=20., azim=30)
	
	# 保存图形
	fig.savefig(fname, dpi=400)
	plt.close(fig)
# 注意：在实际运行此函数之前，请确保pca数组已经正确定义，并且包含了足够的数据点。
# 此外，还需要确保out_dir目录存在，或者添加代码来创建它。
# 这里的pca应该是一个二维数组，其中每一行代表一个数据点的PC1、PC2和PC3值。

	# 绘制1, 2, 和3 PC (3D散点图) 并附加2D投影
	fname = out_dir + '/' + file_name + '1_2_3_3D_with_2D_projection' + '.png'
	fig = plt.figure(figsize=figsize)
	ax = fig.add_subplot(111, projection='3d')
	
	# 绘制3D散点图
	scatter_3d = ax.scatter(pca[:, 0], pca[:, 1], pca[:, 2], marker='.', c=range(len(pca)), cmap='viridis')
	
	# 设置3D图的标签和标题
	ax.set_xlabel('PC1')
	ax.set_ylabel('PC2')
	ax.set_zlabel('PC3')
	ax.set_title(title + '\n(Color represents Frame Number)')
	
	# 添加颜色条
	cbar = fig.colorbar(scatter_3d, ax=ax, label='#Frame')
	
	# 绘制2D投影（在XY平面上，即z=0处）  # 使用空心圆表示2D投影
	scatter_2d = ax.scatter(pca[:, 0], pca[:, 1], -330, marker='.', facecolors='none', edgecolors='r', s=10, zorder=0)
	#scatter_2d = ax.scatter(pca[:, 0], pca[:, 1], -330, marker='.', c=range(len(pca)), s=50, zorder=-300)
	
	# 注意：上面的scatter_2d实际上是在z=0处绘制的点，但它们看起来可能不像传统的2D投影。
	# 如果您想要更明确的2D投影效果（比如只显示边框），您可以使用ax.plot来绘制边框。
	# 但为了简单起见，这里我们仅使用空心圆来表示投影点。
	
	# 如果您想要绘制一个明确的边框来表示2D投影的范围，可以使用以下代码：
	#xmin, xmax = np.min(pca[:, 0]), np.max(pca[:, 0])
	#ymin, ymax = np.min(pca[:, 1]), np.max(pca[:, 1])
	#ax.plot([xmin, xmax, xmax, xmin, xmin], [ymin, ymin, ymax, ymax, ymin], [0, 0, 0, 0, 0], 'r-', zorder=0, linewidth=1)
	
	# 调整视图角度，以便更好地查看3D图和投影  ax.view_init(elev=20., azim=30)
	ax.view_init(elev=15., azim=30)
	
	# 保存图形
	fig.savefig(fname, dpi=400)
	plt.close(fig)
	
	return;

## write PCs 
def write_pcs(file_name, pca, out_dir):
	'write PCs and explained_variance_ratio_. takes name of the file to write and pca object name'
	fname = ''
	fname = out_dir+'/'+file_name+'.agr'
	#print type(pca)
	e_ratio = pca.explained_variance_ratio_
	e_ratio = e_ratio*100   # to make it percent
	
	np.savetxt(fname, e_ratio)
	ef = open(fname, 'r')
	ef_cont = ef.read()
	ef.close()
	title = '\tcreated by pca.py\t'
	my_time = strftime("%Y-%m-%d  %a  %H:%M:%S", gmtime())
	legends = '@    title "explained_variance of PCs"\n\
	@    xaxis  label "PCs"\n\
	@    yaxis  label "% Variance"\n\
	@	TYPE xy\n\
	@    s0 symbol 1\n\
	@    s0 symbol size 0.250000\n\
	@    s0 symbol color 1\n\
	@    s0 symbol pattern 1\n\
	@    s0 symbol fill color 1\n\
	@    s0 symbol fill pattern 1\n\
	@    s0 symbol linewidth 1.0\n\
	@    s0 symbol linestyle 1\n\
	@    s0 symbol char 25\n\
	@	s0 symbol fill color 2\n\
	@	s0 symbol color 2\n\
	@    s0 symbol char font 0\n\
	@    s0 symbol skip 0\n'
	
	ef = open(fname, 'w')
	ef.write('#'+title+'\ton\t'+my_time+'\n'+legends+'\n'+ef_cont)
	ef.close()
	return;
	
