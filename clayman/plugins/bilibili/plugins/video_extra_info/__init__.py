#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""显示 Bilibili 视频详细信息的功能
"""

from nonebot import get_driver, on_message
from nonebot.rule import regex, to_me
from nonebot.matcher import Matcher
from nonebot.params import RegexMatched

from .config import Config
from . import data_source

global_config = get_driver().config
config = Config.parse_obj(global_config)

VideoInfo = on_message(rule=regex(r"BV\S{10}") & to_me())


@VideoInfo.handle()
async def video_info_first_receive(matcher=Matcher, bvid=RegexMatched()):
    video_info = await data_source.get_video_info_by_bvid(bvid)
    if video_info:
        await matcher.finish(
            "标题：{title}\n作者: {author}\n发布日期: {pubdate}\n简介: {desc}".format(**video_info)
        )
    else:
        await matcher.finish("信息检索失败")
