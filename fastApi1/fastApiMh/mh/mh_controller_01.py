#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from datetime import date
from enum import Enum
from typing import Optional, List

from fastapi import APIRouter, Query, Path, Body, Cookie, Header
from pydantic import BaseModel, Field



app_mh = APIRouter()



@app_mh.get("/parameters")
def parameters():
    return {"message": "This is a message"}


@app_mh.get("/home_commic")
def home_comic():
    from .data.home_comic import h_commic
    return h_commic


@app_mh.get("/comic_detail")
def comic_detail():
    from .data.comic_detail import c_detail
    return c_detail

@app_mh.get("/comic_reader_image")
def comic_reader_image():
    from .data import c_reader_image
    return c_reader_image

@app_mh.get("/home_video")
def home_video():
    from .data import h_video
    return h_video

@app_mh.get("/comic_detail_tab1")
def comic_detail_tab1():
    from .data import c_detail_tab1
    return c_detail_tab1

@app_mh.get("/comic_detail_tab2")
def comic_detail_tab2():
    from .data import c_detail_tab2
    return c_detail_tab2

@app_mh.get("/comic_detail_tab3")
def comic_detail_tab3():
    from .data import c_detail_tab3
    return c_detail_tab3
