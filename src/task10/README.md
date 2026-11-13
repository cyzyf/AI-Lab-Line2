# demo
包含测试文件
# Docker
容器化文件，Docker时会对这个进行扫描以构建容器完成
# main
主文件，用来调用各个板块
# requirements
依赖包，用于写出容器里面要下载准备的环境等安装包
# mdcheck 
## _init_
是识别成python并运行的必备文件
## scanner
找出要测试的md文件
## headscan
扫描标题的版块
## link_checker
扫描无效链接和损毁图片的板块
## reporter
用扫描板块将要写的东西全都合成一个字符串
