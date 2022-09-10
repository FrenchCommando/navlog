#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Copyright (C) 2022 FrenchCommando
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


""""
====================================================================================================================
        This is a tool to generate navlogs for aviation
        Author : FrenchCommando
====================================================================================================================
"""

import key_matcher
import fill_keys
import fill_contents
import input_data.build_json
import utils.forms_clean


if __name__ == '__main__':

    key_matcher.main()
    fill_keys.main()

    input_data.build_json.build_input(folder="stuff")

    fill_contents.main()

    # utils.forms_clean.clean()
