from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from pysc2.agents import base_agent
from pysc2.lib import actions


class SaveSimulationResults(base_agent.BaseAgent):
    units_1 = None
    units_2 = None

    def clean(self):
        self.units_1 = dict([(0, 0)])
        self.units_2 = dict([(0, 0)])

    def increment(self, units, unit_type):
        if unit_type in units:
            units[unit_type] += 1
        else:
            units[unit_type] = 1

    def add(self, player, unit_type):
        if player == 1:
            self.increment(self.units_1, unit_type)
        else:
            self.increment(self.units_2, unit_type)

    def get_units(self, obs):
        units_arr = obs[3]["units"]
        for unit in units_arr:
            self.add(unit.owner, unit.unit_type)

    def step(self, obs):
        if obs.first():
            self.clean()
            self.get_units(obs)
            print("\nBEGINBEGINBEGINBEGINBEGINBEGIN\n")
            print(self.units_1)
            print(self.units_2)
            print("\n\n\n")

        if obs.last():
            self.clean()
            self.get_units(obs)
            print("\nENDINGENDING\n")
            print(self.units_1)
            print(self.units_2)

        return actions.FunctionCall(0, [])
