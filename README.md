# Reviewer Response DOCX Skill

[![Release](https://img.shields.io/github/v/release/wzgytuA888/reviewer-response-docx-skill)](https://github.com/wzgytuA888/reviewer-response-docx-skill/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

一个用于科研论文返修和逐点回复审稿意见的 Codex Skill。它可以根据审稿意见、论文、补充材料、图表、数据与既往回复格式，生成内容一致、修改位置明确且便于核查的 Word 返修材料。

## 核心原则

- 保留完整审稿意见，并逐条建立意见、证据、修改动作、状态和位置之间的对应关系。
- 将审稿意见作为识别论文问题和确定修改方向的依据，而不是机械照搬审稿人的措辞、问题顺序或论证方式。
- 综合论文自身研究逻辑、已有证据和经过核验的文献，从读者角度修改论点、方法、结果解释、局限性和段落结构。
- 不虚构文献、分析结果、实验、图表变化、页码或修改位置。
- 未完成事项使用明确的待处理状态，不在缺乏可核查证据时声称已经完成。

## 回复文件格式

默认的逐点回复格式包括：

1. 蓝色审稿意见原文；
2. 黑色 `Response` 和有证据支持的直接回复；
3. 红色加粗 `Revision`；
4. 加粗的章节、页码和段落位置；
5. 红色斜体的论文修订原文。

详细排版规范见 [Word formatting rules](reviewer-response-docx/references/word-format.md)。

## 本地数据补充分析

当审稿意见涉及重新计算、稳健性检验、统计更新、图表重绘或其他补充分析时，Skill 会进入本地数据处理流程。如果当前材料没有明确路径，它会先向作者询问以下内容：

- 原始数据和处理后数据的位置；
- 分析脚本、Notebook 或命令文件的位置；
- 数据字典、变量定义和编码说明；
- 当前表格、图件源数据与结果输出；
- Python、R、Stata、MATLAB、GIS 等运行环境及特殊依赖。

收到路径后，先以只读方式检查材料并保留原文件，随后复现论文原始结果、开展补充分析，并核对代码输出、表格、图件、论文、补充材料和回复信中的数值一致性。无法核查的分析不会被标记为已完成。

查看 [完整工作流图](reviewer-response-docx/references/workflow.md)。

## 安装

将仓库中的 `reviewer-response-docx` 文件夹复制到 Codex Skills 目录：

```text
~/.codex/skills/reviewer-response-docx
```

也可以下载 [最新正式版本](https://github.com/wzgytuA888/reviewer-response-docx-skill/releases/latest) 后再复制该文件夹。

## 使用示例

```text
Use $reviewer-response-docx to process these reviewer comments,
revise the supplied manuscript, and prepare the Word response package.
```

中文任务示例：

```text
使用 $reviewer-response-docx 处理这些审稿意见，结合论文全部材料和可靠文献修改论文，
按照指定 Word 格式撰写逐点回复，并列出每项修改的准确位置。
```

## 仓库内容

| 路径 | 内容 |
|---|---|
| [`SKILL.md`](reviewer-response-docx/SKILL.md) | Skill 的核心工作规则 |
| [`references/workflow.md`](reviewer-response-docx/references/workflow.md) | 完整返修工作流图 |
| [`references/word-format.md`](reviewer-response-docx/references/word-format.md) | Word 回复文件排版规范 |
| [`assets/response-template.docx`](reviewer-response-docx/assets/response-template.docx) | 回复信模板 |
| [`scripts/validate_response_docx.py`](reviewer-response-docx/scripts/validate_response_docx.py) | 回复文件检查工具 |
| [`scripts/compare_docx_packages.py`](reviewer-response-docx/scripts/compare_docx_packages.py) | 清洁版、标记版和修订版一致性检查工具 |

仓库不包含任何论文、审稿报告、作者身份信息或未公开研究数据。

## 版本与许可

- 当前正式版本：[v1.0.0](https://github.com/wzgytuA888/reviewer-response-docx-skill/releases/tag/v1.0.0)
- 许可协议：[MIT License](LICENSE)
