# 长坡 · 40年投资工作台

中文投资决策、长期情景、再平衡与年度复盘工具。默认收益、波动率、相关性和危机冲击均为占位假设。10%是长期研究目标，20%是亏损承受约束，不是收益或止损保证。

## 正式在线访问

GitHub Pages：<https://little-insect.github.io/invesment/>

网站和源码公开，无需启动 Codespaces。网页只发布 public/ 目录；Python 启动脚本不参与正式网站运行。

## 记录与迁移

投资参数、真实收益、年度复盘、快照与日志保存在当前浏览器，不会自动上传到 GitHub，也不会与其他访客共享。正式复盘后，请在页面导出完整JSON备份并妥善保存。

从原 Codespaces 预览网址迁移时，请先在原网址导出备份，再在正式网址导入。不同域名、浏览器或设备之间不会自动同步。

## 更新网站

修改 main 分支的 public/ 内容后，GitHub Actions 会自动部署到同一网址。发布流程位于 .github/workflows/pages.yml。

## 可选的 Codespaces 开发预览

Codespaces 仅用于后续开发或私人测试，不是正式网站访问的前置步骤。使用后停止环境可节省免费计算额度；保留的环境仍可能消耗存储额度。

- public/：网站运行文件。
- .devcontainer/devcontainer.json：可选开发预览环境。
- scripts/serve.py、scripts/start_preview.py：可选开发启动程序。

本项目不保存密码、GitHub令牌，也不执行证券交易。
