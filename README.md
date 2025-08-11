exTHmUI 黄页数据
=====
部分数据来源于 https://github.com/metowolf/vCards/
其他信息，请参阅[vCards README](README_vCard.md)

## 项目说明
 这个项目来自于`exTHmUI/YellowPage_Data`，因为原服务已经不可用，说明和教程请访问 [https://exypd.nxdyy.cn](https://exypd.nxdyy.cn)
 
## 环境依赖
 1. `Node.js LTS v16+`
 2. `Python 3.8+`

## Notes
  - `convert_data.py`用于从源vCards项目文件格式化`yaml`文件为json compatibility文件。
  - 支持原vCards项目构建`.vcf`文件，您需要安装`Node.js LTS v16+`后在项目中执行`npm run gulp buildVcard`。
  - `make.py`会将`yellowpage_data`目录下的所有yaml文件转换为json并且合并到`yellowpage_data.json`

## 请求收录

 1. 打开 https://github.com/exTHmUI/YellowPage_data/issues/new/choose 页面，选择「黄页数据新增请求」
 2. 完整填写相关信息
 3. 提交 `issue`，等待处理

## 参与维护

 1. 在 `/data/类别/` 里添加 `yaml` 与 `png` 文件
 2. 提交 `pull requests`，等待合并

## 图标设计

 - 采用 `PNG` 编码
 - 画布大小 `width：200px；height：200px`
 - logo 居中放置
   - 圆形尺寸 140w140h
   - 正矩形尺寸 120w120h
   - 长矩形尺寸 160w80h
   - 无 svg 需要使用 Inkscape 改绘转换
   - 特殊情况特殊处理
 - 图像大小压缩在 `20 kB` 内

![Design](https://user-images.githubusercontent.com/2666735/60966995-224fae00-a34c-11e9-970c-ea5fa15186c6.png)

## 致谢
 - [vCards](https://github.com/metowolf/vCards/)提供数据
