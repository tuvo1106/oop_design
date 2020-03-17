#!/usr/bin/env python3


class Wicket:
    def __init__(self, wicket_type, player_out, caught_by, runout_by,
                 stumped_by):
        self.__wicket_type = wicket_type
        self.__player_out = player_out
        self.__caught_by = caught_by
        self.__runout_by = runout_by
        self.__stumped_by = stumped_by
