#!/usr/bin/env python3
# -*- coding: utf-8 -*-~

import aiohttp
from bs4 import BeautifulSoup


def _parse_video_info_from_html(html_str: str):
    soup = BeautifulSoup(html_str, "lxml")
    # 标题 作者 简介
    video_title = soup.find(name="h1", class_="video-title tit").text.strip()
    video_author = (
        soup.find(name="div", class_="up-info_right")
        .find(name="a", class_="username")
        .text.strip()
    )
    video_desc = soup.find(name="span", class_="desc-info-text").text.strip()

    # 发布日期 播放数
    video_data_list_div = soup.find(name="div", class_="video-data-list")
    video_pubdate = video_data_list_div.find(
        name="span", class_="pudate-text"
    ).text.strip()
    video_viewcount = video_data_list_div.find(
        name="span", class_="view item"
    ).text.strip()

    # TODO(hukening):添加获取封面的支持
    # video_cover = soup.find(name="div",class_="video-capture").find(name="picture",class_="b-img__inner").src

    return {
        "title": video_title,
        "author": video_author,
        "desc": video_desc,
        "pubdate": video_pubdate,
        "viwecount": video_viewcount,
    }


async def get_video_info_by_bvid(bvid: str):
    async with aiohttp.ClientSession("https://www.bilibili.com") as session:
        async with session.get(f"/video/{bvid}") as response:
            if response.status == 200:
                return _parse_video_info_from_html(await response.text())
            else:
                # return None if failed.
                pass
