from pathlib import Path
p = Path("todolist.html")
t = p.read_text(encoding="utf-8-sig")
t = t.replace(
    "\u53d7 BD-X \u542f\u53d1\u7684\u89d2\u8272\u673a\u5668\u4eba\u8868\u8fbe\u7814\u7a76 \u00b7 24 \u4e2a\u6708\u8def\u7ebf\u56fe \u00b7 \u6bcf\u5468 20\u201324 \u5c0f\u65f6",
    "\u505a\u81ea\u5df1\u7684 BD-X \u5f0f\u673a\u5668\u4eba \u00b7 AI \u8f85\u52a9 \u00b7 \u4ee5\u5f55\u5c4f\u4ea7\u51fa\u4e3a\u51c6",
)
old1 = "\u5f00\u59cb Coursera\u300cProgramming for Everybody\u300d"
if old1 in t:
    t = t.replace(
        "\u5f00\u59cb Coursera\u300cProgramming for Everybody\u300d<small>\u53d8\u91cf\u3001\u5faa\u73af\u3001\u51fd\u6570\u3001\u57fa\u7840 I/O</small>",
        "\u7528 AI \u5199\u7b2c\u4e00\u4e2a Python \u811a\u672c<small>\u80fd\u8bfb JSON \u5373\u53ef\uff0c\u4e0d\u5fc5\u4e0a\u7f51\u8bfe</small>",
    )
p.write_text(t, encoding="utf-8-sig", newline="\n")
print("replacements done", "Coursera" in t)
