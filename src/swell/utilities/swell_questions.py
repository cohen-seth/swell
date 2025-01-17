# (C) Copyright 2021- United States Government as represented by the Administrator of the
# National Aeronautics and Space Administration. All Rights Reserved.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# --------------------------------------------------------------------------------------------------


import os
import yaml
from typing import Callable

from swell.swell_path import get_swell_path
from swell.utilities.logger import Logger


# --------------------------------------------------------------------------------------------------
#  @package configuration
#
#  Class containing the configuration. This is a dictionary that is converted from
#  an input yaml configuration file. Various function are included for interacting with the
#  dictionary.
#
# --------------------------------------------------------------------------------------------------


from dataclasses import dataclass


# --------------------------------------------------------------------------------------------------

@dataclass
class SwellQuestion:
    """Basic dataclass for defining Swell questions for suites and tasks"""
    name: str
    dtype: str
    question_type: str
    default_value: str
    prompt: str
    depends: dict = None
    models: list = None
    ask_question: bool = False
    options: str = None

    def get(self, attr, default=None):
        return getattr(self, attr, default)

# --------------------------------------------------------------------------------------------------


@dataclass
class QuestionList:
    """Basic dataclass containing a list of questions for each model, suite, task"""
    name: str
    list_type: str
    questions: list

    def get(self, attr, default=None):
        return getattr(self, attr, default)

# --------------------------------------------------------------------------------------------------
