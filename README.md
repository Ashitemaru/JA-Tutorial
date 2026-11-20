# JA-Tutorial

简明日语自学手册：https://ashitemaru.github.io/JA-Tutorial/

## 本地构建

```bash
pip install -r requirements.txt
PYTHONPATH=ext zensical serve      # 预览
PYTHONPATH=ext zensical build      # 输出到 site/
```

- 站点用 [Zensical](https://zensical.org/) 构建，配置仍在 `mkdocs.yml`。
- 注音写法 `[@ 漢字 かな]` 由 `ext/ja_ruby.py` 处理。
- 推送到 master 后 CI 自动构建并发布到 gh-pages；构建前 `scripts/git_dates.py` 会把每页的创建、更新日期写入页面元数据（只在 CI 里改动，不要提交）。
