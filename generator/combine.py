#!/usr/bin/env python3
"""
海龟汤动态组合生成器
根据难度和风格，随机组合元素生成题目
"""

import json
import random
from pathlib import Path

# 加载元素库
def load_elements():
    base_path = Path(__file__).parent.parent / "database" / "elements"
    
    with open(base_path / "scenes.json", encoding="utf-8") as f:
        scenes = json.load(f)
    
    with open(base_path / "characters.json", encoding="utf-8") as f:
        characters = json.load(f)
    
    with open(base_path / "objects.json", encoding="utf-8") as f:
        objects = json.load(f)
    
    with open(base_path / "actions.json", encoding="utf-8") as f:
        actions = json.load(f)
    
    with open(base_path / "endings.json", encoding="utf-8") as f:
        endings = json.load(f)
    
    return scenes, characters, objects, actions, endings

def load_templates():
    base_path = Path(__file__).parent.parent / "database" / "templates"
    with open(base_path / "basic_templates.json", encoding="utf-8") as f:
        return json.load(f)

def filter_by_style(templates, style):
    """根据风格筛选模板"""
    if style == "随机":
        return templates
    
    style_mapping = {
        "本格清汤": "本格清汤",
        "本格红汤": "本格红汤",
        "变格清汤": "变格清汤",
        "变格红汤": "变格红汤",
        "重口黑汤": "重口黑汤",
        "整活抽象汤": "整活抽象汤"
    }
    
    return [t for t in templates if t["style"] == style_mapping.get(style, style)]

def filter_by_difficulty(templates, difficulty):
    """根据难度筛选模板"""
    if difficulty == "随机":
        return templates
    return [t for t in templates if t["difficulty"] == difficulty]

def generate_puzzle(style="随机", difficulty="随机"):
    """
    生成一道海龟汤题目
    
    Args:
        style: 风格 (本格清汤/本格红汤/变格清汤/变格红汤/重口黑汤/整活抽象汤/随机)
        difficulty: 难度 (简单/中等/困难/随机)
    
    Returns:
        dict: 包含情境、答案、关键词的题目信息
    """
    templates = load_templates()
    
    # 筛选
    templates = filter_by_style(templates, style)
    templates = filter_by_difficulty(templates, difficulty)
    
    if not templates:
        # 如果没有匹配的，随机选一个
        templates = load_templates()
    
    # 随机选择一个模板
    puzzle = random.choice(templates)
    
    return puzzle

def main():
    # 测试生成
    puzzle = generate_puzzle()
    print("=" * 50)
    print(f"风格: {puzzle['style']}")
    print(f"难度: {puzzle['difficulty']}")
    print("=" * 50)
    print(f"\n【情境】\n{puzzle['example']}")
    print(f"\n【答案】\n{puzzle['answer']}")
    print(f"\n【关键词】\n{', '.join(puzzle['keywords'])}")

if __name__ == "__main__":
    main()
