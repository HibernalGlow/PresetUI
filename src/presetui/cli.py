#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PresetUI 命令行入口
提供全局调用功能
"""

import sys
from rich_preset import create_config_app as rich_create_config_app
from textual_preset import create_config_app as textual_create_config_app

def main():
    """主入口函数，自动选择适当的界面"""
    # 如果命令行指定了参数，可以根据参数选择界面
    if len(sys.argv) > 1 and sys.argv[1] == "--textual":
        return textual_create_config_app()
    else:
        # 默认使用 rich 界面
        return rich_create_config_app()

if __name__ == "__main__":
    main()