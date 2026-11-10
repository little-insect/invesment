# 长坡 · 私人投资工作台

中文投资决策、长期情景、再平衡与年度复盘工具。默认收益、波动率、相关性和危机冲击均为占位假设。10%是长期研究目标，20%是亏损承受约束，不是收益或止损保证。

## 私人在线使用

1. 仓库可见性必须保持 **Private**，不要开启 GitHub Pages。
2. 在仓库选择 **Code → Codespaces**，首次使用创建2核环境；已有环境则选择原环境启动。
3. 启动后工作台会自动运行。在 **Ports** 面板确认 **4173 → Visibility → Private**，点击浏览器图标打开。
4. 预览链接仅在 Codespace 运行时可访问，且需要登录创建它的 GitHub 账号。用完后在 GitHub Codespaces 页面选择 **Stop codespace**。

重新启动同一个 Codespace 后，应用会自动恢复运行。尽量复用同一个环境，避免预览域名变化。

## 保存记录

投资参数与真实复盘只保存在访问网页的浏览器中，不会自动上传到 GitHub 仓库。正式复盘后，请在网站内导出完整JSON备份并妥善保存。更换浏览器、设备或新建 Codespace 时，需要手动导入备份。

## 费用和休眠

Codespaces 的计算和存储会消耗 GitHub 账户额度。首次运行前请检查账户的剩余额度与账单预算，只使用免费额度，不启用超额付费。停止环境会停止计算消耗；保留的环境仍可能消耗存储额度。GitHub 默认空闲30分钟后休眠。

不要为本项目增加付款方式、提高付费预算或把端口改为 Public。

## 文件

- `public/`：网站运行文件。
- `.devcontainer/devcontainer.json`：Codespaces 自动启动与端口配置。
- `scripts/serve.py`：只提供 public 目录，禁止目录浏览与隐藏路径。
- `scripts/start_preview.py`：可重复执行的启动程序。

浏览器登录与访问控制由 GitHub Codespaces 提供；本项目没有保存密码或 GitHub 令牌。
