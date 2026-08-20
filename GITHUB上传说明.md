# 把代码上传到 GitHub

## 第一次上传

先在 GitHub 网站创建一个空仓库。创建时不要勾选自动生成 README，因为本地已经有 README。

复制仓库的 HTTPS 地址，例如：

```text
https://github.com/你的用户名/python-learning.git
```

然后在当前文件夹打开 PowerShell，依次运行：

```powershell
git add .
git commit -m "完成第一周学习文件"
git branch -M main
git remote add origin https://github.com/你的用户名/python-learning.git
git push -u origin main
```

注意：上面的仓库地址必须换成你自己的地址。

## 以后更新代码

以后每次写完代码，只需要运行：

```powershell
git add .
git commit -m "写清楚这次完成了什么"
git push
```

## 三个命令分别是什么意思

- `git add .`：把本次修改放进待上传清单。
- `git commit`：给本次修改保存一个本地版本。
- `git push`：把本地版本上传到 GitHub。
