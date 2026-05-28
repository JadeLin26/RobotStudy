# AI 设计 + 网上现成资源（档 1 路线）

> 你 **不必** 从零机械设计。推荐：**现成双足 + AI 改头相机 + Blender 只做概念**。

## 你能用 AI 做什么

| 阶段 | AI 能帮 | 你仍要做 |
|------|---------|----------|
| 概念外形 | 文生图、Tripo/Meshy 粗模、Cursor 写 bpy 方块机 | 定 1.6–2m、头=相机读性 |
| 机构示意 | Cursor 生成「升降/横移/旋转」方块装配 | 确认像你要的运镜 |
| 仿真 | Cursor 写 Isaac 脚本、改质量/关节 | 跑 sim、看倒不倒、画面抖不抖 |
| 行走平衡 | 用 **现成 Isaac Lab 模板** | 验收，不自己推公式 |

**AI 不能替代：** 真机线轨选型、第一版就完美平衡（要靠试）。

---

## 最推荐：Isaac Sim 自带人形（免建模先走通）

安装 Isaac Sim 5.1 后，Content 里 **Isaac Sim/Robots**，文档：

- https://docs.isaacsim.omniverse.nvidia.com/5.1.0/assets/usd_assets_robots.html

| 模型 | 身高大致 | 适合你的原因 |
|------|----------|--------------|
| **Unitree H1** | ~1.8 m | 接近 1.6–2m，Lab 资料多 |
| **Unitree G1** | ~1.3 m | 偏矮，可当「矮摄影师」或以后不用 |
| **Fourier GR-1** | 成人尺寸人形 | 备选 |
| **Humanoid28** | 通用人形 | 轻量 proxy |
| Agility Digit | 特殊腿型 | 偏难，后期 |

**档 1 做法：** 先打开 `Unitree H1` 或 `GR1` → 在 **头 link** 挂 camera sensor → 先学走和平衡 → 再换成你的 Blender 外形。

---

## 行走 + 平衡：现成「技能包」（GitHub）

不是 Cursor Skill，是 **Isaac Lab 扩展/仓库**：

| 资源 | 链接 | 用途 |
|------|------|------|
| **unitree_rl_lab** | https://github.com/unitreerobotics/unitree_rl_lab | G1/H1/Go2 行走 RL，官方向 |
| **unitree_sim_isaaclab** | https://github.com/unitreerobotics/unitree_sim_isaaclab | G1/H1-2 全身仿真场景 |
| **unitree_model (HF)** | https://huggingface.co/datasets/unitreerobotics/unitree_model | USD/模型数据集 |
| **IsaacLab_Locomotion_H1** | https://github.com/NirajPudasaini/IsaacLab_Locomotion_H1 | H1 粗糙地形行走教程向 |

你的 **头升降/横移/旋转** 不在这些包里 → 后期在 Isaac 里 **加 3 个关节** 或 Blender 里方块示意再导入。

---

## Blender 建模：AI + 插件（不是必须精通机械）

### A. 概念外形（最快）

- **文生图**（Gemini / Midjourney）：提示词 `1.8m biped robot, head is cinema camera, professional camera operator aesthetic`
- **Tripo / Meshy / Rodin**：图生 3D 粗模 → 导入 Blender 当比例参考（常需重拓扑）

### B. 在 Blender 里用 AI 写脚本（你已有 Cursor）

- 让 AI 写 **bpy**：按 1.8m 总高建方块头身、头=镜头筒
- 参考开源 **3D-Designer-Agent**（多 agent 生成 bpy）：https://github.com/pierreamir123/3D-Designer-Agent

### C. 机器人专用 Blender 插件（导出仿真用）

| 插件 | 链接 | 作用 |
|------|------|------|
| **LinkForge** | https://extensions.blender.org/add-ons/linkforge/ | Blender ↔ URDF/XACRO，带物理检查，可进 Isaac |
| URDF Importer | Isaac 自带 | 反向：URDF → 编辑 |

适合：**你雕外形 + 插件导出 URDF → Isaac 导入**（比手写 XML 现实）。

### D. 研究向 Text-to-CAD（可选，偏实验）

- **Graph-CAD**：https://github.com/EESJGong/Graph-CAD — 文字 → 分解图 → bpy（零件级，不是整机行走）

---

## 和你 Cursor 里已有 Skill 的关系

| 你 workspace 里的 | 用于本项目 |
|-------------------|------------|
| **ai-for-blender-rendering** | 以后 VLM 看渲染/画面稳不稳 |
| **ce-work / 日常 Cursor** | 写 parse_motion_channels、Isaac 脚本 |
| **无专用「机器人建模」skill** | 用本文 + 让 Cursor 按 mechanical-spec 写 bpy |

可以说：「按 docs/mechanical-spec.md 用 bpy 建 1.8m 方块概念机，头=相机，带升降横移旋转示意」。

---

## 推荐执行顺序（AI + 现成资产）

```
1. 装 Isaac Sim 5.1 + Checker
2. 打开 Unitree H1 USD，头 link 挂 camera，跑官方 locomotion 示例（行走平衡）
3. 并行：Blender 或 AI 粗模画「你的」头相机外形（仅概念）
4. Cursor：把头相机机构加成 Isaac 额外关节（prismatic + revolute）
5. 运镜意图 → command_schema.json（你已有 v1.1）
```

---

## 没有现成「完全符合」的单一模型

市面上 **没有** 开箱即用的「1.6–2m + 头相机 + 升降横移旋转 + 摄像师平衡」整机。

合理拆法：

- **身体行走平衡** → 用 H1/G1 + unitree_rl_lab  
- **头机构 + 外形** → Blender 示意 + AI bpy  
- **合流** → Isaac 里组装 USD

这就是档 1，也是专业团队原型阶段的做法。
