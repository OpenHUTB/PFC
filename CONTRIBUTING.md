

# 贡献指南

## 贡献步骤
1. 下载相关[开发工具](https://pan.baidu.com/s/1Is2-VR1z-tMYvmdinsVY_g?pwd=hutb) ，先安装`Git-2.40.0-64-bit.exe`，再安装`TortoiseGit-2.14.0.0-64bit.msi`。


## git管理

- [命令管理](https://blog.csdn.net/weixin_45682261/article/details/124003706) ；
- 可视化工具管理：利用可视化工具[TortoiseGit](https://blog.csdn.net/xwnxwn/article/details/108694863) 进行项目管理。


### 递归克隆
```shell
git clone --recursive https://github.com/OpenHUTB/utils.git
```

### 同步子模块
```
git submodule update --remote
```
 


## 代码提交

先进行本地提交（参考可视化工具管理），然后[提交Pull Request](https://zhuanlan.zhihu.com/p/153381521) 推送到开源仓库。


### 本地检查`Pull requests`请求
有人发送`Pull requests`时，可以在 GitHub 上合并之前[测试并验证更改](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/checking-out-pull-requests-locally) 。


# 问题
## 国内访问github可能较慢
这里提供一个科学上网的[链接](https://a.kkkcloud.men/#/login) 。

## 向github上push的时候报403错误
打开`.git/config`，比如：
```
url = https://github.com/OpenHUTB/bazaar.git
```
将你用户名复制粘贴到github前面再加个@，变成：
```
url = https://OpenHUTB@github.com/OpenHUTB/bazaar.git
```
然后就可以进行授权并继续push。



