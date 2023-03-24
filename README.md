# Python环境安装(使用Anaconda)

**注意：** **建议先看一遍视频**

## 1-阿里云镜像站安装Anaconda(推荐)

推荐阿里云镜像站安装，毕竟服务器在中国下载速度快

当然也可以选择[Anaconda官网安装](https://www.anaconda.com/products/distribution)

### 2-下载Anaconda

1. 点击进入[阿里云镜像站-anaconda官方文档](https://developer.aliyun.com/mirror/anaconda?spm=a2c6h.13651102.0.0.99681b112QShUg)阿里云官方文档
2. 下载Anaconda[所有系统和所有版本大全](http://mirrors.aliyun.com/anaconda/archive/ )。
3. 里面好多文件不知道下那个?[Anaconda3-2022.10-Windows-x86_64.exe](https://mirrors.aliyun.com/anaconda/archive/Anaconda3-2022.10-Windows-x86_64.exe?spm=a2c6h.25603864.0.0.45d532784JcddP):适合windows64位系统，版本Anaconda3-2022.10

### 3-安装Anaconda

1. 安装Anaconda。**注意:** 需要勾选Add Andconda to my PATH environment variable(自动配置环境变量)
2. 输入`win+r`快捷键进入运行，再输入`cmd`进入终端。输入`conda --version`显示版本号，有输出版本号为成功安装，没有则安装出错(可以是环境变量原因)。`conda info`可查看更多信息

### 4-配置阿里云镜像源

1. 安装成功后输入`conda config --set show_channel_urls yes`生成配置文件
2. 输入`conda info`查看配置文件位置`user config file :`后面的路径就是配置文件位置
3. 在终端输入`notepad.exe + 空格 + 你电脑配置文件路径`。  
4. **示例:** 我电脑就输入这条`notepad.exe C:\Users\lxy\.condarc`
5. 复制下面全部代码，粘贴到刚打开的计事本中(覆盖之前的全部文本)

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

### 5-安装python3.9环境

1. 配置完成可运行后回到终端输入`conda clean -i`后按y确认清除索引缓存。
2. 输入`conda create --name python3.9 python=3.9`创建python3.9环境。
3. 输入`conda activate python3.9`激活python3.9环境。
4. 输入`python --version`查看版本，有输出python3.9则为安装成功。
