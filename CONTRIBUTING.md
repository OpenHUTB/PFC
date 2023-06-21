

# 贡献指南

## 贡献步骤
1. 下载相关[开发工具](https://pan.baidu.com/s/1Is2-VR1z-tMYvmdinsVY_g?pwd=hutb) ，先安装`Git-2.40.0-64-bit.exe`，再安装`TortoiseGit-2.14.0.0-64bit.msi`。


## git管理

- [命令管理](https://blog.csdn.net/weixin_45682261/article/details/124003706) ；
- 可视化工具管理：利用可视化工具[TortoiseGit](https://blog.csdn.net/xwnxwn/article/details/108694863) 进行项目管理。


## 代码提交

先进行本地提交（参考可视化工具管理），然后[推送到开源仓库](https://zhuanlan.zhihu.com/p/153381521) 。


### 本地检查`Pull requests`请求
有人发送`Pull requests`时，可以在 GitHub 上合并之前[测试并验证更改](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/checking-out-pull-requests-locally) 。





# 翻译文献

### 开发建议

1. 图片统一放进image_pfc文件夹，并按照原文格式命名，如Fig_5_1；
2. 提交代码到开源仓库时创建分支，可按照章节或姓名命名。

### 参考文献
可以在谷歌学术、百度学术等中获得文献条目（bib item），然后把它们添加到`reference.bib`
中。在文中引用的时候，引用它们的键值（bib key）即可。
注意需要在编译的过程中添加`biber`编译，配置如下图所示。
![alt 属性文本](image_pfc/reference_guide.png)


## 持续集成/持续部署
[实现第一个Github Actions](https://docs.github.com/en/actions/quickstart) 。

参考[链接](https://mrturkmen.com/posts/build-release-latex/) ，通过 github actions 生成和处理 latex。


## 图片翻译步骤

1. 组织页面
![alt 属性文本](image/1_organize_page.png)

2. 提取页面
![alt 属性文本](image/2_extract_page.png)

3. 保存图片的PDF页面
![alt 属性文本](image/3_save.png)

4. 编辑PDF页面
![alt 属性文本](image/4_edit_page.png)

5. 删除当前页面和图片无关的内容
![alt 属性文本](image/5_delete_content.png)

6. 选择图片区域
![alt 属性文本](image/6_select_region.png)

7. 裁剪页面：点击“裁剪页面”，双击空白地方，选中“约束比例”和“删除边距”，然后点“确定”；
![alt 属性文本](image/7_delete_region.png)

8. 编辑并翻译图中文本
![alt 属性文本](image/8_edit_words.png)