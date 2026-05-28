from pathlib import Path
p = Path("todolist.html")
t = p.read_text(encoding="utf-8-sig")
if "panel-ai" not in t:
    t = t.replace(
        '<button data-tab="risks">\u98ce\u9669\u5907\u5fd8</button>',
        '<button data-tab="ai">AI \u600e\u4e48\u5b66</button>\n    <button data-tab="risks">\u98ce\u9669\u5907\u5fd8</button>',
    )
    ins = """
    <section class=\"panel\" id=\"panel-ai\">
      <p class=\"phase-title\">\u6709 AI \u65f6 \u2014 \u5b66\u4ec0\u4e48 / \u4e0d\u5b66\u4ec0\u4e48</p>
      <div class=\"task-group\">
        <ul class=\"tasks\" style=\"list-style:none\">
          <li style=\"padding:0.75rem 1rem;border-bottom:1px solid var(--border)\"><strong>\u4e0d\u5fc5\u7cfb\u7edf\u5b66</strong> \u2014 Coursera\u3001Modern Robotics\u3001\u80cc API</li>
          <li style=\"padding:0.75rem 1rem;border-bottom:1px solid var(--border)\"><strong>\u61c2\u539f\u7406\u5373\u53ef</strong> \u2014 JSON\u3001\u72b6\u6001\u673a\u3001\u5173\u8282/\u8d28\u91cf/\u阻尼</li>
          <li style=\"padding:0.75rem 1rem;border-bottom:1px solid var(--border)\"><strong>\u5fc5\u987b\u4eb2\u624b</strong> \u2014 Blender \u9020\u578b\u7ed1\u9aa8\u3001\u60c5\u7eea\u8868\u6f14\u3001\u4eff\u771f\u5f55\u5c4f\u9a8c\u6536</li>
          <li style=\"padding:0.75rem 1rem\"><strong>\u6d41\u7a0b</strong> \u2014 \u4f60\u5b9a\u76ee\u6807 \u2192 AI \u5199\u4ee3\u7801 \u2192 \u4f60\u8dd1\u901a\u9a8c\u6536</li>
        </ul>
      </div>
      <p class=\"phase-title\">docs/how-to-learn-with-ai.md</p>
    </section>

    <section class=\"panel\" id=\"panel-risks\">"""
    t = t.replace('<section class="panel" id="panel-risks">', ins, 1)
t = t.replace(
    "Git / VS Code / Python + Compatibility Checker + GitHub repo<small>README, learning-log, environment notes</small>",
    "Git / VS Code / Python + Checker<small>Python \u7528\u5230\u54ea\u5b66\u5230\u54ea</small>",
)
t = t.replace(
    "3 \u4e2a\u5c0f\u811a\u672c\uff1a\u91cd\u547d\u540d\u6587\u4ef6\u3001\u8bfb JSON\u3001\u6253\u5370 motion channels<small></small>",
    "motion JSON \u8bfb\u53d6\u8dd1\u901a\uff08AI \u5199\u521d\u7248\uff0c\u4f60\u9a8c\u6536\uff09<small></small>",
)
t = t.replace(
    "motion_channels.json schema v1 + parser<small></small>",
    "schema v1 + parser \u80fd\u8dd1<small>\u61c2\u5b57\u6bb5\u5373\u53ef</small>",
)
p.write_text(t, encoding="utf-8-sig", newline="\n")
print("panel-ai" in t)
