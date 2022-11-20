#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pydantic import BaseSettings


class Config(BaseSettings):
    # Your Config Here

    class Config:
        extra = "ignore"
