# Python环境安装(使用Anaconda)

建议先看一遍视频

## 阿里云镜像站安装Anaconda(推荐)

推荐阿里云镜像站安装，毕竟服务器在中国下载速度快

当然也可以选择[Anaconda官网安装](https://www.anaconda.com/products/distribution)

1. 点击进入[阿里云anaconda镜像站](https://developer.aliyun.com/mirror/anaconda?spm=a2c6h.13651102.0.0.99681b112QShUg)
2. 下载Anaconda[所有系统所有版本大全](http://mirrors.aliyun.com/anaconda/archive/ )。
3. 里面好多文件不知道下那个?[Anaconda3-2022.10-Windows-x86_64.exe](https://mirrors.aliyun.com/anaconda/archive/Anaconda3-2022.10-Windows-x86_64.exe?spm=a2c6h.25603864.0.0.45d532784JcddP):适合windows64位系统，版本Anaconda3-2022.10
4. 安装Anaconda。**注意:** 需要勾选Add Andconda to my PATH environment variable(自动配置环境变量)
5. 输入`win+r`快捷键进入运行，再输入`cmd`进入终端。输入`conda --version`显示版本号，有输出版本号为成功安装，没有则安装出错(可以是环境变量原因)。`conda info`可查看更多信息
6. 安装成功后输入`conda config --set show_channel_urls yes`生成配置文件
7. 输入`conda info`查看配置文件位置`user config file :`后面的路径就是配置文件位置
8. 在终端输入`notepad.exe + 空格 + 你电脑配置文件路径`。我电脑就输入这条`notepad.exe C:\Users\lxy\.condarc`
9. 复制下面全部代码，粘贴到刚打开的计事本中(覆盖之前文本)

        config
        channels:
        - defaults
        show_channel_urls: true
        default_channels:
        - http://mirrors.aliyun.com/anaconda/pkgs/main
        - http://mirrors.aliyun.com/anaconda/pkgs/r
        - http://mirrors.aliyun.com/anaconda/pkgs/msys2
        custom_channels:
        conda-forge: http://mirrors.aliyun.com/anaconda/cloud
        msys2: http://mirrors.aliyun.com/anaconda/cloud
        bioconda: http://mirrors.aliyun.com/anaconda/cloud
        menpo: http://mirrors.aliyun.com/anaconda/cloud
        pytorch: http://mirrors.aliyun.com/anaconda/cloud
        simpleitk: http://mirrors.aliyun.com/anaconda/cloud

10. 回到终端输入`conda clean -i`后按y确认
11. 输入`conda create --name python3.9`创建python3.9环境
12. 输入`conda activate python3.9`激活python3.9环境
13. 输入`python --version`查看版本完成
