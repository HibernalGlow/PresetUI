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
        return textual_create_config_app(module_name="presetui")
    else:
        PRESET_CONFIGS = {
            "默认配置": {
                "description": "基础配置示例",
                "checkbox_options": ["feature1"], # Use opt_id (dest)
                "input_values": {
                    "number": "100", # Use opt_id (dest)
                    "text": "",
                    # "path": "", # Assuming no path arg
                    "choice": "A" # Use opt_id (dest)
                }
            },
        }

        # 直接运行配置界面并获取结果
        result = rich_create_config_app(
            program="presetui.py",
            title="presetui主界面",
            preset_configs=PRESET_CONFIGS,
            rich_mode=True, # Force rich mode for testing
            module_name="presetui" # 使用模块名方式运行
        )

        # 默认使用 rich 界面
        return result

if __name__ == "__main__":
    main()