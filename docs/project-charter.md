# Project Charter

## 项目名称

**BD-X Inspired Expressive Robot Character Study**  
受 BD-X 启发的角色机器人表达研究

## 一句话定位

> 把角色动画/绑定能力，转成 OpenUSD 资产、Isaac Sim 关节机器人、动画参数化管线，以及小型 Isaac Lab 表达控制研究。

**不是**复刻迪士尼 BD-X 硬件。

## 三档范围（已确认）

| 档位 | 内容 | 完成时间 |
|------|------|----------|
| **MVP** | 原创角色 + Blender rig + USD + Isaac Sim 关节 idle + JSON 状态机 + 30–60s 视频 | ~第 12 月 |
| **Target** | MVP + 动画→参数 exporter + 一个 Isaac Lab 任务（obs/act/reward 有文档）+ 2–3 min demo + 中英双语文档 | **第 18 月（主完成点）** |
| **Stretch** | Target + ROS 2 bridge 或 Jetson 小实验 + 最终 polished release | 第 19–24 月 |

## 三段子管线

| 管线 | 工具 | 产出 |
|------|------|------|
| 视觉创作 | Blender + USD | 角色、姿势、情绪片段 |
| 物理创作 | Isaac Sim 5.1 | 关节、碰撞体、驱动调参 |
| 运行时桥接 | Python + JSON | 低维命令、状态机混合 |

## 稳定技术栈（2026，第一年不升级）

- Blender 4.5 LTS+
- Isaac Sim **5.1 stable**（非 6.0）
- Isaac Lab（对齐 5.1）
- Python **3.11 目标**（当前机子 3.12 可学 Python，装 Isaac 时再对齐 3.11）

## 每周投入承诺

| 项目 | 数值 |
|------|------|
| 目标时长 | **20–24 小时/周**（约 3–4 小时/天 × 6 天） |
| 节奏 | 2天 Python · 2天 Blender/USD · 2天 Isaac · 1天复盘 |
| 可见产出 | **每 14 天**至少一个 artifact（截图/clip/devlog） |

## 不做的事（scope 护栏）

- 第一年不做完整双足行走从零训练
- 不买 Jetson 当 Isaac Sim 主力机（第 18 月后再考虑）
- 不依赖 Newton / Isaac Sim 6.0 作为第一年硬依赖
- 公司 IP（AA-Service 等）不混入本 repo

## 求职叙事（记住这三句）

1. 我来自角色动画/绑定，不是传统 robotics 科班。
2. 我把表达力转成了 **OpenUSD 资产 + 动画参数化管线**。
3. 我在 Isaac Sim 里验证了关节机器人，并用 Isaac Lab 做了一个小型表达控制任务。

## 参考

- [deep-research-report.md](../deep-research-report.md)
- [todolist.html](../todolist.html)
- [day1-scope-confirmation.md](./day1-scope-confirmation.md)

---
*Charter v1.1 — 2026-05-28，Day 1 范围已确认*
