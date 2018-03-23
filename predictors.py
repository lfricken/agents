
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import numpy
from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features

_PLAYER_RELATIVE = features.SCREEN_FEATURES.player_relative.index
_PLAYER_FRIENDLY = 1
_PLAYER_NEUTRAL = 3  # beacon/minerals
_PLAYER_HOSTILE = 4
_NO_OP = actions.FUNCTIONS.no_op.id
_MOVE_SCREEN = actions.FUNCTIONS.Move_screen.id
_ATTACK_SCREEN = actions.FUNCTIONS.Attack_screen.id
_SELECT_ARMY = actions.FUNCTIONS.select_army.id
_NOT_QUEUED = [0]
_SELECT_ALL = [0]


class LearnPrediction(base_agent.BaseAgent):


    def encode(self):
        return self

    def step(self, obs):
        t = actions.FUNCTIONS.Build_Bunker_screen.id
        return actions.FunctionCall(t, [])

