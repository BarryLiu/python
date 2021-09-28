#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from datetime import date
from enum import Enum
from typing import Optional, List

from fastapi import APIRouter, Query, Path, Body, Cookie, Header,Request
from pydantic import BaseModel, Field
from fastapi.templating import Jinja2Templates

from .mh_service import m_service

app_mh = APIRouter()

templates = Jinja2Templates(directory='./mh/templates')


"""Path Parameters and Number Validations 路径参数和数字验证"""


@app_mh.get("/parameters")
def parameters():
    return {"message": "This is a message"}


@app_mh.get("/home_commic")
def home_comic():
    #from .data.home_comic import h_commic
    h_commic = m_service.service_home_comic()
    return h_commic


@app_mh.get("/comic_detail/{b_id}")
def comic_detail(b_id:int):
    #from .data.comic_detail import c_detail
    c_detail = m_service.service_comic_detail(id=b_id)    
    return c_detail

@app_mh.get("/comic_reader_image/{item_id}")
def comic_reader_image(item_id:int):
    #from .data import c_reader_image
    c_reader_image = m_service.service_reader_image(item_id=item_id)

    return c_reader_image

@app_mh.get("/home_video")
def home_video():
    from .data import h_video
    return h_video

@app_mh.get("/comic_detail_tab1")
def comic_detail_tab1():
    from .data import c_detail_tab1
    return c_detail_tab1

@app_mh.get("/comic_detail_tab2/{b_id}")
def comic_detail_tab2(b_id:int):
    #from .data import c_detail_tab2
    c_detail_tab2 = m_service.service_comic_detail_tab2(b_id)
    return c_detail_tab2

@app_mh.get("/comic_detail_tab3")
def comic_detail_tab3():
    from .data import c_detail_tab3
    return c_detail_tab3



@app_mh.get("/")
def coronavirus(request: Request,keyword: str = None,skip: int = 0, limit: int = 10): 
    data = m_service.service_home_comic_page(keyword=keyword, skip=skip, limit=limit)
    print('data:',data)
    return templates.TemplateResponse("index.html", {
        "data":data,
        "request": request
    })