#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PresetUI 演示测试脚本
用于展示和测试不同界面模式及功能
"""

import argparse
import os
import sys
from pathlib import Path


def setup_demo_parser():
    """创建演示用的参数解析器"""
    parser = argparse.ArgumentParser(description='PresetUI 演示测试程序')
    
    # 添加一些功能标志
    parser.add_argument('--verbose', '-v', action='store_true', help='显示详细输出')
    parser.add_argument('--quiet', '-q', action='store_true', help='静默模式')
    parser.add_argument('--force', '-f', action='store_true', help='强制执行')
    
    # 添加一些带值的参数
    parser.add_argument('--count', '-c', type=int, default=10, help='重复次数')
    parser.add_argument('--output', '-o', type=str, help='输出文件路径')
    parser.add_argument('--level', '-l', type=int, choices=[1, 2, 3], default=1, help='处理级别')
    parser.add_argument('--mode', '-m', choices=['fast', 'normal', 'safe'], default='normal', help='运行模式')
    
    return parser


def process_args(args):
    """处理解析后的参数"""
    print("\n===== 演示: 收到的参数 =====")
    for arg, value in vars(args).items():
        print(f"{arg}: {value}")


def show_textual_ui():
    """显示Textual界面演示"""
    try:
        from textual_preset import create_config_app
        
        parser = setup_demo_parser()
        preset_configs = {
            "默认配置": {
                "description": "基础演示配置",
                "checkbox_options": ["verbose"],
                "input_values": {
                    "count": "10",
                    "output": "output.txt",
                    "level": "1",
                    "mode": "normal"
                }
            },
            "高级配置": {
                "description": "详细模式配置示例",
                "checkbox_options": ["verbose", "force"],
                "input_values": {
                    "count": "50",
                    "output": "advanced_output.log",
                    "level": "3",
                    "mode": "safe"
                }
            }
        }
        
        # 获取当前脚本路径
        current_script = sys.argv[0]
        
        app = create_config_app(
            program=current_script,
            title="Textual 界面演示",
            parser=parser,
            preset_configs=preset_configs,
            on_run=lambda params: process_received_params(params, parser)
        )
        
        if app:
            app.run()
    
    except ImportError as e:
        print(f"无法加载 Textual 界面: {e}")


def show_rich_ui():
    """显示Rich界面演示"""
    try:
        from rich_preset import create_config_app
        
        parser = setup_demo_parser()
        preset_configs = {
            "默认配置": {
                "description": "基础演示配置",
                "checkbox_options": ["verbose"],
                "input_values": {
                    "count": "10",
                    "output": "output.txt",
                    "level": "1",
                    "mode": "normal"
                }
            },
            "高级配置": {
                "description": "详细模式配置示例",
                "checkbox_options": ["verbose", "force"],
                "input_values": {
                    "count": "50",
                    "output": "advanced_output.log",
                    "level": "3",
                    "mode": "safe"
                }
            }
        }
        
        # 获取当前脚本路径
        current_script = sys.argv[0]
        
        result = create_config_app(
            program=current_script,
            title="Rich 界面演示",
            parser=parser,
            preset_configs=preset_configs
        )
        
        if result:
            # Rich模式直接返回结果字典
            process_received_params(result, parser)
    
    except ImportError as e:
        print(f"无法加载 Rich 界面: {e}")


def process_received_params(params, parser):
    """处理从UI接收的参数"""
    print("\n===== UI返回的参数 =====")
    print(params)
    
    # 将参数转换为命令行参数列表
    cmd_args = []
    
    # 添加布尔选项
    for arg, enabled in params.get('options', {}).items():
        if enabled:
            cmd_args.append(arg)
    
    # 添加输入值选项
    for arg, value in params.get('inputs', {}).items():
        if value:  # 只添加非空值
            cmd_args.append(arg)
            cmd_args.append(value)
    
    # 使用parser解析参数
    try:
        args = parser.parse_args(cmd_args)
        process_args(args)
    except Exception as e:
        print(f"参数解析错误: {e}")


def main():
    """主函数"""
    print("PresetUI 演示测试程序")
    print("====================")
    
    if len(sys.argv) > 1:
        # 如果提供了命令行参数，直接处理
        parser = setup_demo_parser()
        args = parser.parse_args()
        process_args(args)
        return
    
    # 否则显示菜单选择界面类型
    print("\n请选择界面类型:")
    print("1. Rich 界面 (终端内)")
    print("2. Textual 界面 (TUI)")
    
    choice = input("请输入选择 (1/2): ").strip()
    
    if choice == '1':
        show_rich_ui()
    elif choice == '2':
        show_textual_ui()
    else:
        print("无效的选择，退出程序")


if __name__ == "__main__":
    main()