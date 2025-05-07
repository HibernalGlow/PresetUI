"""
PresetUI 包
提供Python TUI配置界面库
"""

import os
import sys
from typing import Optional, List, Tuple

def find_venv_python(search_paths: Optional[List[str]] = None, venv_names: Optional[List[str]] = None) -> Optional[str]:
    """
    在指定路径列表中寻找虚拟环境的Python解释器
    
    Args:
        search_paths: 搜索路径列表，默认为当前目录和父级目录
        venv_names: 虚拟环境文件夹名称，默认为常见的几种
        
    Returns:
        虚拟环境中Python解释器的路径，如果没找到则返回None
    """
    if search_paths is None:
        # 默认搜索当前目录和父级目录
        current_dir = os.path.abspath(os.getcwd())
        parent_dir = os.path.dirname(current_dir)
        search_paths = [current_dir, parent_dir]
    
    if venv_names is None:
        # 默认的虚拟环境名称
        venv_names = ["venv", ".venv", "env", ".env"]
    
    # 确定Python可执行文件的路径格式(根据操作系统)
    python_exe = "python.exe" if os.name == "nt" else "python"
    python_path_format = os.path.join("{}", "bin" if os.name != "nt" else "Scripts", python_exe)
    
    # 在各路径中查找
    for path in search_paths:
        for venv_name in venv_names:
            venv_dir = os.path.join(path, venv_name)
            if os.path.isdir(venv_dir):
                python_path = python_path_format.format(venv_dir)
                if os.path.isfile(python_path):
                    return python_path
    
    return None

def get_python_command() -> Tuple[str, bool]:
    """
    获取适合的Python命令，优先使用虚拟环境
    
    Returns:
        一个元组：(python命令路径, 是否为虚拟环境)
    """
    # 尝试查找虚拟环境
    venv_python = find_venv_python()
    if venv_python:
        return venv_python, True
    
    # 如果没有虚拟环境，使用当前运行的Python解释器
    return sys.executable, False