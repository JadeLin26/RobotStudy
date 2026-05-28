# Learning Log

## 2026-05-28 — Day 1（完成）

### Focus

仓库立项、范围三档确认、学习承诺写下来。

### Done

- [x] GitHub 发布：https://github.com/JadeLin26/RobotStudy
- [x] README / project-charter / todolist.html / 目录骨架
- [x] docs/day1-scope-confirmation.md — MVP / Target / Stretch 书面确认
- [x] Charter v1.1 — 含每周 20–24h 承诺与 scope 护栏
- [x] todolist.html 编码修复（UTF-8）
- [x] 本机探测：Git 2.52 ✓ · Python 3.12.8 ✓（Isaac 阶段目标 3.11）


### 为什么做这个项目（v2 — 创作动机）

**主目标：做一台类似 BD-X 的、我自己设计的表达型机器人，先在电脑里仿真。**

- 不是为求职而做；求职只是可能的副产品。
- 造型、性格、动作库由我定；迪士尼是**参考思路**（分层动画 + 物理身体 + 低维命令），不是抄外形。
- 「做出来」= 仿真里能稳定表演、能录屏给别人看、管线可重复。

详见 [why-isaac.md](./why-isaac.md) 和 [project-charter.md](./project-charter.md)。

### 每周时间承诺

| 项 | 承诺 |
|----|------|
| 每周总时长 | **20–24 小时** |
| 工作日 | 约 3–4 h/天（配合 15:00–24:00 工作节律） |
| 休息日 | 1 天轻量复盘或休息 |
| 硬规则 | 每 **14 天** 必须有一个可见 artifact |

### Blockers

- 无（Day 1 不要求装 Isaac Sim）

### Next — Day 2

- [ ] 确认/安装 VS Code
- [ ] 记录本机 CPU / GPU / RAM 到 docs/environment-notes.md
- [ ] 下载并运行 **Isaac Sim Compatibility Checker**
- [ ] 用 AI 辅助完成第一个 JSON 读取脚本（不必上网课，见 docs/how-to-learn-with-ai.md）

### Notes

- 稳定车道写进 charter，避免追 Isaac 6.0 / Newton
- Day 1 在 todolist 里可勾选：仓库、charter、todolist 三项

---

## Template

`markdown
## YYYY-MM-DD — Day N

**Focus:**

**Done:**
-

**Blockers:**
-

**Next:**
-
`

## 2026-05-28 — 目标更新

**最终目标澄清：** 双足 + 摄像 = **稳定走动的运镜平台**，代替摄像师（仿真先行）。

- BD-X 降为可选审美参考，主线的表情/state machine 后移
- 第一座里程碑改为：负重 + 走几步 + 虚拟相机画面不晃
- 见 `docs/final-goal.md`

