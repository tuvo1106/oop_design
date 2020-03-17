#!/usr/bin/env python3


class Ball:
    def __init__(self, balled_by, played_by, ball_type, wicket, runs,
                 commentary):
        self.__balled_by = balled_by
        self.__played_by = played_by
        self.__type = ball_type
        self.__wicket = wicket
        self.__runs = runs
        self.__commentary = commentary
