# (C) Copyright 2021- United States Government as represented by the Administrator of the
# National Aeronautics and Space Administration. All Rights Reserved.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.


# --------------------------------------------------------------------------------------------------


import os
from dataclasses import dataclass

from swell.utilities.swell_questions import SwellQuestion


# --------------------------------------------------------------------------------------------------

cycle_times = SwellQuestion(
    name="cycle_times",
    question_type="suite",
    default_value="defer_to_model",
    ask_question=True,
    options="defer_to_model",
    models=[
        "all_models"
    ],
    prompt="Enter the cycle times for this model.",
    dtype="string-check-list"
)


# --------------------------------------------------------------------------------------------------

ensemble_hofx_packets = SwellQuestion(
    name="ensemble_hofx_packets",
    question_type="suite",
    default_value="defer_to_model",
    models=[
        "all_models"
    ],
    prompt="Enter the number of ensemble packets.",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

ensemble_hofx_strategy = SwellQuestion(
    name="ensemble_hofx_strategy",
    question_type="suite",
    default_value="defer_to_model",
    models=[
        "all_models"
    ],
    prompt="Enter the ensemble hofx strategy.",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

experiment_id = SwellQuestion(
    name="experiment_id",
    question_type="suite",
    default_value="defer_to_code",
    ask_question=True,
    prompt="What is the experiment id?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

experiment_root = SwellQuestion(
    name="experiment_root",
    question_type="suite",
    default_value="defer_to_platform",
    ask_question=True,
    prompt="What is the experiment root (the directory where the experiment will be stored)?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

final_cycle_point = SwellQuestion(
    name="final_cycle_point",
    question_type="suite",
    default_value="2021-12-12T06:00:00Z",
    ask_question=True,
    prompt="What is the time of the final cycle (middle of the window)?",
    dtype="iso-datetime"
)


# --------------------------------------------------------------------------------------------------

marine_models = SwellQuestion(
    name="marine_models",
    question_type="suite",
    default_value="defer_to_model",
    ask_question=True,
    options="defer_to_model",
    models=[
        "geos_marine"
    ],
    prompt="Select the active SOCA models for this model.",
    dtype="string-check-list"
)


# --------------------------------------------------------------------------------------------------

model_components = SwellQuestion(
    name="model_components",
    question_type="suite",
    default_value="defer_to_code",
    ask_question=True,
    options="defer_to_code",
    prompt="Enter the model components for this model.",
    dtype="string-check-list"
)


# --------------------------------------------------------------------------------------------------

runahead_limit = SwellQuestion(
    name="runahead_limit",
    question_type="suite",
    default_value="P4",
    ask_question=True,
    prompt="Since this suite is non-cycling choose how many hours the workflow can run ahead?",
    dtype="string"
)


# --------------------------------------------------------------------------------------------------

skip_ensemble_hofx = SwellQuestion(
    name="skip_ensemble_hofx",
    question_type="suite",
    default_value="defer_to_model",
    models=[
        "all_models"
    ],
    prompt="Enter if skip ensemble hofx.",
    dtype="boolean"
)


# --------------------------------------------------------------------------------------------------

start_cycle_point = SwellQuestion(
    name="start_cycle_point",
    question_type="suite",
    default_value="2021-12-12T00:00:00Z",
    ask_question=True,
    prompt="What is the time of the first cycle (middle of the window)?",
    dtype="iso-datetime"
)


# --------------------------------------------------------------------------------------------------

window_type = SwellQuestion(
    name="window_type",
    question_type="suite",
    default_value="defer_to_model",
    options=[
        "3D",
        "4D"
    ],
    models=[
        "all_models"
    ],
    prompt="Enter the window type for this model.",
    dtype="string-drop-list"
)


# --------------------------------------------------------------------------------------------------
