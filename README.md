# 魏廷坤 · 个人作品集

`site/` 是已构建好的静态网站，包含所有图片、动效和五部视频。每个文件均低于 GitHub 的 100 MiB 单文件限制。大型 ZIP/TAR.GZ 是本地交付包，不应提交到此仓库。

## 使用 Render 发布

在 Render 连接此 GitHub 仓库后，创建 **Static Site**。若用 Blueprint，仓库根目录的 `render.yaml` 已配置好发布目录；若手动设置，Build Command 填 `echo ready`，Publish Directory 填 `site`。发布成功后，会获得一个 `onrender.com` 地址。

网站内容在本机 `portfolio-react/` 中继续编辑。更新时先在那里重新构建，再将新 `dist/` 文件同步到本仓库 `site/`，提交并推送；Render 会自动重新部署。

新网址须在中国内地手机的移动网络和 Wi-Fi 上实际测试，包括首页、头像和五部视频。任何境外托管的默认域名都不能只凭部署成功就保证在各地稳定访问。

